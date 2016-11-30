@echo off

rem Check %PATH% for ISCC.exe
for %%X in (ISCC.exe) do (set inno_path=%%~dp$PATH:X)
if defined inno_path goto :found

rem Check registry for InnoSetup install path
if %PROCESSOR_ARCHITECTURE%==x86 (
    set RegQry=HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Inno Setup 5_is1
) else (
    set RegQry=HKLM\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Inno Setup 5_is1
)

for /F "tokens=2*" %%a in ('reg query "%RegQry%" /v InstallLocation ^|findstr InstallLocation') do set inno_path=%%b

:found
if defined inno_path (
    "%inno_path%\ISCC.exe" %1
) else (
    echo 'ISCC.exe' is not recognized as an internal or external command, operable program or batch file.
)
