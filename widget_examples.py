from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.gridlayout import GridLayout


Builder.load_file("widget_examples.kv")

class WidgetsExample(GridLayout):
    compteur = 1
    my_text = StringProperty("Bonjour!")
    compteur_actif = BooleanProperty(False)
    slider_value_txt = StringProperty("Valeur")
    text_input_str = StringProperty("toto") 
    
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
        
    
    def on_slider_value(self, widget):
        print(" Slider :" + str(int(widget.value)))        
        self.slider_value_txt = str(int(widget.value))


    def on_text_validate(self, widget):
        self.text_input_str = widget.text
        