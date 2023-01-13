Set objSHL = CreateObject("Wscript.Shell")

MsgBox "Informer is up and running",vbOKOnly,"Informer Starting"
objSHL.Popup "Informer report is underway",10,"Informer Running",vbokonly


Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "D:\INFORMER\informer.bat" & chr(34), 0
Set WshShell = Nothing

wscript.sleep 6000

objSHL.Popup "Informer report is Ready",5,"Informer Has Finsihed",vbokonly

