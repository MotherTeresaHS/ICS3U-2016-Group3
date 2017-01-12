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
        self.stroke_began = False
        self.fish = []
        self.fish_swim_speed = 20
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
                                     size = self.size/3)
                                     
    def update(self):
                                     
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
        pass
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        if self.character.frame.contains_point(touch.location):
            self.stroke_began = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        
        # moves the character following user's finger
        if self.stroke_began == True:
            self.character.position = touch.location
#            if (self.character.position.x) < self.size_of_screen_x-50:
#                if (self.character.position.x) > 50:
#                    if (self.character.position.y) < self.size_of_screen_y-50:
#                        if (self.character.position.y) > 50:
#                            self.character.position = touch.location
#                        else:
#                            self.character.position.y += 10
#                    else:
#                        self.character.position.y += -10
#                else:
#                    self.character.position.x += 10
#            else:
#                self.character.position.x += -10
                    
        
        # move image with your finger
        #self.school_crest.position = touch.location
        #character_move = Action.move_by(20, 0.0, 0.1)
        #self.spaceship.run_action(spaceship_move)
        
        #if int(touch.location.x) - int(self.character_position.x) < 0:
        #    fish_move = Action.move_to(touch_location, 2)
            
        #FIGURE OUT HOW OT BE THE THINGS OF THE VEST FJDDFh
        #fish_move_action = Action.move_to(missiles_end_position.x,
        #                                    missiles_end_position.y+0,
        #                                    5.0)
            
           
        
        #self.character_position = touch.location
        #self.character_position.y = touch.location.y
         #-1 * (self.character_position.x - touch.location.x)/3
        

        
        #if self.left_button_down == True:
        #    if self.spaceship_position.x < 150:
        #        self.spaceship_position.x = self.size_of_screen_x
        #    elif self.spaceship_position.x > self.size_of_screen_x:
        #        self.spaceship_position.x = 150
        #    else:
        #        spaceship_move = Action.move_by(-1*self.ship_move_speed, 0.0, 0.1)
        #    
        #    self.spaceship.run_action(spaceship_move)
        # 
        #if self.right_button_down == True:
        #    spaceship_move= Action.move_by(self.ship_move_speed, 0.0, 0.1)
        #    
        #    self.spaceship.run_action(spaceship_move
        #pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        self.stroke_began = False
            
    
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
        
    def add_fish(self):
        #add new fish to enter into screen
        #based on alien scripting by Mr Coxall
        
        fish_start_position = Vector2(-100,random.randint(100, int(self.size_of_screen_y - 100)))
        
        fish_end_position = Vector2(self.size_of_screen_x + 100,(random.randint(100, self.size_of_screen_y))
        
        self.fish.append(SpriteNode('./assets/sprites/fish.png',
                                    position = fish_start_position,
                                    parent = self))
                                      
        fishMoveAction = Action.move_to(fish_end_position.x, 
                                         fish_end_position.y, 
                                         self.fish_swim_speed,
                                         TIMING_SINODIAL)
                                         
        self.fish[len(self.fish)-1].run_action(fishMoveAction)
