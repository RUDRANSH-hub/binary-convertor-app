
import kivy
from kivy import Config

Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton, MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar
from kivy.uix import  gridlayout
from kivy.core.window import Window
class ConverterApp(MDApp):
    

    def flip(self):
        # a function for the "flip" icon
        # changes the state of the app
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.text = ''

        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.text = ''
        # hide labels until needed
        self.converted.text = ""
        self.label.text = ""
    
  
    def convert(self, args):
        
        # a function to find the decimal/binary equivallent
        
        if self.state == 0:
            
            if ("0" and "1") in list(self.input.text) :
    


            # binary to decimal
                val = str(int(self.input.text,2))
                self.label.text = "in decimal is:"
                self.converted.text = val

            else:

                self.label.text="'Input error' \n  'enter only binary no.' "
        else :

            if "." in list(self.input.text):

                self.labeltext="enter perfect integer no. only"


            # decimal to binary
            else:

                val = bin(int(self.input.text))[2:]
                self.label.text = "in binary is:"
                self.converted.text = val
            
    def build(self):
        self.state = 0 #initial state
        self.theme_cls.primary_palette = "DeepOrange"

        
        screen = MDScreen()

        # top toolbar
        self.toolbar = MDToolbar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        # logo
        screen.add_widget(Image(
            source="logo.png",
            pos_hint = {"center_x": 0.5, "center_y":0.7}
            ))

        #collect user input
        self.input = MDTextField(
            
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            font_size = 22
        )
        screen.add_widget(self.input)

        #secondary + primary labels
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.35},
            theme_text_color = "Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # "CONVERT" button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y":0.15},
            on_press = self.convert
        ))
        #self.error=MDLabel(
            #font_size=22,
            #pos_hint = {"center_x": 0.5, "center_y":0.7},)

            




        
        #screen.add_widget(self.error)

        return screen

if __name__ == '__main__':
    ConverterApp().run()
