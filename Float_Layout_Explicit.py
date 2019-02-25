import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class toto(App):
	def build(self):
		return FloatLayout()


if __name__ == "__main__":
	toto().run()