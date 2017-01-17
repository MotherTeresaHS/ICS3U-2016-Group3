# Created by: Anna Devlin
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main game

from scene import *
import ui
from numpy import random


class GameScene(Scene):
    def setup(self):
        # this is called when user moves to the scene
        
        # size of screen variables are updated to not use deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        #self.score = 0
        self.game_over = False
        self.eatable_fish_rate = 3
        self.eatable_fish_attack_speed = 20.0
        self.scale_size = 0.75
        self.score = 0
        self.alien_attack_rate = 1
        self.scale_size = 0.25
        self.stroke_began = False
        self.fish = []
        self.fish_swim_speed = 20
        self.new_fish_rate = 4
        self.fishhook_enter_rate = 1
        self.game_over = False
        #self.score = 0
        
        # add background image
        background_position = Vector2(self.screen_center_x, 
                              self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/ocean_background.jpg',
                                     position = background_position, 
                                     parent = self,
                                     size = self.size + (100,100))
                                     
        #add the main character to the screen
        self.character_position = Vector2(self.screen_center_x, 75)
        self.character = SpriteNode('./assets/sprites/character.png',
                                     parent = self,
                                     position = self.size/2,
                                     size = self.size/6)
                                     
    def update(self):
        # this method is called 60 times a second to update the game
            
        # every update, randomly check if new fish should be added
        eatable_fish_create_chance = random.randint(1,120)
        if eatable_fish_create_chance <= self.new_fish_rate:
            self.add_fish()
            # call the eatable fish class
        
        # check every update if a fish is off screen
        for fish in self.fish:
            if fish.position.x > self.size_of_screen_x + 25:
                fish.remove_from_parent()
                self.fish.remove(fish)
                print("fish removed")
                print(len(self.fish))
                
        #check every update to see if the character has eaten a fish
        #if len(self.fish) > 0:
        for fish_eaten in self.fish:
            if self.fish.frame.intersects(self.character.frame):
                print("Fish was EATEN!")
                self.score += 100
                fish.remove_from_parent()
                self.fish.remove(fish_eaten)
        
        #check every update if a fish is off screen
        #for fish in self.fish:
        #    if fish.position.x > self.size_of_screen_x + 10
        #        fish.remove_from_parent()
        #        self.fish.remove(fish)

        
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
        
        if self.character.frame.contains_point(touch.location):
            self.stroke_began = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        
        # moves the character following user's finger
        if self.stroke_began == True:
            self.character.position = touch.location
            # add restrictions for sides of screen
                    
        #self.character_position = touch.location
        #self.character_position.y = touch.location.y
         #-1 * (self.character_position.x - touch.location.x)/3
    
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
        
#    def add_fish(self):
#        #add new fish to enter into screen
#        #based on alien scripting by Mr Coxall
#        
#        print("fish added")
#        
#        fish_start_position = Vector2(2, 200)
#        #fish_start_position = Vector2(-100,random.randint(100, int(self.size_of_screen_y - 100)))
#        
#        fish_end_position = Vector2(600, 15)
#        
#        #fish_end_position = Vector2(self.size_of_screen_x + 100,(random.randint(100, self.size_of_screen_y))
        
        
        #THESE NEXT FOUR LINES OF CODE ARE THE ONES GETTING ERRORS, SPECIFICALLY THE LINE FOR THE POSITION
#        self.fish.append(SpriteNode('./assets/sprites/fish.png',)
#                                    position = Vector2(3,4),
#                                    parent = self)
                                    #fish_start_position,

                                      
        # make fish move across the screen
#        fish_move_action = Action.move_to(fish_end_position.x, 
#                                         fish_end_position.y, 
#                                         self.fish_swim_speed)
                                         #TIMING_SINODIAL)
                                        
                                         
#        print(len(self.fish))
#        self.fish[int(len(self.fish)-1)].run_action(fish_move_action)
        #self.aliens[len(self.aliens)-1].run_action(alien_move_action)
        
    def add_fish(self):
        #add new fish to enter into screen
        #based on alien scripting by Mr Coxall
        
        print("fish added")
        
        fish_start_position = Vector2(-200, 0)
        fish_start_position_y = random.randint(100, int(self.size_of_screen_y - 100))
        fish_start_position.y = fish_start_position_y
        
        fish_end_position = Vector2(0, 0)
        fish_end_position_x = int(self.size_of_screen_x + 100)
        fish_end_position_y = random.randint(100, int(self.size_of_screen_y - 100))
        fish_end_position.x = fish_end_position_x
        fish_end_position.y = fish_end_position_y
        
        #fish_end_position = Vector2(self.size_of_screen_x + 100,(random.randint(100, self.size_of_screen_y))
        
        
        #THESE NEXT FOUR LINES OF CODE ARE THE ONES GETTING ERRORS, SPECIFICALLY THE LINE FOR THE POSITION
        # add a fish, just 
        self.fish.append(SpriteNode('./assets/sprites/fish.png',
                             position = fish_start_position,
                             scale = self.scale_size,
                             parent = self))

                                      
        # make fish move across the screen
        fish_move_action = Action.move_to(fish_end_position.x, 
                                         fish_end_position.y, 
                                         self.fish_swim_speed,
                                         TIMING_SINODIAL)
                                        
                                         
        print(len(self.fish))
        self.fish[int(len(self.fish)-1)].run_action(fish_move_action)
