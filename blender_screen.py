import os
os.environ['KIVY_GL_BACKEND'] = 'gl'
os.environ['KIVY_WINDOW'] = 'sdl2'
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
from gpiozero import LED
from time import sleep

# Define Variables
speed1 = LED(13)
speed2 = LED(19)
speed3 = LED(26)
speed4 = LED(12)
pump1 = LED(16)
pump2 = LED(21)

class ScreenLayout(FloatLayout):
    def __init__(self, **kwargs):
        self.blend_speed = 1
        self.blend_flag = False
        self.dispense_flag = False
        self.clean_flag = False
        self.confirm_clean_flag = False
        super(ScreenLayout, self).__init__(**kwargs)
        blend_power_slider = Slider(orientation='vertical',min=1,max=4,value=1,size_hint_y=0.8,pos_hint={'x':0.75,'y':0.1})
        self.btn1 = Button(text = "Blend", size_hint = (0.2, 0.2), pos_hint = {'x': .75, 'y': .75})
        self.btn2 = Button(text = "Dispense", size_hint = (0.2, 0.2), pos_hint = {'x': .75, 'y': .55})
        self.btn3 = Button(text = "Clean", size_hint = (0.2, 0.2), pos_hint = {'x': .75, 'y': .35})
        self.btn4 = Button(text = "Speed 1", size_hint = (0.2, 0.2), pos_hint = {'x': .75, 'y': .15})
        self.btn1.bind(on_press=self.clk1)
        self.btn2.bind(on_press=self.clk2)
        self.btn3.bind(on_press=self.clk3)
        self.btn4.bind(on_press=self.clk4)
        
        
        
        with self.canvas.before:
            Rectangle(size=(800,600),pos=self.pos,source='Black_Wallpaper.jpg')
            
        
        
        
        
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.add_widget(self.btn4)
        
    def clk1(self, obj):
        if (self.blend_flag == False):
            if (self.blend_speed == 1):
                #speed1.on()
                pass
            elif (self.blend_speed == 2):
                #speed2.on()
                pass
            elif (self.blend_speed == 3):
                #speed3.on()
                pass
            elif (self.blend_speed == 4):
                #speed4.on()
                pass
            self.blend_flag = True
            self.btn1.text = "Stop Blending"
            self.btn1.background_color = (1.0, 0, 0, 1.0)
        else:
            speed1.off()
            speed2.off()
            speed3.off()
            speed4.off()
            self.btn1.text = "Blend"
            self.btn1.background_color = (0.95, 0.95, 0.95, 1.0)
            self.blend_flag = False
        
    def clk2(self, obj):
        if (self.dispense_flag == False):
            self.dispense_flag = True
            self.btn2.text = "Stop Dispensing"
            self.btn2.background_color = (1.0, 0, 0, 1.0)
        else:
            self.btn2.text = "Dispense"
            self.btn2.background_color = (0.95, 0.95, 0.95, 1.0)
            self.dispense_flag = False
            
    def clk3(self, obj):
        if (self.clean_flag == False):
            self.btn3.text = "Confirm Cleaning"
            self.btn3.background_color = (1.0, 1.0, 0, 1.0)
            self.clean_flag = True
        elif (self.clean_flag == True) and (self.confirm_clean_flag == False):
            self.confirm_clean_flag = True
            pump1.on()      # Add water to karaffe
            sleep(7.5)
            pump1.off()
            sleep(2)
            speed1.on()     # Mix water around for 10 seconds
            sleep(10)
            speed1.off()
            self.btn3.text = "Dispense Waste"
            self.btn3.background_color = (1.0, 0, 0, 1.0)
        elif (self.clean_flag == True) and (self.confirm_clean_flag == True):
            pump2.on()      # Dispense water 
            sleep(8)
            pump2.off()
            self.btn3.text = "Clean"
            self.btn3.background_color = (0.95, 0.95, 0.95, 1.0)
            self.clean_flag = False
            self.confirm_clean_flag = False
        
    def clk4(self, obj):
        if (self.blend_speed < 4):
            self.blend_speed = self.blend_speed+1
        else:
            self.blend_speed = 1
        self.btn4.text = 'Speed ' + str(self.blend_speed)
            

class BlenderApp(App):
     def build(self):
        return ScreenLayout()
        
if __name__ == '__main__':
    BlenderApp().run()