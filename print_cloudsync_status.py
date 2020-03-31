#!/usr/bin/python3
from cterasdk import *
import getpass
import os.path

filename = os.path.basename(__file__)

print("This script logs into the portal and then prints the cloudsync status from each filer")
# Read input from keyboard and store into global variables.
portal = input("Please enter the portal address: ")
username = input("Please enter the global admin username: ")
password = getpass.getpass("Please enter the password for " + username + ": ")
domain = input("Please enter the domain: ")

if __name__ == "__main__":
    try:
        admin = GlobalAdmin(portal)
        print("Logging into " + portal)
        admin.login(username, password)
        print("Successfully logged in to " + portal)
        for filer in admin.devices.filers():
            filer.show('/proc/cloudsync')
    except CTERAException as error:
        print(error)
    admin.logout()
    print("Logged out of " + portal)
    print('Exiting ' + filename + '.\nCheers.')
