import os
import os.path
import bitdotio
import display_module as disp

#-----------------------------------------------------------------------------------

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

b = bitdotio.bitdotio(api) #establish connection using API key

conn = b.get_connection() #connect to db
cur = conn.cursor() #cursor

char_list = [] #characters list

path = os.getcwd() #current working dir

file = open(path+"\\playerID.txt", 'r')   #get player ID
player_id = file.read()
file.close()

player_id = player_id.upper().strip() #player ID

#-----------------------------------------------------------------------------------

os.system('cls')

cur.execute(f"select * from \"siddhanth78/MainGame\".player_characters where p_id = '{player_id}'")

for x in cur.fetchall():
    print(x)