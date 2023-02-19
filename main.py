from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.garden.iconfonts import *
from os.path import join,dirname
from hoverable import HoverBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.graphics import Rectangle,Color
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ReferenceListProperty,ObjectProperty,ListProperty
from kivy.vector import Vector
from kivy.clock import Clock 
from kivy.core.window import Window
import random
from pathlib import Path
import glob
import os
Builder.load_file("design.kv")

class Search_page(Screen):
    velocity = ListProperty([5, 5])     
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        
        
        Clock.schedule_interval(self.update, 1 / 60.)
        ball=ObjectProperty(None)
        
  
    def update(self, *args): 
        
        self.ball.pos=Vector(*self.velocity) +self.ball.pos
       
       
  
        if self.ball.pos[0] < 0 or self.ball.pos[0] > Window.width-160: 
            
            self.velocity[0] *= -1
        if self.ball.pos[1] < 0 or self.ball.pos[1]  > Window.height-150: 
            self.velocity[1] *= -1
    def joke(self,instance):
        s2 = self.manager.get_screen('jokes')
        s2.joke2(self.ids.degree.text)
 


class Laughing_image(Screen):
    def back(self):
        self.manager.current="search"
    
    
    def joke2(self,course):
        self.course=course
        path_course="degrees_1/"+course
       
        #course_jokes=glob.glob('path_course/*')#have paths of all jokes
        course_jokes=os.listdir(path=path_course)
     
        joke=random.choice(course_jokes)
        way=path_course+'/'+joke
       
        self.ids.point.source=way
        self.manager.current="jokes"

    def joke3(self):
        
        path_course="degrees_1/"+self.course
        
        #course_jokes=glob.glob('path_course/*')#have paths of all jokes
        course_jokes=os.listdir(path=path_course)
        
        joke=random.choice(course_jokes)
        way=path_course+'/'+joke
        #'Accounting & Finance','Agriculture','Anatomy & Physiology','Anthropology','Archaeology','Architecture','Art & Design','Biological Science','Business Studies','Classics & Ancient History','Communication & Media Studies','Computer science','Creative Writing','Dentistry','Drama','Economics','Education','Engineering','English','Geology','Geography','History','Hospitality','Law','Marketing','Mathematics','Medicine','Music','Pharmacy','Philosophy','Politics','Psychology',
        self.ids.point.source=way
        
class RootWidget(ScreenManager):
    pass

class ImageButton(ButtonBehavior,HoverBehavior,Image):
    pass

class emoji(Widget):
    pass
    

class MainApp(App):
    def build(self):
        
        return RootWidget()

if __name__=="__main__":
    register('default_font','assests/fonts/Material-Design-Iconic-Font.ttf',join(dirname(__file__),'assests/fonts/zmd.fontd'))
    MainApp().run()

    
