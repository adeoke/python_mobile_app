from kivy.app import App
from .view import MainWindow

# view file will contain all the gui logic

class MainApp(App):
  def build(self):
    return MainWindow()
