# file terkait adalah MyCalaculator

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy
 
Window.size = (640, 700)

kivy.require('1.0.1')

class MyRoot(BoxLayout):
    
    def __init__(self):
        super(MyRoot, self).__init__()
        
    def calc_symbol(self, symbol):
        self.calc_field.text += symbol
        
    def clear(self):
        self.calc_field.text = ""
        
    def get_result(self):
        self.calc_field.text = str(eval(self.calc_field.text))

class MyCalculator(App):
    
    def build(self):
        return MyRoot()

mycalc = MyCalculator()
mycalc.run()