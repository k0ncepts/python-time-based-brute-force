# python-time-based-brute-force
Time based brute force attack python script

Usage:
python test.py <path to file to brute force>
  example: k0ncepts:~$ python3 /home/k0ncepts/Desktop/vault.o

  
Tests:
  printing dictionary for only 1 iteration for each character in the format {"a" : response_time} and building on that to build out the full dictionary to use for the password brute force attempts. Ran multiple times on a Lubuntu VM. 
  
  
Further:
  Not sure if the Virtual Machine affected the outcome of the server response because it never got a "Success" however, I did reverse the sample to know what the actual password was and the script got close multiple times. I am sure there's a better solution to this however it does perform a time-based brute force attack in it's current state. 
