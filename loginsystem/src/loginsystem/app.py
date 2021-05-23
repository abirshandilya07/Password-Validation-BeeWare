"""
A basic login screen and validation
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class LoginSystem(toga.App):


    def startup(self):
        name_lbl = toga.Label('Name       : ', style=Pack(padding_top=20))
        password_lbl = toga.Label('Password : ', style=Pack(padding_top=20))
        self.name_inp = toga.TextInput(style=Pack(padding_top=20))
        self.password_inp  = toga.PasswordInput(style=Pack(padding_top=20))
        submit_btn = toga.Button('Log in', style=Pack(padding_left=20,padding_top=10), on_press=self.validate_pass)
        box1 = toga.Box()
        box2 = toga.Box()
        btn_box = toga.Box()

        #adding in boxes   
        box1.add(name_lbl) 
        box1.add(self.name_inp)
        box2.add(password_lbl)
        box2.add(self.password_inp)
        btn_box.add(submit_btn)
        main_box = toga.Box(style=Pack(direction=COLUMN))
        main_box.add(box1)
        main_box.add(box2)
        main_box.add(btn_box)
        self.main_box = main_box
        
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
    def validate_pass(self,widget):
        if self.password_inp.value == 'abir@123':
            self.main_window.info_dialog('Log in',"Your logged in successfully {}".format(self.name_inp.value))
        else:
            self.main_window.info_dialog('Log in',"Incorrect password {}".format(self.name_inp.value))          
def main():
    return LoginSystem()
