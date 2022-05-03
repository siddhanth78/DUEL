import os
import os.path
import bitdotio
import display_module as disp
import pandas as pd
import keyboard
import random
import time

#-----------------------------------------------------------------------------------

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

path = os.getcwd() #current working dir

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

print("TORK:")

print("Vulcan was once a barren land.")
print("Many civilizations have been wiped out by the super volcano that stands tall in the middle of the island.")
print("Every 10000 years, the volcano erupts and engulfs the entire area, leaving no survivors.")
print("Nine mass volcanic events have occurred.")
print("Then came along the Society of Engineers.\n\nPress 'enter' to continue.\n")

input()

print("The origins of this civilization remains unknown, but there are traces of them that lead back to before the sixth mass volcanic event.")
print("They were experts in harvesting resources from abundant and obscure sources alike, and are masters of crafting.")
print("The engineers had learnt to extract minerals and other materials from the volcano and regions surrounding it.")
print("This resulted in the volcano going permanently dormant, with mass volcanic events no more.")
print("200000 years had passed, and they lived in peace and only continued growing.")
print("Then, the unimaginable happened.\n\nPress 'enter' to continue.\n")

input()

print("The volcano erupted.")
print("Because of the resource harvesting, the eruption was not too destructive, but it did result in several lives being lost.")
print("Mage, the leader of the society, called for a council.")
print("Among the council members was one intelligent and ambitious, but rebellious, egoistic and ill-tempered man.")
print("His name was Nexus.\n\nPress 'enter' to continue.\n")

input()

print("Nexus began to doubt the capabilities of the newer generation of engineers as the volcanic event killed thousands.")
print("He raised his voice against Mage, staring down into her soul with his eyes blood-red and filled with tears.")
print("Nexus revealed that his family was killed in the event.")
print("Mage gave him her condolences, but Nexus refused to listen.")
print("He stormed out of the council, and was never seen since.")
print("Many years passed. A search party was sent out. But, nobody found him.")
print("Mage eventually called it off.")
print("The very next day, a device was set off at the headquarters of the society. The device exploded and destroyed the entire island.")
print("Now, Vulcan is a historical site.")
print("To this day, it remains a mystery as to what happened to Nexus and the Society of Engineers.\n\nPress 'enter' to continue.\n")

input()

print("We are now the fourth generation of post-Vulcan engineers.")
print("Although we craft on Ptorin, our headquarters remain hidden so that even if our island is wiped, the headquarters will still exist.")
print("To save time rebuilding, of course.")
print("The council now only intervenes during major events, if you were wondering all these years why you've never seen a member.")
print("Alright, get back to work now. Oh wait, you don't have a job here. My bad, hahahaha!\n\nPress 'enter' to continue.\n")

input()

df = pd.DataFrame({'0':['---EXIT---','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '1':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '2':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '3':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '4':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '5':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '6':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '7':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '8':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------'],
                    '9':['----------','----------','----------','----------','----------','----------','----------','----------','----------','----------']})
                    
tork = "(0_-)T"

you = "(-_-)"

df.loc[6][9] = tork

you_curloc = [6,8]
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
    tork_flag = 0
    tork_dialogue = ["Watch it, boy!", "What do you need?", "The exit isn't here.", "Beautiful day, eh? Now leave."]
    if(df.loc[you_curloc[0]][you_curloc[1]] == tork):
        df.loc[you_prevloc[0]][you_prevloc[1]] = you
        df.loc[you_curloc[0]][you_curloc[1]] = tork
        you_curloc[0] = you_prevloc[0]
        you_curloc[1] = you_prevloc[1]
        tork_flag = 1
    else:
        df.loc[you_curloc[0]][you_curloc[1]] = you
        df.loc[you_prevloc[0]][you_prevloc[1]] = '----------'
        
    os.system('cls')
    print(df)
    
    if(tork_flag == 1):
        print("\nTORK: "+random.choice(tork_dialogue))
    else:
        pass
        
    if(you_curloc[0] == 0 and you_curloc[1] == 0):
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
                
        cur.execute(f"update \"siddhanth78/MainGame\".player_progress set story = 1 where p_id = '{player_id}'")
        conn.commit()
        os.system(path+"\\STORY\\_1_.py")

keyboard.add_hotkey('up arrow', lambda:up(you_curloc, you_prevloc))
keyboard.add_hotkey('left arrow', lambda:left(you_curloc, you_prevloc))
keyboard.add_hotkey('down arrow', lambda:down(you_curloc, you_prevloc))
keyboard.add_hotkey('right arrow', lambda:right(you_curloc, you_prevloc))

os.system('cls')

print("\nUSE ARROWS TO MOVE.\n")
print(df)

while True:
    continue