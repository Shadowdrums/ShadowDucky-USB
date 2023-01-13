Set objSHL = CreateObject("Wscript.Shell")

MsgBox "Shadow Ducky Is Starting",vbOKOnly,"Its Happening"
objSHL.Popup "Don't Look Away",5,"The Show Is About To Start",vbokonly

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "D:\README\move-ducky.bat" & chr(34), 0
Set WshShell = Nothing

wscript.sleep 6000

Set objSHL = CreateObject("Wscript.Shell")

MsgBox "Just a few more second",vbOKOnly,"Thank you"

