#!/usr/bin/python3
import getpass
from cterasdk import *

if __name__ == "__main__":
    try:
        # Create admin object
        admin = GlobalAdmin('todd.ctera.me')
        # Log into virtual portal as admin
        #admin.login('admin', getpass.getpass())
        admin.login('admin', 'Breakthings456')
        # Create users array

        for filer in admin.devices.filers():
            filer.show('/proc/cloudsync')

    except CTERAException as e:
            print(e)
admin.logout()