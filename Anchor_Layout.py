# Sample Python application demonstrating the working of AnchorLayout in Kivy

#We import the required modules
import kivy as Pawan_App_Creator
# Sample Python application demonstrating the working of AnchorLayout in Kivy

# Module imports
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

# A Kivy app demonstrating the working of anchor layout
class AnchorLayoutDemo(App):

    def build(self):
	    # Create a box layout
        boxLayout = BoxLayout()

        # Anchor Layout1
        anchorLayout1 = AnchorLayout(anchor_x='left', anchor_y='bottom')
        button1 = Button(text='Bottom-Left', size_hint = (0.6, 0.3))
        anchorLayout1.add_widget(button1)
		
        # Anchor Layout2
        anchorLayout2 = AnchorLayout()
        anchorLayout2.anchor_x = 'right'
        anchorLayout2.anchor_y = 'top'

        # Anchor Layout3
        anchorLayout3 = AnchorLayout()
        anchorLayout3.anchor_x = 'left'
        anchorLayout3.anchor_y = 'top'		
		
        # Add the anchor layouts to a box layout    
        button2 = Button(text='Top-Right', size_hint = (0.6, 0.3))
        anchorLayout2.add_widget(button2)     

        # Add the anchor layouts to a box layout    
        button3 = Button(text='Top-Left', size_hint = (0.6, 0.3))
        anchorLayout3.add_widget(button3)  		

        # Add both the anchor layouts to the box layout
        boxLayout.add_widget(anchorLayout1)
        boxLayout.add_widget(anchorLayout2)
        boxLayout.add_widget(anchorLayout3)
		
        # Return the boxlayout widget
        return boxLayout

# Run the Kivy app
if __name__ == '__main__':
    AnchorLayoutDemo().run()
