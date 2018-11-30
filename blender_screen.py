import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
os.environ['KIVY_WINDOW'] = 'sdl2'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from gpiozero import LED
from time import sleep

class CustomWidget(BoxLayout):
     def __init__(self, **kwargs):
        super(CustomWidget, self).__init__(**kwargs)
        btn = Button(text = "Click")
        btn.bind(on_press=self.clk)
        
        self.add_widget(btn)
     def clk(self, obj):
        print("hello bitches")

class BlenderApp(App):
     def build(self):
        return CustomWidget()
        
if __name__ == '__main__':
    BlenderApp().run()