#!/usr/bin/python3
from cterasdk import *
import getpass
import os.path

print("This script tries to fetch hardcoded domain users or groups")
portal = input("Please enter the portal address: ")
username = input("Please enter the global admin username: ")
password = getpass.getpass("Please enter the password for " + username + ": ")
domain = input("Please enter the domain: ")
input_file = 'input-users.txt'

if __name__ == "__main__":
    try:
        admin = GlobalAdmin(portal)
        print("Logging into " + portal)
        admin.login(username, password)
        print("Creating user/group objects to be fetched...") 

        print("Initializing empty arrays")
        users = []
        accounts = []
        print("Opening input file for reading")
        with open(input_file) as file:
            for user in file:
               account = portal_types.UserAccount(user.rstrip('\n'), 'ctera.lab')
               accounts.append(account)
        admin.directoryservice.fetch(accounts)

    except CTERAException as error:
        print(error)
    admin.logout()
