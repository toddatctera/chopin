#!/usr/bin/python3
from cterasdk import *
import getpass
import os.path

# Hardcoded global variables.
portal = 'todd.ctera.me'
username = 'admin'
password = 'Breakthings456'
domain = 'ctera.lab'

print("This script tries to fetch hardcoded domain users or groups")
#portal = input("Please enter the portal address: ")
#username = input("Please enter the global admin username: ")
#password = getpass.getpass("Please enter the password for " + username + ": ")
#domain = input("Please enter the domain: ")
input_file = 'input-users.txt'

if __name__ == "__main__":
    try:
        admin = GlobalAdmin(portal)
        print("Logging into " + portal)
        admin.login(username, password)
        print("Creating user/group objects to be fetched...") 

        print("initalizing empty array")
        users = []
        print("Opening input file for reading")
        with open(input_file) as f:
            for line in f:
                users.append(line)
                print("appending this to users array: " + line)

    except CTERAException as error:
        print(error)
    admin.logout()
