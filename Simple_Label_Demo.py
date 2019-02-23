#We import the required modules
import kivy as Pawan_App_Creator
from kivy.app import App
from kivy.uix.label import Label



#We create a class that becomes the name of the App 
class LabelApp(App):
	def build(self):
		#We create a Label here 
		return Label(text ='This is the worst App on the planet')
		
		
#We now execute the App by using the "run" method
if __name__ == '__main__':
	LabelApp().run()
	print('yahan pe ho gaya')