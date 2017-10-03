import kivy
import hashlib

from kivy.app import App
from kivymd.theming import ThemeManager
from kivymd.button import MDRaisedButton
from kivymd.button import *
from kivy.uix.boxlayout import BoxLayout


class CreatePasswordForm(BoxLayout):
    def encodepass(self, o, m1, m2):
        temp = o + m1 + m2
        temp = hashlib.md5(temp.encode())
        return (temp.hexdigest())
        
 

class PasswordApp(App):
    theme_cls = ThemeManager()
    menu_items = [{'viewclass': 'MDMenuItem', 'text': 'MD5', "on_press": "app.show_example_date_picker(1,1)"}]

    pass

if __name__ == '__main__':
        PasswordApp().run()
