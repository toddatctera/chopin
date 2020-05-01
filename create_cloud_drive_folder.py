#!/usr/bin/python3
# This script creats a cloud folder for specified users.
from cterasdk import *
import getpass
import os.path
import time
import logging

filename = os.path.basename(__file__)
portal = None
username = None
password = None
domain = None
cloud_folder = None
folder_group = 'portal-CloudFolders'
timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
file_failed_users = 'failed-users-' + timestr + '.txt'
#file_failed_users = 'failed-users.txt'
config.Logging.get().enable()
config.Logging.get().setLevel(logging.INFO)

logging.info('Starting script: ' + filename)

if __name__ == "__main__":
    try:
        print("This script creats a new cloud folder for all valid domain users.")
        portal = input("Please enter the portal address: ") 
        username = input("Please enter the global admin username: ") 
        admin = GlobalAdmin(portal)
        password = getpass.getpass("Please enter the password for " + username + ": ") 
        logging.info('Logging into ' + portal)
        admin.login(username, password)
        logging.info('Successfully logged in to ' + portal)
        domain = input('Please enter the domain: ') 
        cloud_folder = input("Please enter a name for the new Cloud Folder (Default='My Files'): ") or 'My Files'
        print("Printing Possible Folder Group Names to hold the new Cloud Folder...")
        print("\t" + "Folder Group Names")
        print("\t" + "==================")
        for fg in admin.cloudfs.list_folder_groups():
            print("\t" + fg.name)
        folder_group = input("Please enter one of the Folder Groups printed above to use (Default='portal-CloudFolders'):\n>") or 'portal-CloudFolders'
        users = admin.users.list_domain_users(domain)
        failed_users = []
        for user in users:
            user_account = portal_types.UserAccount(user.name,domain)
            try:
                admin.cloudfs.mkdir(cloud_folder, folder_group, user_account)
                logging.info('Created Cloud Folder, ' + cloud_folder + ', for ' + user.name)
            except CTERAException as error:
                logging.error(error)
                logging.warning('Failed to make Cloud Folder, ' + cloud_folder + ', for ' + user.name)
                failed_users.append(user.name)
    except CTERAException as error:
        print(error)
    if failed_users:
        print('Failed to make cloud folder for the following users:')
        for user in failed_users:
            print(user)

    # Write failed users to an output file
    failed_file = open(file_failed_users,'w') 
    for user in failed_users:
        failed_file.write(user + '\n')
    failed_file.close()    
    admin.logout()
    logging.info("Logged out of " + portal)
    logging.info('Exiting script: ' + filename)
