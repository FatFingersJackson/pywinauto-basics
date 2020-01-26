from pywinauto.application import Application
import sys

from pywinauto.application import Application
# Start a new process and specify a path to the text file



exe_path = r"..\\WinFormsUITest\\WinFormsUITest\bin\Debug\WinFormsUITest.exe"
app = Application().start(exe_path, timeout=10)
main_dlg = app.window(title="Main Window")
main_dlg.wait('visible')
main_dlg.print_control_identifiers()


#main_dlg.Edit.type_keys("Testing...", with_spaces=True,pause=0.5)
main_dlg.child_window(auto_id="textBox1", control_type="System.Windows.Forms.TextBox").type_keys("Testing...", with_spaces=True,pause=0.5)

#main_dlg.Button.click()
main_dlg.btn1.click()

sys.exit()
app = Application().start('notepad.exe', timeout=10)
main_dlg = app.UntitledNotepad
main_dlg.wait('visible')
main_dlg = app.window(title='Untitled - Notepad')
main_dlg.print_control_identifiers()
