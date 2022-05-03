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

df = pd.DataFrame({'0':['----------','----------','----------','----------','----------','----------','----------','----------','----------','---EXIT---'],
                    '1':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '2':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '3':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '4':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '5':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '6':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '7':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '8':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '9':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------']})
                    
mage = "|(- _ -) "

you = "(-_-)"

df.loc[7][7] = mage

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
        print("You're late.")
        print("I assumed you knew your way around HQ.\n\nPress 'enter' to continue.\n")

        input()
        
        print("YOU:")
        print("Been a while.\n\nPress 'enter' to continue.\n")

        input()
        
        print("MAGE:")
        print("And I assume Tork doesn't know of this.\n\nPress 'enter' to continue.\n")

        input()
        
        print("YOU:")
        print("No, he doesn't\n\nPress 'enter' to continue.\n")

        input()
        
        os.system('cls')
        print(df)
        
        print("\nMAGE:")
        print("Very well.")
        print("Here is the test warrior you asked for.")
        print("You can keep it.\n\nPress 'enter' to continue.\n")

        input()
        
        print("YOU:")
        print("Well, that's very polite of you.\n\nPress 'enter' to continue.\n")

        input()
        
        print("MAGE:")
        print("Appreciate the sarcasm.")
        print("Dmitri will meet you at the border.")
        print("Stay safe.\n\nPress 'enter' to continue.\n")

        input()
        
        print("YOU:")
        print("Will do.\n\nPress 'enter' to continue.\n")

        input()
        
        print("RECEIVE YOUR WARRIOR ON YOUR WAY OUT.\n\nPress 'enter' to continue.\n")

        input()
        
        os.system('cls')
        print(df)
        
    else:
        pass
        
    if(you_curloc[0] == 9 and you_curloc[1] == 0):
    
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
                
        ch_ids = []
                
        cur.execute(f"select ch_id from \"siddhanth78/MainGame\".player_characters where p_id = '{player_id}'")
        
        for x in cur.fetchall():
            ch_ids.append(x[0])
                
        cur.execute(f"update \"siddhanth78/MainGame\".player_progress set story = 3 where p_id = '{player_id}'")
        if("B001" not in ch_ids):
            cur.execute(f"insert into \"siddhanth78/MainGame\".player_characters values('{player_id}', 'B001', 10, 200, 1)")
            print("\nYou have received 'SAM'! Check your characters for more info.")
        conn.commit()
        os.system(path+"\\STORY\\_3_.py")

keyboard.add_hotkey('up arrow', lambda:up(you_curloc, you_prevloc))
keyboard.add_hotkey('left arrow', lambda:left(you_curloc, you_prevloc))
keyboard.add_hotkey('down arrow', lambda:down(you_curloc, you_prevloc))
keyboard.add_hotkey('right arrow', lambda:right(you_curloc, you_prevloc))

os.system('cls')

print("\nUSE ARROWS TO MOVE.\n")
print(df)

while True:
    continue