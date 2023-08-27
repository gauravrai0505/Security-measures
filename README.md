
# Windows Security Measures 
## Overview
This script is designed to apply security measures to a Windows system by modifying system settings and configurations. It employs functions to disable USB ports, Bluetooth functionality, Command Prompt access, and block access to specific websites through the manipulation of system settings.

## Contents
1.Introduction

2.Functions
+ disable_usb_ports()
+ disable_bluetooth()
+ disable_command_prompt()
+ block_website(website)
  
3.Execution

## Introduction
The script targets Windows systems to implement a set of security measures aimed at restricting access to certain functionalities and websites. The measures include disabling USB storage devices, disabling Bluetooth, restricting Command Prompt usage, and blocking access to a specific website.

## Functions

### disable_usb_ports()
This function modifies the Windows Registry to disable USB storage devices. It achieves this by changing the "Start" value of the USBSTOR service to 4, indicating "Disabled." USB storage devices will no longer function on the system.

### disable_bluetooth()
This function uses the subprocess.run command to disable Bluetooth functionality by configuring the "bthserv" service. It sets the service's startup type to "Disabled," effectively preventing Bluetooth devices from functioning on the system.

### disable_command_prompt()
This function restricts access to the Command Prompt for the current user. It modifies the Windows Registry to set the "DisableCMD" value to 2, effectively preventing the Command Prompt from being accessed.

### block_website(website)
This function blocks access to a specific website by modifying the hosts file located at C:\Windows\System32\drivers\etc\hosts. It adds an entry to the hosts file that redirects the specified website's IP address to the loopback address (127.0.0.1). Please note that the effectiveness of this method may vary depending on browser and DNS settings.

## Execution

To run the script:

+ Ensure you have Python installed on your Windows system.
+ Open a Command Prompt with administrative privileges.
+ Navigate to the directory containing the script using the cd command.
+ Run the script using the command: python script_filename.py
+ Follow any prompts and confirm administrative permissions, if required.

![VirtualBox_windows_26_08_2023_23_03_48](https://github.com/gauravrai0505/Security-measures/assets/75598640/a7979740-1f1d-4462-8f32-008405936c2b)

![VirtualBox_windows_26_08_2023_23_05_19](https://github.com/gauravrai0505/Security-measures/assets/75598640/5cf0d7f8-bc4a-44a4-a24d-aac3e8bfd8e4)

![VirtualBox_windows_26_08_2023_23_07_47](https://github.com/gauravrai0505/Security-measures/assets/75598640/dd3eba91-1515-4b54-88d3-94ef8909a219)





