# Created by: Mr. Coxall
# Modified by: Anna Devlin
# Added buttons, design, and connection to other scenes
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
from help_scene import *
from about_scene import *
import ui


class MainMenuScene(Scene):
                                     
    def setup(self):
        # this method is called, when user moves to this scene
        
        # add background color
        self.background = SpriteNode('./assets/sprites/school_of_fish.gif',
                                     position = self.size / 2, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
                                     
        self.start_button = SpriteNode('./assets/sprites/start_button.png',
                                       parent = self,
                                       position = self.size / 2)
                                       
        help_button_position = self.size / 2
        help_button_position.y = help_button_position.y - 200
        self.help_button = SpriteNode('./assets/sprites/help_button.png',
                                       parent = self,
                                       position = help_button_position)
        about_button_position = self.size / 2
        about_button_position.y = about_button_position.y - 400
        self.about_button = SpriteNode('./assets/sprites/about_button.png',
                                       parent = self,
                                       position = about_button_position)
    
    def update(self):
        # this method is called 60 times per second
        pass
    
    def touch_began(self, touch):
        # this method is called when user touches screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, go to game scene
        #if self.start_button.frame.contains_point(touch.location):
        #    self.present_modal_scene(GameScene())
            
        # if start button is pressed, go to game scene
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
           
        #I will restore this once I have a button whose frame is the same size as the button itself
        #if self.about_button.frame.contains_point(touch.location):
        #    self.present_modal_scene(AboutScene())
    
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
