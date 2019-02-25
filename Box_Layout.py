#We import the required modules
import kivy as Pawan_App_Creator
from kivy.app import App as Karma
from kivy.uix.boxlayout import BoxLayout as Dabba
from kivy.lang import Builder

presentation = Builder.load_file("Pawan.kv")

#We create a class that becomes the name of the App 
class BakwasApp(Karma):
	def build(self):
		return Dabba()
	
#We now execute the App by using the "run" method
if __name__ == '__main__':
	BakwasApp().run()
	print('yahan pe ho gaya')
