from tkinter import Grid
from xmlrpc.client import Boolean
from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainWidget(Widget): 
    pass


class WidgetsExample(GridLayout):
    compteur = 1
    my_text = StringProperty("Bonjour!")
    compteur_actif = BooleanProperty(False)
    
    def on_button_click(self):
        if self.compteur_actif: 
                self.compteur += 1
                self.my_text = str(self.compteur)
    
    
    def on_toggle_button_state(self, widget):
        print('toggle state : '+ widget.state ) 
        if widget.state == "normal": 
            print("OFF")
            widget.text = "OFF"
            self.compteur_actif = False
        else: 
            print("ON")
            widget.text = "ON"
            self.compteur_actif = True
            
    def on_switch_active(self,widget):
        print("Switch : " + str(widget.active))
        


         
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0,100): 
            b =  Button(text=str(i+1), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)
            

class GridLayoutExample(GridLayout):
    pass
         
class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs) 
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
                  
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)


class LeLabApp(App):
    pass


LeLabApp().run()