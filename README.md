# Getting Started with the CTERA SDK

You can do this on Windows but I prefer to use a Linux VM or WSL.
For example purposes, I will assume setup is being done on Ubuntu. 
For other distros, use the appropriate package manager commands. 
After setup, the distro should not matter.



## Latest Version of Online Docs
https://ctera-python-sdk.readthedocs.io/en/latest/index.html

## GitHub Link
https://github.com/CTERA-Networks/ctera-python-sdk/

## Environment Setup Instructions

1. Update your system.

    ```sudo apt update && sudo apt upgrade```

1. Install git.

    ```sudo apt install git```

1. Install Python3.

    ```sudo apt install python3```

1. Download the CTERA SDK for Python source to your current working directory.

    ```git clone https://github.com/CTERA-Networks/ctera-python-sdk.git```
    
1. Setup CTERA SDK

    ```cd ctera-python-sdk```
    
    ```python3 setup.py install```

## CTERA SDK Setup in Interactive Mode.

Do these steps each time to test things interactively in the Python Console.

1. Change into the CTERA SDK folder.

    ```cd ctera-python-sdk```

1. Enter Python Console.

    ```python3```

    Your shell prompt will change to this: ```>>>```

1. Import CTERA SDK Libraries.

    ```from cterasdk import *```

1. Create a Global Admin object to work with.

    ```admin = GlobalAdmin('portal.example.com')```

1. Log into the tenant above as a global administrator.

    ```admin.login('admin', 'P@ssw0rd123!')```

1. Check your host, context, and current tenant.
    
    ```admin.whoami()```

1. Switch between browsing the Administration and team portal tenant.

    ```admin.portals.browse_global_admin()```
    
    ```admin.portals.browse('cloud-dev')```

1. When you are done playing, logout and exit Python

    ```admin.logout()```

    ```Ctrl+d```
