#!/usr/bin/python3
# This script creats a cloud folder for specified users.
from cterasdk import *
import getpass
import os.path

filename = os.path.basename(__file__)

print("This script creats a cloud folder for specified users.")
# Read input from keyboard and store into global variables.
#portal = input("Please enter the portal address: ")
#username = input("Please enter the global admin username: ")
#password = getpass.getpass("Please enter the password for " + username + ": ")
#domain = input("Please enter the domain: ")

# Hardcode global variables.
portal = 'todd.ctera.me'
username = 'admin'
password = 'Breakthings456'
domain = 'ctera.lab'
cloud_folder = 'H Drive'
folder_group = 'portal-CloudFolders'

if __name__ == "__main__":
    try:
        admin = GlobalAdmin(portal)
        print("Logging into " + portal)
        admin.login(username, password)
        print("Successfully logged in to " + portal)
        print("Creating domain users array.")
        users = admin.users.list_domain_users(domain)
        print("Looping through array...")
        for user in users:
            print("Username is " + user.name)
            user_account = portal_types.UserAccount(user.name,domain)
            print("User account is " + user_account.name) 
            print("Creating " + cloud_folder + ' for ' + user.name)
            admin.cloudfs.mkdir(cloud_folder, folder_group, user_account)
    except CTERAException as error:
        print(error)
    admin.logout()
    print("Logged out of " + portal)
    print('Exiting ' + filename + '.\nCheers.')
