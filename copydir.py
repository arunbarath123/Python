import PySimpleGUI as sg
import os
from importlib.resources import path
import shutil

sg.theme('DarkGrey7')
layout = [[sg.T("")], 
        [sg.Text("Source folder: "),
        sg.Input(key="-IN2-" ,change_submits=True),
        sg.FolderBrowse(key="-IN2-")],        
    
        [sg.Text("Destination folder: "),
        sg.Input(key="-IN3-" ,change_submits=True),
        sg.FolderBrowse(key="-IN3-"),
        sg.Button("Submit")],  
]        
###Building Window
window = sg.Window('My File Browser', layout, size=(600,150))    
while True:
    event, values = window.read()    
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    elif event == "Submit": 
            csv_address2=values['-IN2-']
            sou=csv_address2
            csv_address3=values['-IN3-']
            des=csv_address3
            dir_name = csv_address2
            fol=os.path.basename(sou)
            panth2000=os.path.join(des,fol)
            shutil.copytree(sou,panth2000) 
            sg.Popup('Process Finished')
window.close()

