import os
import os.path
import time
import bitdotio
import pwinput
import display_module as disp

#-----------------------------------------------------------------------------------

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

b = bitdotio.bitdotio(api) #establish connection using API key

conn = b.get_connection() #connect to db
cur = conn.cursor() #cursor

player_cred = [] #credentials list

path = os.getcwd() #current working dir

file = open(path+"\\playerID.txt", 'r')   #get player ID
player_id = file.read()
file.close()

#-----------------------------------------------------------------------------------

while True:
    os.system('cls')
    if(player_id == ''):
        player_id = input("Enter your player ID: ")
        player_id = player_id.upper().strip()
    else:
        print("Obtaining player ID...")
        time.sleep(0.5)
        pass

    try:
        cur.execute(f"select username, passwd from \"siddhanth78/MainGame\".player_info where p_id = '{player_id}'")
        for x in cur.fetchall():
            player_cred.append(x)
    
        if(player_cred == []):
            disp.error("Invalid player ID.")
            file = open(path+"\\playerID.txt", 'w')
            file.write('')
            file.close()
            continue
        else:
            pass
    except:
        disp.error("Invalid player ID.")
        file = open(path+"\\playerID.txt", 'w')
        file.write('')
        file.close()
        continue
    else:
        break

print()

while True:
    user = input("Enter username: ")
    passwd = pwinput.pwinput(prompt = "Enter password: ", mask = "*")
    
    if(user!=player_cred[0][0] or passwd!=player_cred[0][1]):
        disp.error("Invalid username or password.")
        continue
    else:
        break

print("\nWelcome to DUEL!")
time.sleep(1)

file = open(path+"\\playerID.txt", 'w')
file.write(player_id)
file.close()

os.system(path+"\\Main.py")