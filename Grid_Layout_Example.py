from kivy.uix.button import Button
from kivy.app import App  
from kivy.uix.gridlayout import GridLayout    
from kivy.lang import Builder


class Grid(GridLayout):
    pass


presentation = Builder.load_file("glout.kv")

class UcoeApp(App):
    def build(self):
        return Grid()


UcoeApp().run()