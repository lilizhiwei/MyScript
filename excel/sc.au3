;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("打开","","Edit1")

; Wait 10 senconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)

; Set the File name text on the Edit field
ControlSetText("打开","","Edit1","C:\Users\Administrator\MyScript\excel\shangcuo.xls")
Sleep(2000)

;Click on the Open button
ControlClick("打开","","Button1");