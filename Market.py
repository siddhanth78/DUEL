import os
import os.path
import bitdotio
import display_module as disp
import nltk.tokenize as tokenize
import random

#-----------------------------------------------------------------------------------

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

b = bitdotio.bitdotio(api) #establish connection using API key

conn = b.get_connection() #connect to db
cur = conn.cursor() #cursor

char_list = [] #characters list

bronze_chars = [] #bronze characters
silver_chars = [] #silver characters
gold_chars = [] #gold characters
platinum_chars = [] #platinum characters

player_chars = [] #player's characters

player_cred = [] #player info

path = os.getcwd() #current working dir

options = ['Search', 'Buy', 'Exit'] #menu options

menu = disp.menu(title = "Market",
                items = options,
                reuse = 1
                    )       #main menu

file = open(path+"\\playerID.txt", 'r')   #get player ID
player_id = file.read()
file.close()

player_id = player_id.upper().strip() #player ID

chambers = disp.menu("Synthesis chamber",
                            ["Random (Price: 53000 points)",   #synthesis chamber menu (to buy characters)
                            "Bronze (Price: 20000 points)",
                            "Silver (Price: 39500 points)",
                            "Gold (Price: 79000 points)",
                            "Platinum (Price: 155000 points)",
                            "Exit"],
                            1)

#-----------------------------------------------------------------------------------
os.system('cls')

cur.execute(f"select points from \"siddhanth78/MainGame\".player_info where p_id = '{player_id}'")

for x in cur.fetchall():
    player_cred.append(x)
    
points = player_cred[0][0]

cur.execute(f"select ch_id, attack, health from \"siddhanth78/MainGame\".player_characters where p_id = '{player_id}'")

for x in cur.fetchall():
    player_chars.append(x[0])

cur.execute(f"select ch_id, name, rank, attack, health from \"siddhanth78/MainGame\".characters")

for x in cur.fetchall():
    char_list.append(x)

for x in char_list:

    if(x[2] == "bronze"):
        bronze_chars.append(x)
    elif(x[2] == "silver"):
        silver_chars.append(x)
    elif(x[2] == "gold"):
        gold_chars.append(x)
    elif(x[2] == "platinum"):
        platinum_chars.append(x)
        
    disp.box(title = x[1],
            m = f"Rank: {x[2]}\nAttack: {x[3]}\nHealth: {x[4]}")
            

print("Available characters ^^^")

