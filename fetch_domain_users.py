#!/usr/bin/python3
from cterasdk import *
import getpass

print("This script tries to fetch hardcoded domain users or groups")
#portal = input("Please enter the portal address: ")
#username = input("Please enter the global admin username: ")
#password = getpass.getpass("Please enter the password for " + username + ": ")
#domain = input("Please enter the domain: ")

portal = 'todd.ctera.me'
username = 'admin'
password = 'Breakthings456'
domain = 'ctera.lab'

if __name__ == "__main__":
    try:
        admin = GlobalAdmin(portal)
        print("Logging into " + portal)
        admin.login(username, password)
        print("Creating user/group objects to be fetched...") 
        user = portal_types.UserAccount('todd',domain)
        group = portal_types.GroupAccount('Domain Users',domain)
        print("Fetching user accounts and groups...")
        admin.directoryservice.fetch([user])
    except CTERAException as error:
        print(error)
    admin.logout()
