@echo off

set inno_dir=

if defined INNO_HOME (
    if exist "%INNO_HOME%\ISCC.exe" (
        set "inno_dir=%INNO_HOME%"
    )
)

if %PROCESSOR_ARCHITECTURE%==x86 (
    set RegQry=HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Inno Setup 5_is1
) else (
    set RegQry=HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Inno Setup 5_is1
)

if not defined inno_dir (
    for /F "tokens=2*" %%a in ('reg query "%RegQry%" /v InstallLocation ^|findstr InstallLocation') do set inno_dir=%%b
)

if not defined inno_dir (
    for %%X in (ISCC.exe) do (set inno_dir=%%~dp$PATH:X)
)

if defined inno_dir (
    "%inno_dir%\ISCC.exe" %1
) else (
    echo "Error, build system cannot find NSIS! Please reinstall it, add ISCC.exe to your PATH, or defined the INNO_HOME environment variable."
)