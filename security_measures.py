import os
import subprocess
import ctypes
import winreg as winreg

def disable_usb_ports():
    key = winreg.HKEY_LOCAL_MACHINE
    subkey = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
    with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as registry_key:
        winreg.SetValueEx(registry_key, 'Start', 0, winreg.REG_DWORD, 4)

def disable_bluetooth():
    subprocess.run(['sc', 'config', 'bthserv', 'start=disabled'], shell=True)

def disable_command_prompt():
    key = winreg.HKEY_CURRENT_USER
    subkey = r'Software\Policies\Microsoft\Windows\System'
    with winreg.CreateKeyEx(key, subkey, 0, winreg.KEY_WRITE) as registry_key:
        winreg.SetValueEx(registry_key, 'DisableCMD', 0, winreg.REG_DWORD, 2)

def block_website(website):
    hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    with open(hosts_path, 'a') as hosts_file:
        hosts_file.write(f'127.0.0.1 {website}\n')

def main():
    # Run the security measures
    disable_usb_ports()
    disable_bluetooth()
    disable_command_prompt()
    block_website('facebook.com')

    ctypes.windll.user32.MessageBoxW(0, "Security measures have been applied.", "Success", 1)

if __name__ == '__main__':
    main()