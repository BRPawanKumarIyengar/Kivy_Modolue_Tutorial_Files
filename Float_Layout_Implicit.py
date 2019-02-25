from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class SimpleApp (App):
 def build(self):
  root = FloatLayout()
  label = Label(text = 'What a waste', color = (0,1,0,1), font_size = 40)
  label.pos_hint ={ 'x': 0, 'y':0}
  button = Button(text = 'Total Waste')
  button.size_hint = (0.3,0.3)
  button.pos_hint ={ 'x': 0, 'y':0}
  mutton = Button(text = 'Perfect Waste')
  mutton.size_hint = (0.3,0.3)
  mutton.pos_hint ={ 'x': 0, 'y':0.7}
  root.add_widget(button)
  root.add_widget(mutton)
  root.add_widget(label)
  return root
  
app = SimpleApp()
app.run()