import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
os.environ['KIVY_WINDOW'] = 'sdl2'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class BlenderScreen(Widget):
    pass


class BlenderApp(App):
    def build(self):
        return Button(text="Blend")
        return BlenderScreen()


if __name__ == '__main__':
    BlenderApp().run()