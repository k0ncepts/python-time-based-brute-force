#!/usr/bin/env python

import subprocess, sys, time
#Alaphbet to test against
alphabet = (
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
)


def getChar(password):
    """
    getChar takes the the parameter password
    creates an average based on the average of 30 iterations 
    of the currentl letter being tested for server response time. 
    For instance it will test the letter "a" 30 times and get the
    server response times from each iteration adding them to a list.
    Then we get the average of that list for just the letter "a" and 
    add that to the full averages dictionary {"a" : average_response_time}
    """

    averages = {} #get average of all characters iterated through
    num_iters = 30 #arbitrary number of iterations to account for anomalies 

    #Outter loop to iterate through the letters in the alphabet 
    #stores the current test password
    #stores the duration of the server response for each letter
    for letter in alphabet:
        executable_path = sys.argv[1]
        test_password = password + letter

        durations = []  # Store durations for each iteration
        #innter loop to iterate the arbitrary number of times to account for anomalies
        for i in range(num_iters):
            #get the time in nano seconds before calling the exectuable.
            start_time = time.perf_counter_ns()
            result = subprocess.run([executable_path, test_password], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            end_time = time.perf_counter_ns() #get the end time after the executable was ran

            last_stdout = result.stdout #store the stdout aka if the executable responded with "Wrong password" or "Success"

            duration = end_time - start_time #calculate the time it took between submission and server response
            duration_ms = duration / 1000000 #I like nano seconds more for this since it's really fast. So getting nano seconds from milliseconds by taking duration and dividing by 1million

            durations.append(duration_ms)  # Append the duration to the durations list

        average_duration = sum(durations) / num_iters  # Calculate the average duration for the current letter
        averages[letter] = average_duration  # Store the average duration in the dictionary

    return averages, last_stdout #function returns the averages and the stdout to see if we are successful

#create a variable to test our while loop against
found = False

#while found is not True continue to build the password based on the function up to 14 characters long
#14 was arbitrary number
#this while loop will continue and start over after 14 characters has been reached if found is not True
#This will indefinitely run until it found the correct password
while not found:
    password = ""
    while not found and len(password) <15:
        average_results, server_response = getChar(password) #assign variables from the return variables of the function
        max_char = max(average_results, key=average_results.get) #get the key in the key value pair of average_results
        password += max_char #build the password for each iteration

        if server_response.strip() == "Success":
            found = True
        else:
            print(f"Current password attempt: {password}")

print(f"The password is: {password}")
