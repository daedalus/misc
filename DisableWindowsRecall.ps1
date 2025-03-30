# PowerShell script to disable Windows Recall

# Disable Recall via Registry

$regPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsAI" $regName = "AllowRecallEnablement" $regValue = 0

# Create registry key if it does not exist

if (!(Test-Path $regPath)) { New-Item -Path $regPath -Force | Out-Null }

# Set the registry value to disable Recall

Set-ItemProperty -Path $regPath -Name $regName -Value $regValue -Type DWord

# Stop and disable Recall-related service (if applicable)

$serviceName = "RecallService" # Replace with actual service name if known if (Get-Service -Name $serviceName -ErrorAction SilentlyContinue) { Stop-Service -Name $serviceName -Force Set-Service -Name $serviceName -StartupType Disabled }

# Confirm changes

Write-Host "Windows Recall has been disabled. Please restart your computer for changes to take effect."

