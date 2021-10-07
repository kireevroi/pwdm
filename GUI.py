from kivy.app import App
import kivy
from random import randint
from os import path

kivy.require('1.9.0')

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.lang import Builder

Builder.load_file(path.join(path.dirname(__file__), 'view\mMenu.kv'))

Config.set('graphics', 'resizable', 1)

class pwdgengui(App):

    def build(self):
        root_widget = BoxLayout(orientation='vertical')

        output_label = Label(size_hint_y=1)

        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')

        button_grid = GridLayout(cols=4, size_hint_y=2)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))

        clear_button = Button(text='clear', size_hint_y=None,
                              height=100)

        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_button)

        return root_widget


        return layout
if __name__ == '__main__':
    pwdgengui().run()
