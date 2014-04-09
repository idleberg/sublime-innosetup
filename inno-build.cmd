@echo off

set inno_compiler=

if defined INNO_HOME (
    if exist "%INNO_HOME%\makensis.exe" (
        set "inno_compiler=%INNO_HOME%"
    )
)

if %PROCESSOR_ARCHITECTURE%==x86 (
    set RegQry=HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Inno Setup 5_is1
) else (
    set RegQry=HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Inno Setup 5_is1
)

if not defined inno_compiler (
    for /F "tokens=2*" %%a in ('reg query "%RegQry%" /v InstallLocation ^|findstr InstallLocation') do set inno_compiler=%%b
)

if not defined inno_compiler (
    for %%X in (ISCC.exe) do (set inno_compiler=%%~dp$PATH:X)
)

if defined inno_compiler (
    "%inno_compiler%\ISCC.exe" %1
) else (
    echo "Error, build system cannot find NSIS! Please reinstall it, add ISCC.exe to your PATH, or defined the INNO_HOME environment variable."
)