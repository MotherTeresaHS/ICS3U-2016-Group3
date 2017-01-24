# Created by: Anna Devlin
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the help scene.

from scene import *
import ui

from main_menu_scene import *


class HelpScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # modified to replace deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        self.scale_size = 0.3
        self.shrink_size = 0.25
        
        # add background color
        background_position = Vector2(self.screen_center_x, 
                              self.screen_center_y)
        self.background = SpriteNode(position = background_position, 
                                     color = 'white', 
                                     parent = self, 
                                     size = self.size)
                                     
        instructions_1_position = Vector2(int(200), 
                              self.screen_center_y)
        self.instructions_1 = SpriteNode('./assets/sprites/instructions_1.png',
                                    position = instructions_1_position, 
                                     parent = self, 
                                     scale = self.scale_size)
                                     
        instructions_2_position = Vector2(self.screen_center_x, 
                              self.screen_center_y)
        self.instructions_2 = SpriteNode('./assets/sprites/instructions_2.png',
                                    position = instructions_2_position, 
                                     parent = self, 
                                     scale = self.scale_size + 0.2)
                                     
        instructions_3_position = Vector2(int(self.size_of_screen_x-200), 
                              self.screen_center_y)
        self.instructions_3 = SpriteNode('./assets/sprites/instructions_3.png',
                                    position = instructions_3_position, 
                                     parent = self, 
                                     scale = self.scale_size)
                                     
        back_button_position = Vector2(100, 
                              self.size_of_screen_y - 100)
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position,
                                       scale = 0.75)
                                       
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        #to make the back buttons react to being touched
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = self.shrink_size
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        
        #to make the back buttons revert to original size if the user's finger is moved from it
        if not self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = self.scale_size
            
        #to make the back buttons revert to original size if the user's finger is moved on top of it
        if self.back_button.frame.contains_point(touch.location):
            self.back_button.scale = self.shrink_size
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
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
