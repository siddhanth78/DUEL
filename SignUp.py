import os
import os.path
import time
import bitdotio
import pwinput
import display_module as disp
import random

#-----------------------------------------------------------------------------------

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

while True:
    try:
        b = bitdotio.bitdotio(api)
        conn = b.get_connection()
        cur = conn.cursor()
    except:
        disp.error("Check your internet connection.")
        time.sleep(1)
        continue
    else:
        break

player_cred = [] #credentials list

playerid_list = [] #list of all player IDs

path = os.getcwd() #current working dir

uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") #uppercase letters
numbers = list("0123456789") #numbers

player_id = ""  #new player ID

playerid_flag = False  #to check if player ID already exists

player_user_flag = False  #to check if username already exists

#-----------------------------------------------------------------------------------

while True:
    os.system('cls')
    
    for i in range(0, 4):
        player_id = player_id + random.choice(uppercase) + random.choice(numbers) + random.choice(numbers) + random.choice(numbers)

    cur.execute("select p_id from \"siddhanth78/MainGame\".player_info")
    
    for x in cur.fetchall():
        playerid_list.append(x)
        
    if(playerid_list == []):
        pass
    else:
        for x in playerid_list[0]:
            if(player_id == x):
                player_id = ""
                playerid_flag = True
                break
    
    if(playerid_flag == True):
        player_id = ""
        playerid_flag = False
        continue
    elif(playerid_flag == False):
        print("Player ID: "+player_id)
        disp.warn("Remember your player ID! You'll need it every time to log in!")
    
    while True:
        user = input("Enter new username: ")
        
        cur.execute("select username from \"siddhanth78/MainGame\".player_info")
        
        for x in cur.fetchall():
            player_cred.append(x)
            
        if(player_cred == []):
            pass
        else:
            for x in player_cred:
                if(user == x[0]):
                    print("Username already in use.\n")
                    player_user_flag = True
                    break
        
        if(player_user_flag == True):
            player_user_flag = False
            continue
        else:
            break
    
    while True:
        passwd = input("Enter new password: ")
        confirmpasswd = input("Confirm new password: ")
        
        if(passwd == confirmpasswd):
            break
        else:
            print("\nPasswords do not match. Try again.\n")
            continue

    break
    
while True:
    try:
        b = bitdotio.bitdotio(api)
        conn = b.get_connection()
        cur = conn.cursor()
    except:
        disp.error("Check your internet connection.")
        time.sleep(1)
        continue
    else:
        break
 
cur.execute(f"insert into \"siddhanth78/MainGame\".player_info values('{player_id}', '{user}', '{passwd}', 0, 0)")
cur.execute(f"insert into \"siddhanth78/MainGame\".player_progress values('{player_id}', 0, 0, 0, '-', '-', '-', '-')")
conn.commit()

file = open(path+"\\playerID.txt", 'w')
file.write(player_id)
file.close()

print("\nSign up complete.\n")

os.system(path+"\\Start.py")