# The MIT License (MIT)
# Copyright (c) 2016 Jan T. Sott
#
# https://github.com/idleberg/sublime-innosetup

$DebugPreference = "SilentlyContinue"

If (-Not (Test-Path HKLM:)) {
    # This should never be shown when run from Sublime Text
    Write-Host "Error: This script is meant to be run on Windows only"
    Exit
}

If ($PSVersionTable.PSVersion.Major -lt 3) {
    # PowerShell 3.0 is integrated with Windows 8 and with Windows Server 2012
    Write-Host "Error: This script requires PowerShell 3.0 (or higher)"
    Exit
}

If (Get-Command "ISCC.exe" -ErrorAction SilentlyContinue) {
    Write-Debug "'ISCC.exe' found in %PATH%"
    $iscc = "ISCC.exe"
} Else {
    Write-Debug "Checking registry for NSIS installation path"
    If ([System.Environment]::Is64BitOperatingSystem) {
        $inno_key = 'HKLM:\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Inno Setup 5_is1'
    } Else {
        $inno_key = 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Inno Setup 5_is1'
    }

    $inno_path = (Get-ItemProperty -Path $inno_key -Name InstallLocation).InstallLocation
    $iscc = Join-Path -Path $inno_path -ChildPath "ISCC.exe"
}

If (-Not $iscc) {
    Write-Host "'ISCC.exe' is not recognized as an internal or external command, operable program or batch file."
} Else {
    Write-Debug "Executing `"$iscc $args`""
    Start-Process -NoNewWindow -FilePath "$iscc" -ArgumentList "`"$args`""
}
