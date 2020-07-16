#!/usr/bin/python3
# Creates a cloud folder for all users in the specified domain.
import os.path
import logging
import getpass
from cterasdk import *

portal = None
username = None
password = None
domain = None
cloud_folder = None
folder_group = None
failed_users = []
filename = os.path.basename(__file__)

# Enable and set logging level.
config.Logging.get().enable()
config.Logging.get().setLevel(logging.INFO)

logging.info('Starting script: ' + filename)

if __name__ == "__main__":
    try:
        print("This script creates a cloud folder for specified domain users.")
        # Read inputs and set variables
        portal = input('Enter the portal address: ') 
        username = input('Enter the global admin username: ') 
        password = getpass.getpass('Enter the password for ' + username + ': ')
        domain = input('Enter the domain: ') 
        cloud_folder = input("Enter a name for the new Cloud Folder: ")
        # Login
        admin = GlobalAdmin(portal)
        admin.login(username, password)
        logging.info('Successfully logged in to %s,', portal)
        # Pick a folder group to hold the new cloud folders
        print("Printing Available Folder Groups...")
        print("\t" + "Folder Group Names")
        print("\t" + "==================")
        for fg in admin.cloudfs.list_folder_groups():
            print("\t" + fg.name)
        folder_group = input("Enter a Folder Group from above to be use: ")
        logging.info('Using folder group %s', folder_group)
        # Try and create specified cloud folder for each user found
        users = admin.users.list_domain_users(domain)
        for user in users:
            user_account = portal_types.UserAccount(user.name,domain)
            try:
                admin.cloudfs.mkdir(cloud_folder, folder_group, user_account)
                logging.info('Created %s for %s.', cloud_folder, user)
            except CTERAException as error:
                logging.error(error)
                failed_users.append(user.name)
                logging.warning(
                        'Failed making %s for %s.', cloud_folder, user.name)
    except CTERAException as error:
        logging.error(error)

# Logout and exit
admin.logout()
logging.info("Logged out of " + portal)
logging.info('Exiting script: ' + filename)
