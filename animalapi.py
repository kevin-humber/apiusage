"""We have a client that is our computer, and we would like to access 
information that is stored on a webserver. There are webserver online 
that give the public access to the information on its server using the RestAPI. 
The RestAPI is a set of rules that allow us to create simple requests to a server 
and get back information.
In this lab, we are going to use the website 'https://api-ninjas.com’ as our source 
for information. We are going to pull the information, process it and then store into a file.
We are going to use two python modules that make our life easier.

Requests and json
The requests module is made so that it is easy for us a make a connection to a remote server 
and makes requests from it. The response is usually sent back to us as a string.
The json module is a built-in python module, made to convert a json string into a python 
dictionary so that we can use the built-in dictionary methods. We don’t need to 
pip install json because it is built.
"""

import requests
import json

api_key = 'sC+rZaSDcGKobphXlZxeNg==k8NVPTOZa0iMTHqX'

name = 'cheetah'
url = f'https://api.api-ninjas.com/v1/animals?name={name}'

# looking at the documentation at https://requests.readthedocs.io/en/latest/, what is the request that is being sent to the API
#'requests' is an object that has methods defined in the documentation, et is on e of the methods, 
# and the most popular
# response is now an object of whatever requests.get() returns and we can do those methods to it
# much of the time, the requests.get returns a string that looks like json

response = requests.get(url, headers={'X-Api-Key': api_key})

#
#print(response)
#print(response.url)
#print(response.status_code)
#print(response.content)
#print(type(response.content))
#print(response.json)
#print(type(response.json))
#print(response.headers)
#print(type(response.headers))


# usually for this library, we always use the code as below, because any server errors raises an exception
# when we call the response object and nothings is there and our code stops, so we always do the status_code check 
# before accessing the response object 

#from above, what kind of information does response.json return?
'''
if response.status_code == requests.codes.ok:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)
'''
# if we wanted the json data to print in a way that is easily readable by us, then we would do 
# below
'''
if response.status_code == requests.codes.ok:
    data = response.json()
    #json.dumps() converts the python object into a string
    #json.loads() does the opposite, converts a string into a python object
    #response.json creates a python object
    pretty_response = json.dumps(data, indent=4)
    print(pretty_response)
else:
    print("Error:", response.status_code, response.text)
'''

###now let's play around with the data from the server, choose different animals and see what returns


### choose lion, see what returns, and pull out three pieces of information about one type of lion
# and print it to the screen

#the next bit of code shows you how to write your information into a file
'''
if response.status_code == requests.codes.ok:
    data = response.json()
    pretty_response = json.dumps(data, indent=4)
    print(pretty_response)
    #make a filename using our animal name
    filename =f'{name}.txt'
    # makes and opens a file object called file, which we can do file methods to
    with open (filename, 'w') as file:
        #write the data into the file
        file.write(pretty_response)
        print('saved to file')
        file.close()
else:
    print("Error:", response.status_code, response.text)
'''


# below I will create a function that pulls three pieces of data from the animal API response
def pull_animal_data(animal_input):
    animal_response={}
    animal_response['name']=animal_input[0]['name']
    animal_response['kingdom']=animal_input[0]['taxonomy']['kingdom']
    animal_response['location']=animal_input[0]['locations']
    animal_response['top speed']=animal_input[0]['characteristics']['top_speed']
    return animal_response

# to keep my code neat, I could opt to save my functions in another file, and import that 
# file with an import statement and access the functions

if response.status_code == requests.codes.ok:
    data = response.json()
    #pull animal data
    animal_data = pull_animal_data(data)
    pretty_response = json.dumps(animal_data, indent=4)
    filename =f'{name}_pulleddata.txt'
    # makes and opens a file object called file, which we can do file methods to
    with open (filename, 'w') as file:
        #write the data into the file
        file.write(pretty_response)
        print('saved to file')
        file.close()
else:
    print("Error:", response.status_code, response.text)

    
    
    