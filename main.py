import kivy
import hashlib

from kivy.app import App
from kivymd.theming import ThemeManager
from kivymd.button import MDRaisedButton
from kivymd.button import *
from kivy.uix.boxlayout import BoxLayout


class CreatePasswordForm(BoxLayout): 
    def encodeMd5(tempor):
        tempor = hashlib.md5(tempor.encode())
        return tempor

    def encodeSha1(tempor):
        tempor = hashlib.sha1(tempor.encode())
        return tempor

    def encodeSha224(tempor):
        tempor = hashlib.sha224(tempor.encode())
        return tempor

    def encodeSha256(tempor):
        tempor = hashlib.sha256(tempor.encode())
        return tempor

    def encodeSha384(tempor):
        tempor = hashlib.sha384(tempor.encode())
        return tempor

    def encodeSha512(tempor):
        tempor = hashlib.sha512(tempor.encode())
        return tempor

#http://pythoncentral.io/hashing-strings-with-python/

    def encodepass(self, o, m1):
        temp = o + m1
        temp = CreatePasswordForm.encodeMd5(temp)
        return (temp.hexdigest())
        
        
    def updateTextOne(self, input1, input2):
        temp = CreatePasswordForm.encodepass(self, input1, input2)
        tempor = self.ids['hashoutput']
        tempor.text = temp

    def updateTextTwo(self, input1, input2):
        temp = CreatePasswordForm.encodepass(self, input1, input2)
        tempor = self.ids['newpassword']
        tempor.text = temp

class PasswordApp(App):
    theme_cls = ThemeManager()
    menu_items = [{'viewclass': 'MDMenuItem', 'text': 'MD5', "on_press": "app.show_example_date_picker(1,1)"}]

    pass

if __name__ == '__main__':
        PasswordApp().run()
