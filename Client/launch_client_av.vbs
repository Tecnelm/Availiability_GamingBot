Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "<absolute path to script>\start.bat" & Chr(34), 0
Set WshShell =Nothing