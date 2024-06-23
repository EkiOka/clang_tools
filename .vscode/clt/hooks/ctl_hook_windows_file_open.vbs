dim ws
dim fso
dim vbs_dir
dim bat_name
set fso = createObject("Scripting.FileSystemObject")
set ws = CreateObject("Wscript.Shell")

vbs_dir = fso.getParentFolderName(WScript.ScriptFullName)
bat_name = "ctl_hook_windows_file_open.bat"
ws.run "cmd /c "&vbs_dir&"\"&bat_name ,vbhide
