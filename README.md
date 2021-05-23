# Password-Validation-BeeWare
A log in system made in beeware python and used toga as the toolkit
---
This project's code is in the app.py file which you can find at this address:
Password-Validation-BeeWare\loginsystem\src\loginsystem\app.py

# A closer look on the code
---
```
    """
    A basic login screen and validation
    """
    import toga
    from toga.style import Pack
    from toga.style.pack import COLUMN, ROW
```
So, in this we are importing our GUI-toolkit toga and its components

```
    class LoginSystem(toga.App):

        def startup(self):
            name_lbl = toga.Label('Name       : ', style=Pack(padding_top=20))
            password_lbl = toga.Label('Password : ', style=Pack(padding_top=20))
            self.name_inp = toga.TextInput(style=Pack(padding_top=20))
            self.password_inp  = toga.PasswordInput(style=Pack(padding_top=20))
```
In this part we are making our application in the pre-made class of our application which inherits from toga.app an we are making some labels and text inputs in our basic function.. and password input for the password because we can't show it..

```
    submit_btn = toga.Button('Log in', style=Pack(padding_left=20,padding_top=10), on_press=self.validate_pass)
    box1 = toga.Box()
    box2 = toga.Box()
    btn_box = toga.Box()

```
In this part we are making our Log in button and defining the boxes in which all the widgets would be added and when we press the log in button the validate function will be called which will validate the password
```
    #adding widgets in boxes   
    box1.add(name_lbl) 
    box1.add(self.name_inp)
    box2.add(password_lbl)
    box2.add(self.password_inp)
    btn_box.add(submit_btn)
```
In this part we are adding the widgets in the boxes we made earlier
```
    main_box = toga.Box(style=Pack(direction=COLUMN))
    main_box.add(box1)
    main_box.add(box2)
    main_box.add(btn_box)
    self.main_box = main_box
```
Now we have made a main box which will cover all the content in the screen
```
    self.main_window = toga.MainWindow(title=self.formal_name)
    self.main_window.content = main_box
    self.main_window.show()
```
Now we have specified main_box as the content of our screen and we have showed our window
```
    def validate_pass(self,widget):
        if self.password_inp.value == 'abir@123':
            self.main_window.info_dialog('Log in',"Your logged in successfully {}".format(self.name_inp.value))
        else:
            self.main_window.info_dialog('Log in',"Incorrect password {}".format(self.name_inp.value))          
```
Now comes the real validation function which will be called on the click of Log in button, if the password is abir@123 then it will show the message of login successful otherwise the incorrect password message
```
    def main():
        return LoginSystem()
```
Now the main function 