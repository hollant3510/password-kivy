import hashlib

from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.uix.boxlayout import BoxLayout

hash_type_select_one = 0
hash_type_select_two = 0


class CreatePasswordForm(BoxLayout):
    # buttonid is button id string, hashId is string
    def update_hash_button(self, button_id, hash_id):
        print("hello!")
        widget = self.ids[button_id]
        widget.text = hash_id

    # different encoding methods to increase the number of possible different combinations.
    def encode_md5(self):
        return hashlib.md5(self.encode())

    def encode_sha1(self):
        return hashlib.sha1(self.encode())

    def encode_sha224(self):
        return hashlib.sha224(self.encode())

    def encode_sha256(self):
        return hashlib.sha256(self.encode())

    def encode_sha384(self):
        return hashlib.sha384(self.encode())

    def encode_sha512(self):
        return hashlib.sha512(self.encode())

    # Takes in itself, two strings and an int used to select which hash should be used
    # Based on the strings and the selected hash it returns a string
    @staticmethod
    def encode_pass(o, m1, hash_type_used):
        temp = o + m1

        if hash_type_used == 0:
            if hash_type_select_one == 0:
                temp = CreatePasswordForm.encode_md5(temp)

            elif hash_type_select_one == 1:
                temp = CreatePasswordForm.encode_sha1(temp)

            elif hash_type_select_one == 2:
                temp = CreatePasswordForm.encode_sha224(temp)

            elif hash_type_select_one == 3:
                temp = CreatePasswordForm.encode_sha256(temp)
            
            elif hash_type_select_one == 4:
                temp = CreatePasswordForm.encode_sha384(temp)
            
            elif hash_type_select_one == 5:
                temp = CreatePasswordForm.encode_sha512(temp)

        if hash_type_used == 1:
            if hash_type_select_two == 0:
                temp = CreatePasswordForm.encode_md5(temp)

            elif hash_type_select_two == 1:
                temp = CreatePasswordForm.encode_sha1(temp)

            elif hash_type_select_two == 2:
                temp = CreatePasswordForm.encode_sha224(temp)

            elif hash_type_select_two == 3:
                temp = CreatePasswordForm.encode_sha256(temp)
            
            elif hash_type_select_two == 4:
                temp = CreatePasswordForm.encode_sha384(temp)
            
            elif hash_type_select_two == 5:
                temp = CreatePasswordForm.encode_sha512(temp)

        return temp.hexdigest()

    # Used when hashing using two layers
    # Updates Text output One whenever called with the hash of input1+input2.
    # Stores this value in outputTextOne(a global variable) and makes hash output
    # field in the kv file display a shortened version to fit on the screen.
    # Shortens to 15 characters.     
    def update_text_one(self, input1, input2, hash_type_select):
        output_text_one = CreatePasswordForm.encode_pass(input1, input2, hash_type_select)
        tempor = self.ids['hashoutput']
        if len(output_text_one) > 15:
            tempor.text = output_text_one[:15] + "..."
        else:
            tempor.text = output_text_one

    # Updates Text output Two whenever called with the hash of input1+input2.
    # Stores this value in outputTextTwo(a global variable) and makes
    # new password field in the kv file display a shortened version(the first 20 characters)
    def update_text_two(self, input1, input2, hash_type_select):
        output_text_two = CreatePasswordForm.encode_pass(input1, input2, hash_type_select)
        tempor = self.ids['newpassword']
        tempor.text = output_text_two

    # Used when hashing using three layers
    # Updates Text output One whenever called with the hash of input1+input2.
    # Stores this value in outputTextOne(a global variable) and makes hash output field
    # in the kv file display a shortened version to fit on the screen.
    # Shortens to 15 characters.     
    def update_text_three(self, input1, input2, hash_type_select):
        output_text_three = CreatePasswordForm.encode_pass(input1, input2, hash_type_select)
        tempor = self.ids['Placeholder1']
        if len(output_text_three) > 15:
            tempor.text = output_text_three[:15] + "..."
        else:
            tempor.text = output_text_three

    # Updates Text output One whenever called with the hash of input1+input2.
    # Stores this value in outputTextOne(a global variable) and makes hashoutput
    # field in the kv file display a shortened version to fit on the screen.
    # Shortens to 15 characters.     
    def update_text_four(self, input1, input2, hash_type_select):
        output_text_four = CreatePasswordForm.encode_pass(input1, input2, hash_type_select)
        tempor = self.ids['Placeholder2']
        if len(output_text_four) > 15:
            tempor.text = output_text_four[:15] + "..."
        else:
            tempor.text = output_text_four

    # Updates Text output Two whenever called with the hash of input1+input2.
    # Stores this value in outputTextTwo(a global variable) and makes newpassword field
    # in the kv file display a shortened version(the first 20 characters)
    def update_text_five(self, input1, input2, hash_type_select):
        output_text_five = CreatePasswordForm.encode_pass(input1, input2, hash_type_select)
        tempor = self.ids['Placeholder3']
        tempor.text = output_text_five


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
