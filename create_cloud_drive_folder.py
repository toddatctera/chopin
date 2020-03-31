#!/usr/bin/python3
# This script creats a cloud folder for specified users.
from cterasdk import *
import getpass
import os.path

filename = os.path.basename(__file__)
portal = None
username = None
password = None
domain = None
cloud_folder = None
folder_group = 'portal-CloudFolders'

print("This script creats a cloud folder for specified users.")

if __name__ == "__main__":
    try:
        portal = input("Please enter the portal address: ")
        username = input("Please enter the global admin username: ")
        admin = GlobalAdmin(portal)
        password = getpass.getpass("Please enter the password for " + username + ": ")
        print("Logging into " + portal)
        admin.login(username, password)
        print("Successfully logged in to " + portal)
        domain = input("Please enter the domain: ")
        cloud_folder = input("Please enter a name for the new Cloud Folder: ") or 'Stuff'
        folder_group = input("Please enter an existing Folder Group name: ") or 'portal-CloudFolders'
        users = admin.users.list_domain_users(domain)
        print("Creating domain users array.")
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
