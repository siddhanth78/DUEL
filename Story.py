import os
import os.path
import bitdotio
import display_module as disp
import time
#-----------------------------------------------------------------------------------

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

char_list = [] #characters list

path = os.getcwd() #current working dir

file = open(path+"\\playerID.txt", 'r')   #get player ID
player_id = file.read()
file.close()

story_progress = 0   #player story progress

player_id = player_id.upper().strip() #player ID

#-----------------------------------------------------------------------------------

cur.execute(f"select * from \"siddhanth78/MainGame\".player_characters where p_id = '{player_id}'")

for x in cur.fetchall():
    char_list.append(x)
    
cur.execute(f"select story from \"siddhanth78/MainGame\".player_progress where p_id = '{player_id}'")

for x in cur.fetchall():
    story_progress = x[0]
    
if(story_progress == 0):
    os.system(path+"\\STORY\\_0_.py")
elif(story_progress == 1):
    os.system(path+"\\STORY\\_1_.py")
elif(story_progress == 2):
    os.system(path+"\\STORY\\_2_.py")
elif(story_progress == 3):
    os.system(path+"\\STORY\\_3_.py")