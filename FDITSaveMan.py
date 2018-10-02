#FDIT Save Manager
import os
from pathlib import Path
import configparser

#Variable Declarations
savefilename = 'FDITSave.ini'
buttonactions = []
config = configparser.ConfigParser() #Init Config Parser Object

def initsave():
    checksave() #Check if save exists, create it if not

def getbuttonactionlist():
    return buttonactionlist

def getnumbuttons():
    return int(numbuttons)

def checksave(): #Creates save file object with appropriate checks

    filecheck = Path(savefilename)
    if filecheck.is_file():
        print(savefilename + ' is file.')
    else:
        initfillsave() #Save data if file doesn't exist.

def initfillsave(): #Fills save file with default values
    config['Settings'] = {}
    config['Settings']['NumButtons'] = str(8) #Only supports 8 Buttons Max Currently
    config['Settings']['Button1Action'] = 'Food'
    config['Settings']['Button2Action'] = 'Water'
    config['Settings']['Button3Action'] = 'Treat'
    config['Settings']['Button4Action'] = '#1'
    config['Settings']['Button5Action'] = '#2'
    config['Settings']['Button6Action'] = 'Walk'
    config['Settings']['Button7Action'] = 'Custom'
    config['Settings']['Button8Action'] = 'Custom'
    with open(savefilename, 'w') as configfile:
        config.write(configfile)
        configfile.close()

initsave()
config.read(savefilename); #Update config object to reflect current values

#Put new values into vars
numbuttons = config['Settings']['NumButtons']
button1action = config['Settings']['Button1Action']
button2action = config['Settings']['Button2Action']
button3action = config['Settings']['Button3Action']
button4action = config['Settings']['Button4Action']
button5action = config['Settings']['Button5Action']
button6action = config['Settings']['Button6Action']
button7action = config['Settings']['Button7Action']
button8action = config['Settings']['Button8Action']

buttonactionlist = [button1action, button2action, button3action, button4action, button5action, button6action, button7action ,button8action]

