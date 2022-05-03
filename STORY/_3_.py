import os
import os.path
import bitdotio
import display_module as disp
import pandas as pd
import keyboard
import random
import time

#-----------------------------------------------------------------------------------

path = os.getcwd() #current working dir

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

while True:
    try:
        b = bitdotio.bitdotio(api)
        conn = b.get_connection()
        cur = conn.cursor()
    except:
        disp.error("Check your internet connection.")
        time.sleep(3)
        continue
    else:
        break
        
file = open(path+"\\playerID.txt", 'r')   #get player ID
player_id = file.read()
file.close()

#-----------------------------------------------------------------------------------

os.system('cls')

df = pd.DataFrame({'0':['----------','----------','----------','----------','--BORDER--','----------','----------','----------','----------','----------'],
                    '1':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '2':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '3':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '4':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '5':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '6':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '7':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '8':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '9':['----------','----------','----------','----------','----------','----------','----------','----------','----------','---MAIN---']})
                    

you = "(-_-)"

you_curloc = [0,0]
you_prevloc = [0,0]

df.loc[you_curloc[0]][you_curloc[1]] = you

def up(you_curloc, you_prevloc):
    if(you_curloc[0] == 0):
        pass
    else:
        you_prevloc[0] = you_curloc[0]
        you_prevloc[1] = you_curloc[1]
        you_curloc[0] = you_curloc[0]-1
    move(you_curloc, you_prevloc)
    
def down(you_curloc, you_prevloc):
    if(you_curloc[0] == 9):
        pass
    else:
        you_prevloc[0] = you_curloc[0]
        you_prevloc[1] = you_curloc[1]
        you_curloc[0] = you_curloc[0]+1
    move(you_curloc, you_prevloc)
    
def left(you_curloc, you_prevloc):
    if(you_curloc[1] == 0):
        pass
    else:
        you_prevloc[0] = you_curloc[0]
        you_prevloc[1] = you_curloc[1]
        you_curloc[1] = you_curloc[1]-1
    move(you_curloc, you_prevloc)
    
def right(you_curloc, you_prevloc):
    if(you_curloc[1] == 9):
        pass
    else:
        you_prevloc[0] = you_curloc[0]
        you_prevloc[1] = you_curloc[1]
        you_curloc[1] = you_curloc[1]+1
    move(you_curloc, you_prevloc)
    
def move(you_curloc, you_prevloc):
    df.loc[you_curloc[0]][you_curloc[1]] = you
    df.loc[you_prevloc[0]][you_prevloc[1]] = '----------'
        
    os.system('cls')
    print(df)
        
    if(you_curloc[0] == 9 and you_curloc[1] == 9):
    
        os.system(path+"\\Main.py")
        
    elif(you_curloc[0] == 4 and you_curloc[1] == 0):
    
        while True:
            try:
                b = bitdotio.bitdotio(api)
                conn = b.get_connection()
                cur = conn.cursor()
            except:
                disp.error("Check your internet connection.")
                time.sleep(3)
                continue
            else:
                break
                
        cur.execute(f"update \"siddhanth78/MainGame\".player_progress set story = 4 where p_id = '{player_id}'")
        conn.commit()
        os.system(path+"\\STORY\\_4_.py")

keyboard.add_hotkey('up arrow', lambda:up(you_curloc, you_prevloc))
keyboard.add_hotkey('left arrow', lambda:left(you_curloc, you_prevloc))
keyboard.add_hotkey('down arrow', lambda:down(you_curloc, you_prevloc))
keyboard.add_hotkey('right arrow', lambda:right(you_curloc, you_prevloc))

os.system('cls')

print("\nUSE ARROWS TO MOVE.\n")
print(df)

while True:
    continue