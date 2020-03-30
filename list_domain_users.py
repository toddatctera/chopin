#!/usr/bin/python3
from cterasdk import *
import getpass

print("This script will write or overwrite a file containing usersnames for the specified domain.")
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
        print ("Getting list of portal users in " + domain)
        users = admin.users.list_domain_users(domain)
        filename = domain + "-users.txt"
        file = open(filename, "w")
        for user in users:
            print(user.name)
            file.write(user.name + '\n')
        file.close()
        print("Usernames have been written to " + filename)
        print("Logging out of the portal...")
        admin.logout()
        print("Exiting script. Have a nice day.")
    except CTERAException as error:
        print(error)
