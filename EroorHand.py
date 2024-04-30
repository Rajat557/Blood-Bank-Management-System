class InvalidAgeError(Exception):
    def __init__(self,age=0):
        self.age=age

    def __str__(self):
        return f"{self.age} is invalid for donating blood"    
    
class invalidbld(Exception):
    def __init__(self,bloodgrp):
         self.bloodgrp=bloodgrp

    def __str__(self):
         return f"\n\t{self.bloodgrp} is invalid please enter valid bloodgroup." 
    
class con(Exception):
    def __init__(self,contact=0):
        self.contact=contact 
    def __str__(self):
        return f"{self.contact} is invalid please enter 10 digit num."    



