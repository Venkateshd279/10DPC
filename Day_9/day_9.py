# module intall and import 
# module means they give package - we need to install and use it. 

# need to install the module - pip install requests
import requests
import time 

time.sleep(2) # it will wait for 2 seconds before executing the next line of code.

output = requests.get("https://google.com")

print(output.status_code) # it will print the status code of the response, 200 means success, 404 means not found, 500 means server error.