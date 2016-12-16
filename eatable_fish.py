# Created by: Anna Devlin
# Created on: Dec 2016
# Created for: ICS3U
# This class is used to define an eatable fish object
# Not yet connected to any scene

class Vehicle:
    # this class defines a vehicle

    # class variable shared by all instances

    def __init__(self, gear = 1, license_plate_number = '123ABC', colour = 'blue'):
        # private fields

        self.__swim_speed = 10
        self.__
        
        
        self.__speed = 0
        self.__gear = gear
        self.__license_plate_number = '123ABC'
        self.__colour = 'blue'
        self.__maximum_speed = 200
        
        #in order to set fields "legally"
        self.set_license_plate_number(license_plate_number.upper())
        self.set_colour(colour)
        
    #properties
    def get_rpm(self):
        # get the rpm property
        return self.__rpm
        
    def get_colour(self):
        # get the rpm property
        return self.__colour
        
    def set_colour(self, new_colour):
        #set the colour to one of the colours the dealership has in stock
        
        if new_colour == 'blue' or new_colour == 'red' or new_colour == 'green' or new_colour == 'yellow' or new_colour == 'black':
            self.colour = new_colour
        else:
            pass
            
    def get_speed(self):
        # get the speed property
        return self.__speed
    
    def get_gear(self):
        # get the gear property
        return self.__gear
    
    def set_gear(self, new_gear):
        # set the gear property
        
        if new_gear > 0 and new_gear < 6:
            self.__gear_speed_recalculation(new_gear)
            self.__gear = new_gear
            
    def get_license_plate_number(self):
        # get the license plate number property
        return self.__license_plate_number
        
    def set_license_plate_number(self, new_license_plate_number):
       # set the license plate number
       
       if len(str(new_license_plate_number)) <= 8 and len(str(new_license_plate_number)) > 0:
           self.__license_plate_number = str(new_license_plate_number)
       else:
           self.__license_plate_number = '123ABC'
        
    def get_maximum_speed(self):
        # get the maximum speed property
        return self.__maximum_speed
        
    def __gear_speed_recalculation(self, new_gear):
        #changes the speed as the gear is changed
        
        # old_gear is local
        old_gear = self.__gear
        new_gear = int(new_gear)
        
        if self.__rpm != 0:
            if old_gear > new_gear:
                self.__speed = self.__speed - 2 * (new_gear - old_gear)
            elif old_gear < new_gear:
                self.__speed = self.__speed + 2*(new_gear - old_gear)
        else:
            self.__speed = 0
        
    #private methods
    #def __gear_speed_recalculation(self, new_gear):
        #changes the speed as the gear is changed
        
        # old_gear is local
     #   old_gear = self.__gear
        
      #  if self.__rpm != 0:
       #     if old_gear > new_gear:
        #        self.__speed = self.__speed - 2*(int(new_gear) - int(old_gear)
         #   elif int(old_gear) < int(new_gear):
          #      self.__speed = self.__speed + 2*(int(new_gear) - int(old_gear))
        #else:
         #   self.__speed = 0
    
    # public methods
    def apply_accelerator(self, speed_increase):
        #increase the current speed by value passed in
        
        self.__speed = self.__speed + speed_increase
        if self.__speed > self.__maximum_speed:
            self.__ = self.__maximum_speed

    def apply_brakes(self, speed_decrease):
        # decrease the current speed by value passed in
        
        self.__speed = self.__speed - speed_decrease
        if self.__speed < 0:
            self.__speed = 0
            
    def current_state(self):
        # returns the current state of the bicycle as a string 
        # not necessary because of the getters and setter, but convenient to get all the information
        
        # this varaible is local to this method
        return_string = 'Rpm: ' + str(self.__rpm) + ' Speed: ' + str(self.__speed) + ' Gear: ' + str(self.__gear) + ' License Plate Number: ' + str(self.__license_plate_number) + ' Colour: ' + str(self.__colour) + ' Maximum Speed: ' + str(self.__maximum_speed)        
        return return_string

