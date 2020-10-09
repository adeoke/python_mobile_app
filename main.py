from app import MainApp
from kivy.garden.iconfonts import register

from os.path import dirname, join

fonts_dir = join(dirname(__file__), 'app/assets/fonts/Material.Design-Iconic.ttf')
zmd_file = join(dirname(__file__), 'app/assets/fonts/zmd.fontd')

if __name__ == '__main__':
  register('MatIcons', fonts_dir, zmd_file)
  MainApp().run()
