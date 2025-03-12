#check if entered name is the same as stored name in the program. Capitalization will be ignored
#jaCob = Jacob = JACOB
import os
stored_name = "jacob"
#accept input from the user 
input_name = input("Enter name:") # Jacob
stored_name = stored_name.lower() # jaCob
input_name = input_name.lower() # JACOB
if input_name == stored_name: 
    print("Name matches")
else:
    print("Name does not match")
print("End of program")
    
    

