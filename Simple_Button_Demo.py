#We import the required modules
import kivy as Pawan_App_Creator
from kivy.app import App
from kivy.uix.button import Button

#We create a class that becomes the name of the App 
class ButtonApp(App):
	def build(self):
		#We create a button here
		MyButton = Button(text = 'This button does nothing')
		return MyButton
		#We create a Label here 
		#return Dhikhava(text ='This is the worst App on the planet')
		
		
#We now execute the App by using the "run" method
if __name__ == '__main__':
	ButtonApp().run()
	print('yahan pe ho gaya') 
