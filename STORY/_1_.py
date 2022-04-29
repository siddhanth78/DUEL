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

df = pd.DataFrame({'0':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '1':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '2':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '3':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '4':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '5':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '6':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '7':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '8':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '9':['----------','----------','----------','----------','----------','----------','----------','----------','----------','---EXIT---']})
                    
mage = "|(- _ -) "

you = "(-_-)"

df.loc[7][1] = mage

you_curloc = [0,9]
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
    mage_flag = 0
    if(df.loc[you_curloc[0]][you_curloc[1]] == mage):
        df.loc[you_prevloc[0]][you_prevloc[1]] = you
        df.loc[you_curloc[0]][you_curloc[1]] = mage
        you_curloc[0] = you_prevloc[0]
        you_curloc[1] = you_prevloc[1]
        mage_flag = 1
    else:
        df.loc[you_curloc[0]][you_curloc[1]] = you
        df.loc[you_prevloc[0]][you_prevloc[1]] = '----------'
        
    os.system('cls')
    print(df)
    
    if(mage_flag == 1):
        
        print("\nMAGE:")
        print("Ah, you are here.")
        print("I wanted to meet you.")
        print("My sources tell me that Nexus was spotted in Derkaan.\n\nPress 'enter' to continue.\n")

        input()
        
        print("YOU:")
        print("Isn't Derkaan off-limits?\n\nPress 'enter' to continue.\n")

        input()
        
        print("MAGE:")
        print("Hence, the discretion.")
        print("At the headquarters' lab, we are working on synthesis chambers.")
        print("In fact, we have completed one.")
        print("As you know, we are not known for our combat capabilities.")
        print("These chambers will fulfill those needs for us.\n\nPress 'enter' to continue.\n")

        input()
        
        print("YOU:")
        print("Why do you need me again?\n\nPress 'enter' to continue.\n")

        input()
        
        print("AGAIN, on this island, you are the only one who specializes in neural devices.")
        print("I want you to help us control the warriors that are synthesized.\n\nPress 'enter' to continue.\n")

        input()
        
        print("You want to go face-to-face with Nexus and his army?")
        print("It's suicide.\n\nPress 'enter' to continue.\n")

        input()
        
        print("MAGE:")
        print("These warriors are no ordinary ones.")
        print("These are specifically built to counter Nexus and the Derkaan army.")
        print("I know that the Derkaan army is extraordinarily powerful, but trust me, these warriors will come in handy.\n\nPress 'enter' to continue.\n")

        input()
        
        print("YOU:")
        print("I see.")
        print("Have you conducted any tests?\n\nPress 'enter' to continue.\n")

        input()
        
        print("MAGE:")
        print("That is the other reason for wanting to meet you.")
        print("I need you to go to the outskirts of Derkaan for a test run.\n\nPress 'enter' to continue.\n")

        input()
        
        print("YOU:")
        print("If I don't come back in a day, it means I'm dead.\n\nPress 'enter' to continue.\n")

        input()
        
        print("MAGE:")
        print("Well in that case, I wish you the best of luck. Although, you probably won't need it.\n\nPress 'enter' to continue.\n")

        input()
        
        os.system('cls')
        print(df)
        
    else:
        pass
        
    if(you_curloc[0] == 9 and you_curloc[0] == 9):
    
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
                
        cur.execute(f"update \"siddhanth78/MainGame\".player_progress set story = 2 where p_id = '{player_id}'")
        conn.commit()
        os.system(path+"\\STORY\\_2_.py")

keyboard.add_hotkey('up arrow', lambda:up(you_curloc, you_prevloc))
keyboard.add_hotkey('left arrow', lambda:left(you_curloc, you_prevloc))
keyboard.add_hotkey('down arrow', lambda:down(you_curloc, you_prevloc))
keyboard.add_hotkey('right arrow', lambda:right(you_curloc, you_prevloc))

os.system('cls')

print("\nUSE ARROWS TO MOVE.\n")
print(df)

while True:
    continue