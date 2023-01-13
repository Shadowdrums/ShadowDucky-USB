Set objSHL = CreateObject("Wscript.Shell")

MsgBox "Shadow Ducky Is Almost There",vbOKOnly,"Its Happening Soon"
objSHL.Popup "Don't Look Away",5,"The Show Is About To Start",vbokonly


Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Intel\RubberDucky.bat" & chr(34), 0
Set WshShell = Nothing