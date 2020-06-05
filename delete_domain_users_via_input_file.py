#!/usr/bin/python3
import os.path
import logging
import getpass
from cterasdk import *

# Initialize global variables
accounts = []
script_name = os.path.basename(__file__)
# Hardcoded input file name. Change to your liking.
# Usernames should be one per line. No commas.
input_file = 'delete-these-domain-users.txt'

# Enable and set logging level.
config.Logging.get().enable()
config.Logging.get().setLevel(logging.INFO)

# Log script start and prompt to set variables
logging.info('Starting script: ' + script_name)
print("This script deletes domain users from the portal " + 
        "based on an input file.")
portal = input("Enter the portal address: ")
username = input("Enter the global admin username: ")
password = getpass.getpass("Enter the password for " + username + ": ")
domain = input("Enter the domain: ")

if __name__ == "__main__":
    try:
        # Log into portal.
        admin = GlobalAdmin(portal)
        print("Logging into " + portal)
        admin.login(username, password)
        # Read usernames from input file into accounts list.
        with open(input_file) as users:
            for user in users:
                try:
                    account = portal_types.UserAccount(user.rstrip('\n'), domain)
                    accounts.append(account)
                except CTERAException as error:
                    logging.error(error)
        # Loop through accounts and try to delete them.
        for account in accounts:
            try:
                admin.users.delete(account)
                logging.info('Deleted user account: %s', account.name)
            except CTERAException as error:
                logging.error(error)
                logging.info('Failed to delete account: %s', account.name)
    except CTERAException as error:
        logging.error(error)
    admin.logut()
logging.info('Exiting script: ' + filename)
