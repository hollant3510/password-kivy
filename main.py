import kivy
import hashlib

from kivy.app import App
from kivymd.theming import ThemeManager
from kivymd.button import MDRaisedButton
from kivymd.button import *
from kivy.uix.boxlayout import BoxLayout

global outputTextOne
global outputTextTwo
global outputTextThree
global outputTextFour
global outputTextFive
global hashTypeSelect1
global hashTypeSelect2

hashTypeSelect1 = 0
hashTypeSelect2 = 0

class CreatePasswordForm(BoxLayout):
    # buttonid is button id string, hashId is string
    def updateHashButton(self, buttonID, hashID):
        print("hello!")
        widget = self.ids[buttonID]
        widget.text = hashID
    #different encoding methods to increase the number of possible different combinations.
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

    #Takes in itself, two strings and an int used to select which hash should be used. Based on the strings and the selected hash it returns a string
    def encodepass(self, o, m1, hashTypeUsed):
        temp = o + m1

        if (hashTypeUsed == 0):
            if (hashTypeSelect1 == 0):
                temp = CreatePasswordForm.encodeMd5(temp)

            elif (hashTypeSelect1 == 1):
                temp = CreatePasswordForm.encodeSha1(temp)

            elif (hashTypeSelect1 == 2):
                temp = CreatePasswordForm.encodeSha224(temp)

            elif (hashTypeSelect1 == 3):
                temp = CreatePasswordForm.encodeSha256(temp)
            
            elif (hashTypeSelect1 == 4):
                temp = CreatePasswordForm.encodeSha384(temp)
            
            elif (hashTypeSelect1 == 5):
                temp = CreatePasswordForm.encodeSha512(temp)
        

        if (hashTypeUsed == 1):
            if (hashTypeSelect2 == 0):
                temp = CreatePasswordForm.encodeMd5(temp)

            elif (hashTypeSelect2 == 1):
                temp = CreatePasswordForm.encodeSha1(temp)

            elif (hashTypeSelect2 == 2):
                temp = CreatePasswordForm.encodeSha224(temp)

            elif (hashTypeSelect2 == 3):
                temp = CreatePasswordForm.encodeSha256(temp)
            
            elif (hashTypeSelect2 == 4):
                temp = CreatePasswordForm.encodeSha384(temp)
            
            elif (hashTypeSelect2 == 5):
                temp = CreatePasswordForm.encodeSha512(temp)

        return temp.hexdigest()


    #Used when hashing using two layers

    # Updates Text output One whenever called with the hash of input1+input2. Stores this value in outputTextOne(a global variable) and makes hashoutput field in the kv file display a shortened version to fit on the screen.
    # Shortens to 15 characters.     
    def updateTextOne(self, input1, input2, hashTypeSelect):
        outputTextOne = CreatePasswordForm.encodepass(self, input1, input2, hashTypeSelect)
        tempor = self.ids['hashoutput']
        if len(outputTextOne) > 15:
            tempor.text = outputTextOne[:15] + "..."
        else:
            tempor.text = outputTextOne


    #Updates Text output Two whenever called with the hash of input1+input2. Stores this value in outputTextTwo(a global variable) and makes newpassword field in the kv file display a shortened version(the first 20 characters)
    def updateTextTwo(self, input1, input2, hashTypeSelect):
        outputTextTwo = CreatePasswordForm.encodepass(self, input1, input2, hashTypeSelect)
        tempor = self.ids['newpassword']
        tempor.text = outputTextTwo


    #Used when hashing using three layers

    # Updates Text output One whenever called with the hash of input1+input2. Stores this value in outputTextOne(a global variable) and makes hashoutput field in the kv file display a shortened version to fit on the screen.
    # Shortens to 15 characters.     
    def updateTextThree(self, input1, input2, hashTypeSelect):
        outputTextThree = CreatePasswordForm.encodepass(self, input1, input2, hashTypeSelect)
        tempor = self.ids['Placeholder1']
        if len(outputTextThree) > 15:
            tempor.text = outputTextThree[:15] + "..."
        else:
            tempor.text = outputTextThree


    # Updates Text output One whenever called with the hash of input1+input2. Stores this value in outputTextOne(a global variable) and makes hashoutput field in the kv file display a shortened version to fit on the screen.
    # Shortens to 15 characters.     
    def updateTextFour(self, input1, input2, hashTypeSelect):
        outputTextFour = CreatePasswordForm.encodepass(self, input1, input2, hashTypeSelect)
        tempor = self.ids['Placeholder2']
        if len(outputTextFour) > 15:
            tempor.text = outputTextFour[:15] + "..."
        else:
            tempor.text = outputTextFour


    #Updates Text output Two whenever called with the hash of input1+input2. Stores this value in outputTextTwo(a global variable) and makes newpassword field in the kv file display a shortened version(the first 20 characters)
    def updateTextFive(self, input1, input2, hashTypeSelect):
        outputTextFive = CreatePasswordForm.encodepass(self, input1, input2, hashTypeSelect)
        tempor = self.ids['Placeholder3']
        tempor.text = outputTextFive

class PasswordApp(App):
    theme_cls = ThemeManager()
    hash_one_items = [
        {'viewclass': 'MDMenuItem', 'text': 'MD5', "on_press": "app.updateHashButton('hashselector1', 'MD5')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA1', "on_press": "app.updateHashButton('hashselector1', 'SHA1')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA224', "on_press": "app.updateHashButton('hashselector1', 'SHA224')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA256', "on_press": "app.updateHashButton('hashselector1', 'SHA256')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA384', "on_press": "app.updateHashButton('hashselector1', 'SHA384')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA512', "on_press": "app.updateHashButton('hashselector1', 'SHA512')"}
    ]

    hash_two_items = [
        {'viewclass': 'MDMenuItem', 'text': 'MD5', "on_press": "app.updateHashButton('hashselector2', 'MD5')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA1', "on_press": "app.updateHashButton('hashselector2', 'SHA1')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA224', "on_press": "app.updateHashButton('hashselector2', 'SHA224')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA256', "on_press": "app.updateHashButton('hashselector2', 'SHA256')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA384', "on_press": "app.updateHashButton('hashselector2', 'SHA384')"},
        {'viewclass': 'MDMenuItem', 'text': 'SHA512', "on_press": "app.updateHashButton('hashselector2', 'SHA512')"}
    ]

    pass

if __name__ == '__main__':
        PasswordApp().run()
