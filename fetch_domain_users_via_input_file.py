#!/usr/bin/python3
from cterasdk import *
import logging
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
        accounts = []
        with open(input_file) as users:
            for user in users:
                try:
                    account = portal_types.UserAccount(user.rstrip('\n'), domain)
                    accounts.append(account)
                except CTERAException as error:
                    print(error)
        try:
            admin.directoryservice.fetch(accounts)
        except CTERAException as error:
            print(error)
    except CTERAException as error:
        print(error)
    admin.logout()