while True:
    print(menu)
    choice = input("Enter your choice: ")
    
    if(choice == "1"):
        b = bitdotio.bitdotio(api)
        conn = b.get_connection()
        cur = conn.cursor()
        disp.warn("Search is case-sensitive.")
        
        while True:
            search = input("Enter <field> <query> (Enter 'quit' to exit search): ")
            
            if(search.lower().strip() == 'quit'):
                print()
                break
                
            tokens = tokenize.word_tokenize(search)
            searchlist = []
            
            print(tokens)
        
            if(tokens[0].lower() == "name"):
                cur.execute(f"select name, rank, attack, health from \"siddhanth78/MainGame\".characters where name like '%{tokens[1]}%'")
            elif(tokens[0].lower() == "rank"):
                cur.execute(f"select name, rank, attack, health from \"siddhanth78/MainGame\".characters where rank like '%{tokens[1]}%'")
            else:
                disp.error("Invalid field.\nValid fields: name, rank")
                continue
        
            for x in cur.fetchall():
                searchlist.append(x)
            
            if(searchlist == []):
                disp.info("No results found.")
                continue
            
            for x in searchlist:
                disp.box(title = x[0],
                        m = f"Rank: {x[1]}\nAttack: {x[2]}\nHealth: {x[3]}")
                    
    elif(choice == "2"):
        b = bitdotio.bitdotio(api)
        conn = b.get_connection()
        cur = conn.cursor()
        
        while True:
            player_chars = []
            cur.execute(f"select ch_id, attack, health from \"siddhanth78/MainGame\".player_characters where p_id = '{player_id}'")
            for x in cur.fetchall():
                player_chars.append(x)
                
            print(chambers)
            print(f"Points available: {points}\n")
            select_chamber = input("Enter your choice: ")   
            
            if(select_chamber == '1'):
                if(points < 53000):
                    disp.error("Not enough points.")
                    break
                else:
                    chance = random.random()
                    
                    if(chance < 0.6):
                        random_char = random.choice(bronze_chars)
                    elif(0.6 <= chance < 0.8):
                        random_char = random.choice(silver_chars)
                    elif(0.8 <= chance < 0.95):
                        random_char = random.choice(gold_chars)
                    elif(0.95 <= chance <= 1):
                        random_char = random.choice(platinum_chars)
            elif(select_chamber == '2'):
                if(points < 20000):
                    disp.error("Not enough points.")
                    break
                else:
                    chance = random.random()
                    random_char = random.choice(bronze_chars)
            elif(select_chamber == '3'):
                if(points < 39500):
                    disp.error("Not enough points.")
                    break
                else:
                    chance = random.random()
                    random_char = random.choice(silver_chars)
            elif(select_chamber == '4'):
                if(points < 79000):
                    disp.error("Not enough points.")
                    break
                else:
                    chance = random.random()
                    random_char = random.choice(gold_chars)
            elif(select_chamber == '5'):
                if(points < 155000):
                    disp.error("Not enough points.")
                    break
                else:
                    chance = random.random()
                    random_char = random.choice(platinum_chars)
            elif(select_chamber == '6'):
                confirm = disp.yesno()
        
                if(confirm == 1):
                    break
                elif(confirm == 0):
                    continue
                elif(confirm == 2):
                    disp.error("Invalid choice.")
                    continue
            else:
                disp.error("Invalid choice.")
                break
                
            dupe_flag = False
            char_index = 0
            
            for x in player_chars:
                if(random_char[0] == x[0]):
                    char_index = player_chars.index(x)
                    dupe_flag = True
                    break
                    
            if(dupe_flag == True):
                player_chars_list = list(player_chars[char_index])
                
                if(random_char[2] == "bronze"):
                    player_chars_list[1] = player_chars_list[1] + 20
                    player_chars_list[2] = player_chars_list[2] + 200
                elif(random_char[2] == "silver"):
                    player_chars_list[1] = player_chars_list[1] + 70
                    player_chars_list[2] = player_chars_list[2] + 450
                elif(random_char[2] == "gold"):
                    player_chars_list[1] = player_chars_list[1] + 130
                    player_chars_list[2] = player_chars_list[2] + 900
                elif(random_char[2] == "platinum"):
                    player_chars_list[1] = player_chars_list[1] + 200
                    player_chars_list[2] = player_chars_list[2] + 1500
            
            try:
                if(dupe_flag == False):
                    cur.execute(f"insert into \"siddhanth78/MainGame\".player_characters values('{player_id}', '{random_char[0]}', {random_char[3]}, {random_char[4]}, 1)")
                    conn.commit()
                elif(dupe_flag == True):
                    cur.execute(f"update \"siddhanth78/MainGame\".player_characters set attack = {player_chars_list[1]} where p_id = '{player_id}' and ch_id = '{random_char[0]}'")
                    cur.execute(f"update \"siddhanth78/MainGame\".player_characters set health = {player_chars_list[2]} where p_id = '{player_id}' and ch_id = '{random_char[0]}'")
                    conn.commit()
            except:
                disp.error("Synthesizer not working as intended. Try again later.")
                break
            else:
                if(select_chamber == '1'):
                    points = points - 53000
                elif(select_chamber == '2'):
                    points = points - 20000
                elif(select_chamber == '3'):
                    points = points - 39500
                elif(select_chamber == '4'):
                    points = points - 79000
                elif(select_chamber == '5'):
                    points = points - 155000
                else:
                    pass
                    
                if(dupe_flag == True):
                    disp.box("SYNTHESIS COMPLETE", f"DUPLICATE:\n{random_char[1]}\nRank: {random_char[2]}")
                elif(dupe_flag == False):
                    disp.box("SYNTHESIS COMPLETE", f"{random_char[1]}\nRank: {random_char[2]}")
                cur.execute(f"update \"siddhanth78/MainGame\".player_info set points = {points} where p_id = '{player_id}'")
                conn.commit()
                continue
                    
    elif(choice == "3"):
        confirm = disp.yesno()
        
        if(confirm == 1):
            os.system(path+"\\Main.py")
        elif(confirm == 0):
            continue
        elif(confirm == 2):
            disp.error("Invalid choice.")
            continue
    else:
        disp.error("Invalid choice.")

