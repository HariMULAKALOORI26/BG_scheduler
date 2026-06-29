#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:10:48 2026

@author: mulakal
"""


## Example A ##
# class Participant:
    
#     def __name__(self, name, timezone):
#         self.name = name
#         self.timezone = timezone
        
## Example B ##

class Participant:

    def __init__(self, name, timezone):
        self.name = name
        self.timezone = timezone

    def add(self, num1, num2):
        self.c = num1 + num2
        print("Output sum func is",self.c)
        return self.c
        
    def sub(self, num1, num2):
        self.c = num2 - num1
        print("Output sub func is",self.c)
        return self.c

    def change_timezone(self, new_timezone):
        self.timezone = new_timezone
        
        
# hari = Participant("Hari", "Europe/Paris") 
# print(type(hari)) 
# print(hari.name)
# print(hari.timezone)      


if __name__ == "__main__":
    part = Participant("Hari", "Europe/Paris") 
    print(type(part))  
    print(part.name)
    print(part.timezone)
    
    print(part.add(int(10),int(20))) # if no retrun is given then output is None
    print(part.sub(10,20)) # if no retrun is given then output is None


    
    
