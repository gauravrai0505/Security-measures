import os
import subprocess
import ctypes
import _winreg as winreg

def disable_usb_ports():
    # Disable USB storage devices by modifying the USBSTOR service's start type in the Windows Registry.
    key = winreg.HKEY_LOCAL_MACHINE
    subkey = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
    with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as registry_key:
        winreg.SetValueEx(registry_key, 'Start', 0, winreg.REG_DWORD, 4)

def disable_bluetooth():
    # Disable Bluetooth functionality by configuring the bthserv service to start as "Disabled."
    subprocess.run(['sc', 'config', 'bthserv', 'start=disabled'], shell=True)

def disable_command_prompt():
    # Disable the Command Prompt for the current user by modifying the Windows Registry.
    key = winreg.HKEY_CURRENT_USER
    subkey = r'Software\Policies\Microsoft\Windows\System'
    with winreg.CreateKeyEx(key, subkey, 0, winreg.KEY_WRITE) as registry_key:
        winreg.SetValueEx(registry_key, 'DisableCMD', 0, winreg.REG_DWORD, 2)

def block_website(website):
    # Block access to a specified website by adding an entry to the hosts file.
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    with open(hosts_path, 'a') as hosts_file:
        hosts_file.write(f'127.0.0.1 {website}\n')

def main():
    # Main function to apply security measures and display a success message.
    disable_usb_ports()
    disable_bluetooth()
    disable_command_prompt()
    block_website('facebook.com')

    # Display a success message using a Windows message box.
    ctypes.windll.user32.MessageBoxW(0, "Security measures have been applied.", "Success", 1)

if __name__ == '__main__':
    # Entry point of the program. Call the main function when the script is executed.
    main()
