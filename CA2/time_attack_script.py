# -*- coding: utf-8 -*-
import time
from time_password_checker import check_password

import numpy as np

class solution():
    def __init__(self) -> None:
        # DO NOT MODIFY THE EXISTED PROPERTY
        # You can add as many properties as you need
        self.password = ""                                              # This is where your guessed password is store
    
    def example(self):
        # The following shows how to get the time spent
        # You can modify it to test your ideas
        
        # If password is correct, check_password will return Correct
        # If password is wrong, check_password will return Wrong
        
        T1 = time.perf_counter()
        result = check_password(self.password)
        T2 = time.perf_counter()
        
        # You can print the output for debug or test.
        print(result)
        print("time spend: ", T2-T1)

        # T1 = time.perf_counter()
        # result = check_password('X')
        # T2 = time.perf_counter()
        
        # return T2-T1
        
        
    
    def getPassword(self):
        # Please complete this method
        # It should be the return the correct password in a string
        # GradeScope will import your class, and call this method to get the password you calculated.
        pwd = ""
        while True: # infinite loop
            t = [] # empty array bc check password will have higher times if correct
            for i in range(33, 127): # check every chracter
                median = [] # using medians to find the better time, odd number works best
                test = pwd + chr(i) # testing by checking one stirng at a time
                for j in range(5): # used 5 for faster iterations, could use any odd number
                    T1 = time.perf_counter() # from example
                    bruh = check_password(test) #from example
                    T2 = time.perf_counter() #from example
                    median.append(T2-T1) # append to array
                    if (bruh == 'Correct'): # check to end while loop
                        return test
                t.append(np.median(median)) # append median to time 
            pwd += chr(np.argmax(t) + 33) # whichever has hihgest time is letter and add 33 to get the correct character
              
# Write Up
# Please explain your solution
# iterate throuhghe evry possible character adn check the check password function time
# if it is correct, then it will tkae more time to check it if it is correct so using this
# we can check each letter for the size of the password and it should get the correct password