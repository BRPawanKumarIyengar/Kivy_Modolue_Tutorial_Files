from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line


class Chitrakari(Widget):
	def on_touch_down(self, touch):
		#print(touch)
		with self.canvas:
			touch.ud["line"] = Line(points = (touch.x, touch.y))
			
	def on_touch_move(self, touch):
		#print(touch)
		touch.ud["line"].points += (touch.x, touch.y)
		
		
class Kalakari(App):
	def build(self):
		return Chitrakari()
	
if __name__ == '__main__':
	Kalakari().run()