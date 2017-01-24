# Created by: Anna Devlin
# Created on: Dec 2016
# Created for: ICS3U
# This scene shows the main game

from scene import *
import ui
from numpy import random
import sound
import time

class GameScene(Scene):
    def setup(self):
        # this is called when user moves to the scene
        
        # used to time out instructions label
        self.start_time = time.time()
        
        # size of screen variables are updated to not use deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.game_over = False
        self.score = 0
        self.stroke_began = False
        self.fish = []
        self.fishhooks = []
        self.game_over = False
        
        # constants: used to regulate gameplay
        self.scale_size = 0.2
        self.fish_swim_speed = 20
        self.character_swim_speed = 0.8
        self.new_fish_rate = 3
        self.new_fishhook_rate = 1
        self.fishhook_speed = 38
        self.fishhook_end_position_y = 400
        
        # add background image
        background_position = Vector2(self.screen_center_x, 
                              self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/ocean_background.jpg',
                                     position = background_position, 
                                     parent = self,
                                     size = self.size + (100,100))
                                     
        #add the main character to the screen
        self.character_position = Vector2(self.screen_center_x, 75)
        self.character = SpriteNode('./assets/sprites/character_facing_right.png',
                                     parent = self,
                                     position = self.size/2,
                                     size = self.size/6)
                                     
        #add the score label
        score_label_position = Vector2()
        score_label_position.x = 100
        score_label_position.y = self.size_of_screen_y - 50
        self.score_label = LabelNode(text = 'Score: ',
                                      font=('Futura', 40),
                                      parent = self,
                                      position = score_label_position,
                                      scale = 0.75)
        # added so score is always rendered last
        self.score_label.z_position = 999
        
        # to add the instruction
        self.instruction = LabelNode(text = 'TAP AND DRAG TO MOVE',
                                      font = ('Futura', 20),
                                      color = 'white',
                                      parent = self,
                                      position = Vector2(self.screen_center_x, self.screen_center_y))
        
    def update(self):
        # this method is called 60 times a second to update the game
        
        #to make the instruction label disappear after a couple seconds
        if not self.presented_scene and time.time() - self.start_time > 3:
            self.instruction.text = ''
            
        # CODE FOR LITTLE FISH:
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
                #print("fish removed")
                #print(len(self.fish))
        
       #check every update to see if the character has eaten a fish
        if len(self.fish) > 0:
            for fish_eaten in self.fish:
                # mr.c I changed the line below to character
                if fish_eaten.frame.intersects(self.character.frame):
                    if self.game_over == False:
                        #print("Fish was EATEN!")
                        self.score += 100
                        #mr.c fixed the line below as well
                        fish_eaten.remove_from_parent()
                        self.fish.remove(fish_eaten)
                    
        # CODE FOR FISHHOOKS:    
        # every update, randomly check if new fishhook should be added
        fishhook_create_chance = random.randint(1,240)
        if fishhook_create_chance <= self.new_fishhook_rate:
            self.add_fishhook()
            # calls the add fishhook function
            
        #check every update to see if the character has been caught by a fishhook
        if len(self.fishhooks) > 0:
            for fishhook in self.fishhooks:
                if fishhook.frame.intersects(self.character.frame):
                    #print("Character was caught. GAME OVER!")
                    self.game_over = True
                    self.character.position.y = 30000000
                    fishhook.remove_from_parent()
                    self.fishhooks.remove(fishhook)
                    self.character.remove_from_parent()
            
        #check every update if the fishhooks should be removed from the parent
        if len(self.fishhooks) > 0:
            for fishhook in self.fishhooks:
                if fishhook.position.y == self.fishhook_end_position_y:
                    fishhook.remove_from_parent()
                    self.fishhooks.remove(fishhook)
                    
        # WHEN THE GAME ENDS:
        # when the game ends, show a back to main menu button
        if self.game_over == True:
            menu_button_position = Vector2(self.screen_center_x, self.screen_center_y)
            self.menu_button = SpriteNode('./assets/sprites/main_menu_button.png',
                                       parent = self,
                                       position = menu_button_position,
                                       alpha = 0.5)
            
        #Update score label
        self.score_label.text= 'Score: ' + str(self.score)
        
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        if self.character.frame.contains_point(touch.location):
            self.stroke_began = True
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        
        # moves the character following user's finger
        
        character_aiming_point = Vector2(0,0)
        character_aiming_point.x = touch.location.x
        character_aiming_point.y = touch.location.y
        
        character_move_action = Action.move_to(character_aiming_point.x, 
                                 character_aiming_point.y, 
                                 self.character_swim_speed)
                                 
        if self.stroke_began == True:
            if touch.location.x < self.size_of_screen_x - 25 and touch.location.x > 25:
                if touch.location.y < self.size_of_screen_y - 25 and touch.location.y > 25:
                    self.character.run_action(character_move_action)
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        self.stroke_began = False
        
        # when the game ends and the main menu button
        if self.game_over == True:
            if self.menu_button.frame.contains_point(touch.location):
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
        
    def add_fish(self):
        #add new fish to enter into screen
        #based on alien scripting by Mr Coxall
        
        #print("fish added")
        
        fish_start_position = Vector2(-200, 0)
        fish_start_position_y = random.randint(100, int(self.size_of_screen_y - 100))
        fish_start_position.y = fish_start_position_y
        
        fish_end_position = Vector2(0, 0)
        fish_end_position_x = int(self.size_of_screen_x + 100)
        fish_end_position_y = random.randint(100, int(self.size_of_screen_y - 100))
        fish_end_position.x = fish_end_position_x
        fish_end_position.y = fish_end_position_y
       
        # add a fish, just 
        self.fish.append(SpriteNode('./assets/sprites/fish_' + str(random.randint(1,4)) + '.png',
                             position = fish_start_position,
                             scale = self.scale_size,
                             parent = self))

                                      
        # make fish move across the screen
        fish_move_action = Action.move_to(fish_end_position.x, 
                                         fish_end_position.y, 
                                         self.fish_swim_speed,
                                         TIMING_SINODIAL)
                                        
        #print(len(self.fish))
        self.fish[int(len(self.fish)-1)].run_action(fish_move_action)
        
    def add_fishhook(self):
        #add new fish hook to enter into screen
        #based on alien scripting by Mr Coxall
        
        #print("fishhook added")
        
        fishhook_start_position = Vector2(0, int(self.size_of_screen_y + 900))
        random.randint(100, int(self.size_of_screen_y - 100))
        fishhook_start_position_x = random.randint(20, int(self.size_of_screen_x)-20)
        fishhook_start_position.x = fishhook_start_position_x
       
        # add a fish hook 
        self.fishhooks.append(SpriteNode('./assets/sprites/fishhook.png',
                             position = fishhook_start_position,
                             parent = self))
                             
        # make fishhook go down move across the screen
        fishhook_downward_action = Action.move_to(fishhook_start_position_x,
                                         self.fishhook_end_position_y, 
                                         self.fishhook_speed)
        # run the action if there are fishhooks
        if int(len(self.fishhooks)) > 0:
            self.fishhooks[int(len(self.fishhooks)-1)].run_action(fishhook_downward_action)
