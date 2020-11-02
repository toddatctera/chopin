#!/usr/bin/python3
# to save logs, run `export CTERASDK_LOG_FILE=<logname>`
from cterasdk import *
import getpass
import os.path
import logging

filename = os.path.basename(__file__)

config.Logging.get().enable()
config.Logging.get().setLevel(logging.INFO)

# Read input from keyboard and store into global variables.
def run():
    try:
        logging.info("Starting script: " + filename)
        portal = input("Please enter the portal address: ")
        username = input("Please enter the global admin username: ")
        password = getpass.getpass("Please enter the password for " + username + ": ")
        domain = input("Please enter the domain: ")
    except CTERAException as error:
        logging.error(error)

    if __name__ == "__main__":
        try:
            admin = GlobalAdmin(portal)
            logging.info("Logging into " + portal)
            admin.login(username, password)
            logging.info("Successfully logged in to " + portal)
        except CTERAException as error:
            logging.warning(error)
        admin.logout()
        logging.info("Logged out of " + portal)
        logging.info('Exiting script: ' + filename)

run()
