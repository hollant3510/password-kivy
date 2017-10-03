from kivy.app import App
from kivymd.theming import ThemeManager
from kivymd.button import MDRaisedButton
from kivymd.button import *


class PasswordApp(App):
    theme_cls = ThemeManager()

    menu_items = [{'viewclass': 'MDMenuItem', 'text': 'MD5', "on_press": "app.show_example_date_picker(1,1)"},
                  {'viewclass': 'MDMenuItem', 'text': 'SHA-1', "on_press": "app.show_example_date_picker(1,1)"},
                  {'viewclass': 'MDMenuItem', 'text': 'SHA-256', "on_press": "app.show_example_date_picker(1,1)"}]

    pass

if __name__ == '__main__':
        PasswordApp().run()
