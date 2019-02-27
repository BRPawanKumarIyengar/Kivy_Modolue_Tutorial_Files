#We here see the mouse control options for Kivy

#We import required modules
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock

presentation = Builder.load_file("Mouse_Pointer_Options.kv")

class MyW(Widget):
	def on_touch_down(self, touch):
			self.ids.button1.text = 'Power On' 
			self.ids.button1.color = 0,1,0,1
	
class momo(App):
	def build(self):
		return MyW()

if __name__ == '__main__':
	momo().run()