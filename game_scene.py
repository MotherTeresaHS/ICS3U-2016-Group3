# Created by: Anna Devlin
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main game

from scene import *
import ui
from numpy import random

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        #updated to not use deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        #self.left_button_down = False
        #self.right_button_down = False
        #self.ship_move_speed = 20.0
        #self.missiles = []
        #self.aliens = []
        #self.score = 0
        self.game_over = False
        self.eatable_fish_rate = 3
        self.eatable_fish_attack_speed = 20.0
        self.scale_size = 0.75
        self.score = 0
        self.alien_attack_rate = 1
        self.scale_size = 0.80
        
        # add background color
        background_position = Vector2(self.screen_center_x, 
                              self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/ocean_background.jpg',
                                     position = background_position, 
                                     parent = self,
                                     size = self.size + (100,100))
                                     
        #add the main character to the screen
        self.character_position = Vector2(self.screen_center_x, 75)
        self.character = SpriteNode('./assets/sprites/fish.png',
                                     parent = self,
                                     position = self.size/2,
                                     size = self.size/10)
                                     
        #update score if an alien passes the bottom or is hit by a missile
        #self.score_text.text = 'Score: ' + str(self.score)
                                      
        # move spaceship if button do
            
        # every update, randomly check if new alien should be created
        #eatable_fish_create_chance = random.randint(1,120)
        #if eatable_fish_create_chance <= self.alien_attack_rate:
        #    pass
            # call the eatable fish class
        
        # check every update if a fish is off screen
        #for missile in self.missiles:
        #    if missile.position.y > self.size_of_screen_y - 10:
        #        missile.remove_from_parent()
        #        self.missiles.remove(missile)
        
        #check every update if an alien is off screen
        #for alien in self.aliens:
        #    if alien.position.y < + 10:
        #        alien.remove_from_parent()
        #        self.aliens.remove(alien)
        #        if self.game_over is False:
        #            self.score += -10
        
        #check every upadte is an alien has touched the spaceship
        #if len(self.aliens) > 0 and len(self.missiles) > 0:
        #    for alien in self.aliens:
        #        for missile in self.missiles:
        #            if alien.frame.intersects(missile.frame):
        #                self.score += 20
        #                missile.remove_from_parent()
        #                self.missiles.remove(missile)
        #                alien.remove_from_parent()
        #                self.aliens.remove(alien)
        #                game_over = True
        
        #check every update to see if alien touches spaceship
        #if len(self.aliens) > 0:
        #    for alien_hit in self.aliens:
        #        if alien_hit.frame.intersects(self.spaceship.frame):
        #            self.spaceship.remove_from_parent()
        #            alien_hit.remove_from_parent()
        #            self.aliens.remove(alien_hit)
        
        #when the game ends, show a back to main menu button
        #if self.game_over is True:
        #    menu_button_position = Vector2(self.center_of_screen_x, self.center_of_screen_y)
        #    self.menu_button = SpriteNode('./assets/sprites/menu_button.png',
        #                               parent = self,
        #                               position = right_button_position,
        #                               alpha = 0.5,
        #                               scale = self.scale_size)
            
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        
        # move image with your finger
        #self.school_crest.position = touch.location
        #character_move = Action.move_by(20, 0.0, 0.1)
        #self.spaceship.run_action(spaceship_move)
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

    #def add_eatable_fish(self):
        #add new eatable fish to come into the scene
