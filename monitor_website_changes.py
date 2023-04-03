# Import libraries
import time
import hashlib
from urllib.request import urlopen, Request
  
# Setting the URL that needs to be monitored
url = Request('https://stackoverflow.com/', 
              headers={'User-Agent': 'Mozilla/5.0'})
  
# Perform a GET request and load the 
# content of the website and store it in a var
response = urlopen(url).read()
  
# Create the initial hash using hash.
# The SHA-224 algorithm is one flavor of SHA-2 (Secure Hash Algorithm 2),
# a cryptographic hash function that outputs a value that is 256 bits long.
# In hashing, data of arbitrary size is mapped to data of fixed size.
# For example, a 512-bit string of data would be transformed into a 256-bit string through SHA-256 hashing. 
currentHash = hashlib.sha224(response).hexdigest()
print("website monitoring started")
time.sleep(10)
while True:
    try:
        # Perform the GET request and store it in a var
        response = urlopen(url).read()
          
        # Create a hash
        currentHash = hashlib.sha224(response).hexdigest()
          
        # Wait for 30 seconds
        time.sleep(30)
          
        # Perform the GET request
        response = urlopen(url).read()
          
        # Create a new hash
        newHash = hashlib.sha224(response).hexdigest()
  
        # Check if new hash is same as the previous hash
        if newHash == currentHash:
            continue
  
        # If something changed in the hashes
        else:
            # Notify
            print("something changed in the website")
  
            # Again read the website
            response = urlopen(url).read()
  
            # Create a hash
            currentHash = hashlib.sha224(response).hexdigest()
  
            # Wait for 30 seconds
            time.sleep(30)
            continue
              
    # To handle exceptions
    except Exception as e:
        print("error")
