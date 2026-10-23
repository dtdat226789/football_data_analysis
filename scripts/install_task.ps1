<#
.SYNOPSIS
    Registers the "FootballDataRefresh" Windows scheduled task that keeps the
    football dataset current.

.DESCRIPTION
    The task wakes the WSL distro through wsl.exe and runs
    scripts/refresh_data.sh, which refreshes raw API data, fixtures, validation
    reports, the Postgres build, the analysis reports and the dashboard.

    Two triggers are registered on purpose:

      * LogonTrigger    - fires when you log in, delayed by -LogonDelayMinutes
                          so WSL and the network are up first. This is the
                          "when I start the laptop" trigger.
      * CalendarTrigger - fires daily at -DailyTime with StartWhenAvailable, so
                          a run is not lost if the laptop was off at that hour.

    Both are needed because this machine has Windows Fast Startup enabled
    (HKLM\...\Session Manager\Power\HiberbootEnabled = 1). A hybrid shutdown
    restores the persisted user session instead of creating a new one, so a
    LogonTrigger may not fire at all after Shut down -> power on. The calendar
    trigger does not depend on the boot type.

    refresh_data.sh also stamps the date of each fully successful run and skips
    a second run on the same calendar day, so the double trigger does not cost
    two 20-45 minute sweeps.

.PARAMETER TaskName
    Scheduled task name. Default: FootballDataRefresh

.PARAMETER Distro
    WSL distribution to run in. Default: Ubuntu

.PARAMETER LinuxPath
    Absolute Linux path to refresh_data.sh. Empty by default, which resolves to
    refresh_data.sh next to this script, converted to its WSL path. Override it
    when the refresh script lives elsewhere.

.PARAMETER DailyTime
    HH:mm for the daily calendar trigger. Default: 06:00

.PARAMETER LogonDelayMinutes
    Delay after logon before running, so WSL boots and Wi-Fi connects.
    Default: 3

.PARAMETER TimeLimit
    ExecutionTimeLimit as an ISO-8601 duration. Default: PT2H

.PARAMETER PrintOnly
    Print the task XML and exit without registering anything.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File scripts\install_task.ps1

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File scripts\install_task.ps1 -DailyTime 05:30

.NOTES
    Run from Windows PowerShell. Does not require elevation: the task runs at
    LeastPrivilege in the interactive user's session, which is required because
    WSL distributions are registered per Windows user (HKCU\...\Lxss), so a
    SYSTEM-scoped task would not find the distro.
#>
[CmdletBinding()]
param(
    [string]$TaskName        = 'FootballDataRefresh',
    [string]$Distro          = 'Ubuntu',
    [string]$LinuxPath       = '',
    [ValidatePattern('^\d{2}:\d{2}$')]
    [string]$DailyTime       = '06:00',
    [int]$LogonDelayMinutes  = 3,
    [string]$TimeLimit       = 'PT2H',
    [switch]$PrintOnly
)

$ErrorActionPreference = 'Stop'

function ConvertTo-WslPath([string]$WindowsPath) {
    # E:\code\repo\scripts -> /mnt/e/code/repo/scripts
    if ($WindowsPath -match '^([A-Za-z]):\\(.*)$') {
        return "/mnt/$($Matches[1].ToLower())/$($Matches[2] -replace '\\', '/')"
    }
    throw "Cannot convert '$WindowsPath' to a WSL path; pass -LinuxPath explicitly."
}

# Default to refresh_data.sh beside this script so the task keeps working after
# the repo moves, instead of pinning one checkout layout.
if (-not $LinuxPath) {
    $LinuxPath = ConvertTo-WslPath (Join-Path $PSScriptRoot 'refresh_data.sh')
    if (-not (Test-Path $LinuxPath)) {
        Write-Warning "LinuxPath resolved to '$LinuxPath' via wsl.exe, which cannot be tested from here; verify it exists inside the distro."
    }
}

# The logon trigger must name a fully-qualified account.
$UserId = "$env:USERDOMAIN\$env:USERNAME"
$Wsl   = Join-Path $env:SystemRoot 'System32\wsl.exe'

# CalendarTrigger StartBoundary must be an absolute datetime; the time of day
# is what matters and the date only anchors the first occurrence.
$StartBoundary = '{0}T{1}:00' -f (Get-Date -Format 'yyyy-MM-dd'), $DailyTime

if ($LinuxPath -match '\s') {
    throw "LinuxPath must not contain spaces (wsl.exe argument splitting): $LinuxPath"
}

$Arguments = "-d $Distro -- bash $LinuxPath"

$Xml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Description>Refresh the football dataset (raw API data, fixtures, validation, Postgres build, analysis, dashboard) by running scripts/refresh_data.sh in WSL.</Description>
    <Author>$UserId</Author>
  </RegistrationInfo>
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>$UserId</UserId>
      <Delay>PT${LogonDelayMinutes}M</Delay>
    </LogonTrigger>
    <CalendarTrigger>
      <StartBoundary>$StartBoundary</StartBoundary>
      <Enabled>true</Enabled>
      <ScheduleByDay>
        <DaysInterval>1</DaysInterval>
      </ScheduleByDay>
    </CalendarTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>$UserId</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>true</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>false</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>$TimeLimit</ExecutionTimeLimit>
    <Priority>7</Priority>
    <RestartOnFailure>
      <Interval>PT15M</Interval>
      <Count>3</Count>
    </RestartOnFailure>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>$Wsl</Command>
      <Arguments>$Arguments</Arguments>
    </Exec>
  </Actions>
</Task>
"@

# Fail loudly here rather than handing malformed XML to Task Scheduler.
$null = [xml]$Xml

Write-Host "Task XML is well-formed." -ForegroundColor DarkGray
Write-Host "  name        : $TaskName"
Write-Host "  account     : $UserId"
Write-Host "  command     : $Wsl"
Write-Host "  arguments   : $Arguments"
Write-Host "  logon delay : $LogonDelayMinutes min"
Write-Host "  daily time  : $DailyTime (StartWhenAvailable)"
Write-Host "  time limit  : $TimeLimit, 3 retries 15 min apart"

if ($PrintOnly) {
    Write-Host "`n--- PrintOnly: XML not registered ---" -ForegroundColor Yellow
    Write-Host $Xml
    exit 0
}

$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "`nTask '$TaskName' already exists; replacing it." -ForegroundColor Yellow
}

Register-ScheduledTask -TaskName $TaskName -Xml $Xml -Force | Out-Null

Write-Host "`nRegistered '$TaskName'." -ForegroundColor Green
Write-Host ""
Write-Host "Useful commands:"
Write-Host "  schtasks /run /tn $TaskName              # trigger it now"
Write-Host "  schtasks /query /tn $TaskName /v /fo list # status and last result"
Write-Host "  powershell -File scripts\uninstall_task.ps1 # remove it"
Write-Host ""
Write-Host "Progress is logged inside WSL:  tail -f logs/refresh_latest.log"
