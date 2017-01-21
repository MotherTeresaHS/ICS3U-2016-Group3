# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows a splash screen for 2 seconds,
#   then transitions to the main menu.

from scene import *
import ui
import time

from main_menu_scene import *


class SplashScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # create timer, so that after 2 seconds move to next scene
        self.start_time = time.time()
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        # add MT blue background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = (0.61, 0.78, 0.87), 
                                     parent = self, 
                                     size = self.size)
        #self.school_crest = SpriteNode('./assets/sprites/MT_Crest.jpg',
        #                               parent = self,
        #                              position = Vector2(self.screen_center_x, self.screen_center_y))
                                       
        #time.sleep(1)
        #see about this after
        self.logo = LabelNode(text = '{devlin}',
                                      font = ('Didot', 45),
                                      color = 'white',
                                      parent = self,
                                      position = Vector2(self.screen_center_x, self.screen_center_y))
                                      
        #logo_word = '{devlin}'
        #for index in range (0, len(logo_word)):
        #    self.logo(text.append(str(logo_word[index])),
        #    time.sleep(.1)
                                      
        #self.logo.word = '{'
        #time.sleep(.2)
        #self.logo.word = '{d'
        #time.sleep(.2)
        
        #for letter in '{devlin}':
        #    typed_word += '{devlin}'(letter)
        #    self.logo.text = typed_word
        #    time.sleep(.2)
            
            #self.logo.text = typed_word 
            #                          
     #                                 for letter in str:
    #sys.stdout.write(letter)
    #time.sleep(.1)
                                      
        #self.logo_text = LabelNode(text = 'Design by: Anna Devlin',
        #                              font = ('Times New Roman', 20),
        #                              parent = self,
        #                              position = self.size / 2)
        #                              
    
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # have text wait to appear, then grow to appear
        #if not self.presented_scene and time.time() - self.start_time #> 0.3:
        #    self.text = LabelNode(text = '{devlin}',
        #                              font = ('Times New Roman', 1),
        #                              color = 'white',
        #                              parent = self,
        #                              position = Vector2(self.screen_center_x, self.screen_center_y - 300))
            # to increase the size of the text gradually
            # for index in range (0,20):
            #    self.text.font = (('Times New Roman', int(index())))
            
        
        # after 2 seconds, move to main menu scene
        if not self.presented_scene and time.time() - self.start_time > 2:
            self.present_modal_scene(MainMenuScene())
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
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
    
