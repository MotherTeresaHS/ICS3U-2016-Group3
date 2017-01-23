# Created by: Mr. Coxall
# Modified by: Anna Devlin
# Added buttons, design, and connection to other scenes
# Created on: Sep 2016
# Modified on: Dec - Jan 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *
from help_scene import *
from about_scene import *
from game_scene import *
import ui


class MainMenuScene(Scene):
                                     
    def setup(self):
        # this method is called, when user moves to this scene
        
        # to reference objects off of
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.scale_size = 0.27
        self.shrink_size = 0.25
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = '#2de4ff', 
                                     parent = self, 
                                     size = self.size)
                                     
        title_graphic_position = self.size / 2
        title_graphic_position.y = title_graphic_position.y + 100
        self.title_graphic = SpriteNode('./assets/sprites/title_graphic.png',
                                       parent = self,
                                       position = title_graphic_position,
                                       scale = 0.5)
                                       
        start_button_position = Vector2(self.screen_center_x, self.screen_center_y)
        start_button_position.y = start_button_position.y - 70
        self.start_button = SpriteNode('./assets/sprites/start_button.png',
                                       parent = self,
                                       position = start_button_position,
                                       scale = self.scale_size)
                                       
        help_button_position = self.size / 2
        help_button_position.y = help_button_position.y - 190
        self.help_button = SpriteNode('./assets/sprites/help_button.png',
                                       parent = self,
                                       position = help_button_position,
                                       scale = self.scale_size)
        
        about_button_position = self.size / 2
        about_button_position.y = about_button_position.y - 300
        self.about_button = SpriteNode('./assets/sprites/about_button.png',
                                       parent = self,
                                       position = about_button_position,
                                       scale = self.scale_size)
    
    def update(self):
        # this method is called 60 times per second
        pass
    
    def touch_began(self, touch):
        # this method is called when user touches screen
        
        #to make the buttons react to being touched
        if self.help_button.frame.contains_point(touch.location):
            self.help_button.scale = self.shrink_size
            sound.play_effect('./assets/sprites/Ding_3.caf') # this sound clip is from the Pythonista libraries
            
        if self.about_button.frame.contains_point(touch.location):
            self.about_button.scale = self.shrink_size
            sound.play_effect('./assets/sprites/Ding_3.caf') # this sound clip is from the Pythonista libraries
            
        if self.start_button.frame.contains_point(touch.location):
            self.start_button.scale = self.shrink_size
            sound.play_effect('./assets/sprites/Ding_3.caf') # this sound clip is from the Pythonista libraries
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        
        #to make the buttons revert to their original size when the user moves their finger
        
        if not self.start_button.frame.contains_point(touch.location):
            self.start_button.scale = self.scale_size
            
        if not self.help_button.frame.contains_point(touch.location):
            self.help_button.scale = self.scale_size
            
        if not self.about_button.frame.contains_point(touch.location):
            self.about_button.scale = self.scale_size
            
        #to make the buttons shrink to their original size when the user moves their finger on top of them
        if self.start_button.frame.contains_point(touch.location):
            self.start_button.scale = self.shrink_size
            
        if self.help_button.frame.contains_point(touch.location):
            self.help_button.scale = self.shrink_size
            
        if self.about_button.frame.contains_point(touch.location):
            self.about_button.scale = self.shrink_size
            
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, go to game scene
        if self.start_button.frame.contains_point(touch.location):
            self.present_modal_scene(GameScene())
            
        # if start button is pressed, go to game scene
        if self.help_button.frame.contains_point(touch.location):
            self.present_modal_scene(HelpScene())
            
        if self.about_button.frame.contains_point(touch.location):
            self.present_modal_scene(AboutScene())
    
    
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
    
