#Copyright (C) 2022  Casey Koehn

#Contact at: caseykoehn3@gmail.com

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

#imports the needed librarys
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog

print("Chipper Copyright (C) 2022 Casey Koehn\nThis program comes with ABSOLUTELY NO WARRANTY;\nThis is free software, and you are welcome to redistribute it\nunder certain conditions.")

global boot #making "boot" a global
boot = ""

def select(): #defining the command "select"
    global boot #making "boot" a global
    boot = filedialog.askdirectory(initialdir="/", title="Select Folder") #opening file dialog to select folder
    if(not(len(boot) == 0)): #checking to see if the "boot" string is empty
        entryBoot.delete(0,"end") #deleting the contents of the "Boot" entry box
        entryBoot.insert(0, boot) #setting the contents of the "Boot" entry box to the boot directory

def start(): #defining the command "start"
    ssid = entrySsid.get() #getting the contents of the "Wifi SSID" entry box
    password = entryPsswd.get() #getting the contents of the "Wifi Password" entry box
    directory_ssh = (boot+"/ssh")
    directory_wpa = (boot+"/wpa_supplicant.conf")
    if(not(len(boot) == 0)): #checking to see if the "boot" string is empty
        if(not(len(ssid) == 0)): #checking to see if the "ssid" string is empty
            if(not(len(password) == 0)): #checking to see if the "password" string is empty
               ssh = open(directory_ssh, "w") #creating the ssh file needed to enable ssh on raspberry pi startup
               ssh.close()
               wpa = open(directory_wpa, "w")
               wpa.write("country=US\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\n\nnetwork={\nscan_ssid=1\nssid="+ssid+"\npsk="+password+"\n}")
               wpa.close()
               window.destroy() #closing the tkinter window
               #printing the strings in the shell
               print(directory_ssh)
               print(directory_wpa)
               print("country=US\nctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\nupdate_config=1\n\nnetwork={\nscan_ssid=1\nssid="+ssid+"\npsk="+password+"\n}")

window = tk.Tk() #defining the window string
window.title('Raspberry Pi Headless Setup') #setting the tkinter window title
window.geometry('350x200') #specifying the size of the tkinter window

#setting the tkinter window widgets specifications
buttonSelect = tk.Button(text="Select Boot Folder", command=select) 
labelBoot = tk.Label(text="Boot Directory")
entryBoot = tk.Entry()
labelSsid = tk.Label(text="Wifi SSID")
entrySsid = tk.Entry()
labelPsswd = tk.Label(text="Wifi Password")
entryPsswd = tk.Entry()
buttonStart = tk.Button(text="Setup", command=start)

#showing all widgets in tkinter window in order
labelBoot.pack()
entryBoot.pack()
buttonSelect.pack()
labelSsid.pack()
entrySsid.pack()
labelPsswd.pack()
entryPsswd.pack()
buttonStart.pack()

window.mainloop()
