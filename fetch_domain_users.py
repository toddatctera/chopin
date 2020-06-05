#!/usr/bin/python3
from cterasdk import *
import getpass

print("This script fetches the hardcoded domain users group")
portal = input("Please enter the portal address: ")
username = input("Please enter the global admin username: ")
password = getpass.getpass("Please enter the password for " + username + ": ")
domain = input("Please enter the domain: ")

if __name__ == "__main__":
    try:
        admin = GlobalAdmin(portal)
        print("Logging into " + portal)
        admin.login(username, password)
        print("Creating user/group objects to be fetched...") 
        group = portal_types.GroupAccount('Domain Users',domain)
        print("Fetching user accounts and groups...")
        admin.directoryservice.fetch([group])
    except CTERAException as error:
        print(error)
    admin.logout()
