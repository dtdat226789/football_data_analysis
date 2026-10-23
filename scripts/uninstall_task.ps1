<#
.SYNOPSIS
    Removes the "FootballDataRefresh" scheduled task created by install_task.ps1.

.DESCRIPTION
    Deletes the scheduled task. Does not touch anything the refresh job wrote:
    the raw data, the database, the analysis reports and logs/ all stay.

.PARAMETER TaskName
    Scheduled task name. Default: FootballDataRefresh

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File scripts\uninstall_task.ps1
#>
[CmdletBinding(SupportsShouldProcess)]
param(
    [string]$TaskName = 'FootballDataRefresh'
)

$ErrorActionPreference = 'Stop'

$task = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if (-not $task) {
    Write-Host "Task '$TaskName' is not registered; nothing to do."
    exit 0
}

if ($PSCmdlet.ShouldProcess($TaskName, 'Delete scheduled task')) {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Removed '$TaskName'." -ForegroundColor Green
    Write-Host "Data and logs were left untouched."
}
