import os
import sys
from kivy.app import App
from .view import MainWindow

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
print('**********')
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
print(sys.path)
print('*********')
# view file will contain all the gui logic

class MainApp(App):
  def build(self):
    return MainWindow()
