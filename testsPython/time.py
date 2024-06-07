from datetime import time, timedelta  
     
# Specifying a time duration
A = timedelta(hours = 2, minutes = 30)
 
# Calling the total_seconds() function
# over the specified time duration
my_time = A.total_seconds() // 3600
 
# Getting the Total seconds for
# the duration of 55 minutes
print("Time :", my_time)