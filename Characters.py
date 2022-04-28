import os
import os.path
import bitdotio
import display_module as disp
import nltk.tokenize as tokenize
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

char_info = [] #player's character info
names_and_ranks = [] #player's characters' names and ranks

upgrades = {}

path = os.getcwd() #current working dir

options = ['Search', 'Upgrade', 'Exit'] #menu options

menu = disp.menu(title = "Characters",
                items = options,
                reuse = 1
                    )       #main menu

file = open(path+"\\playerID.txt", 'r')   #get player ID
player_id = file.read()
file.close()

player_id = player_id.upper().strip() #player ID

#-----------------------------------------------------------------------------------

os.system('cls')

cur.execute(f"select ch_id, attack, health, level from \"siddhanth78/MainGame\".player_characters where p_id = '{player_id}'")
                
for x in cur.fetchall():
    char_list.append(x)
                
for x in char_list:
    cur.execute(f"select name, rank from \"siddhanth78/MainGame\".characters where ch_id = '{x[0]}'")
    for y in cur.fetchall():
        names_and_ranks.append(y)
                        
for i in range(0, len(char_list)):
    char_info.append((names_and_ranks[i][0], names_and_ranks[i][1], char_list[i][1], char_list[i][2], char_list[i][3]))
    
for x in char_info:
    disp.box(title = x[0],
            m = f"Rank: {x[1]}\nAttack: {x[2]}\nHealth: {x[3]}")
            
print("Your characters ^^^")
    
while True:
    print(menu)
    choice = input("Enter your choice: ")
    
    if(choice == '1'):
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
                
        disp.warn("Search is case-sensitive.")
        
        while True:
            search = input("Enter <field> <query> (Enter 'quit' to exit search): ")
            
            if(search.lower().strip() == 'quit'):
                print()
                break
                
            tokens = tokenize.word_tokenize(search)
            searchlist = []
            name_and_rank_list = []
            all_info = []
            results = []
            
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
        
            if(tokens[0].lower() == "name" or tokens[0].lower() == "rank"):
                cur.execute(f"select ch_id, attack, health from \"siddhanth78/MainGame\".player_characters where p_id = '{player_id}'")
                
                for x in cur.fetchall():
                    searchlist.append(x)
                
                for x in searchlist:
                    cur.execute(f"select name, rank from \"siddhanth78/MainGame\".characters where ch_id = '{x[0]}'")
                    for y in cur.fetchall():
                        name_and_rank_list.append(y)
                        
                for i in range(0, len(searchlist)):
                    all_info.append((name_and_rank_list[i][0], name_and_rank_list[i][1], searchlist[i][1], searchlist[i][2]))
                
                if(tokens[0] == 'name'):
                    for x in all_info:
                        if(tokens[1] in x[0]):
                            results.append(x)
                elif(tokens[0] == 'rank'):
                    for x in all_info:
                        if(tokens[1] in x[1]):
                            results.append(x)
                        
                for x in results:
                    disp.box(title = x[0],
                        m = f"Rank: {x[1]}\nAttack: {x[2]}\nHealth: {x[3]}")
                
            else:
                disp.error("Invalid field.\nValid fields: name, rank")
                continue
        
            for x in cur.fetchall():
                searchlist.append(x)
            
            if(results == []):
                disp.info("No results found.")
                continue
                        
    elif(choice == '2'):
        
        while True:
        
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
            
            player_currency = []
            
            cur.execute(f"select points, runes from \"siddhanth78/MainGame\".player_info where p_id = '{player_id}'")
            
            for x in cur.fetchall():
                player_currency.append(x)
                
            points = player_currency[0][0]
            runes = player_currency[0][1]
        
            char_menu_options = []
            char_list = []
            char_info = []
            names_and_ranks = []
        
            cur.execute(f"select ch_id, attack, health, level from \"siddhanth78/MainGame\".player_characters where p_id = '{player_id}'")
                
            for x in cur.fetchall():
                char_list.append(x)
                
            for x in char_list:
                cur.execute(f"select name, rank from \"siddhanth78/MainGame\".characters where ch_id = '{x[0]}'")
                for y in cur.fetchall():
                    names_and_ranks.append(y)
                        
            for i in range(0, len(char_list)):
                char_info.append((names_and_ranks[i][0], names_and_ranks[i][1], char_list[i][1], char_list[i][2], char_list[i][3]))
    
            for x in char_info:
                char_menu_options.append(f"{x[0]} [Rank: {x[1]}] <Current Stats: [Lvl: {x[4]}] [Atk: {x[2]}] [Hlth: {x[3]}]>")
            
            for i in range(0, len(char_menu_options)):
                upgrades[str(i+1)] = char_menu_options[i]
    
            char_menu = disp.menu("Your characters",
                                    char_menu_options, 1)
        
            print(char_menu)
            print(f"Points available: {points}")
            print(f"Runes available: {runes}\n")
            upgrade_choice = input("Enter your choice (Enter 'quit' to exit upgrade): ")
            
            if(upgrade_choice.lower().strip() == 'quit'):
                print()
                break
            
            if(upgrade_choice not in upgrades.keys()):
                disp.error("Invalid choice.")
                continue
                
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
                
            selection = upgrades[upgrade_choice]
            selection_tokens = tokenize.word_tokenize(selection)
            selection_tokens_filter = [selection_tokens[0], selection_tokens[4], int(selection_tokens[13]), int(selection_tokens[18]), int(selection_tokens[23])]
            
            cur.execute(f"select ch_id from \"siddhanth78/MainGame\".characters where name = '{selection_tokens_filter[0]}'")
            
            for x in cur.fetchall():
                selection_tokens_filter.append(x[0])
                
            disp.box(selection_tokens_filter[0],
                    f"Rank: {selection_tokens_filter[1]}\nLevel: {selection_tokens_filter[2]}\nAttack: {selection_tokens_filter[3]}\nHealth: {selection_tokens_filter[4]}")
                    
            if(selection_tokens_filter[2] == 50):
                disp.info("Character maxed out.")
                continue
                
            b = bitdotio.bitdotio(api)
            conn = b.get_connection()
            cur = conn.cursor()
            
            rune_flag = False
                
            if(selection_tokens_filter[1] == 'bronze'):
                if(selection_tokens_filter[2]%10 == 0):
                    rune_flag = True
                    confirm = disp.custom_yesno(f"Spend {5000*(selection_tokens_filter[2]/10)} points to use {10*(selection_tokens_filter[2]/10)} runes?")
                else:
                    confirm = disp.custom_yesno(f"Spend {1000*selection_tokens_filter[2]} points to upgrade?")
        
                if(confirm == 1):
                    pass
                elif(confirm == 0):
                    continue
                elif(confirm == 2):
                    disp.error("Invalid choice.")
                    continue
                    
                if(rune_flag == False):
                
                    if(points < 1000*selection_tokens_filter[2]):
                        disp.error("Not enough points.")
                        continue
                    else:
                        points = points - 1000*selection_tokens_filter[2]
                        selection_tokens_filter[2] = selection_tokens_filter[2] + 1
                        selection_tokens_filter[3] = selection_tokens_filter[3] + 5
                        selection_tokens_filter[4] = selection_tokens_filter[4] + 50
                        
                elif(rune_flag == True):
                
                    if(points < (5000*(selection_tokens_filter[2]/10))):
                        disp.error("Not enough points.")
                        continue
                    elif(runes < (10*(selection_tokens_filter[2]/10))):
                        disp.error("Not enough runes.")
                        continue
                    else:
                        runes = runes - (10*(selection_tokens_filter[2]/10))
                        points = points - (5000*(selection_tokens_filter[2]/10))
                        selection_tokens_filter[2] = selection_tokens_filter[2] + 1
                        selection_tokens_filter[3] = selection_tokens_filter[3] + 15
                        selection_tokens_filter[4] = selection_tokens_filter[4] + 150
                        
            elif(selection_tokens_filter[1] == 'silver'):
                if(selection_tokens_filter[2]%10 == 0):
                    rune_flag = True
                    confirm = disp.custom_yesno(f"Spend {10000*(selection_tokens_filter[2]/10)} points to use {20*(selection_tokens_filter[2]/10)} runes?")
                else:
                    confirm = disp.custom_yesno(f"Spend {3500*selection_tokens_filter[2]} points to upgrade?")
        
                if(confirm == 1):
                    pass
                elif(confirm == 0):
                    continue
                elif(confirm == 2):
                    disp.error("Invalid choice.")
                    continue
                    
                if(rune_flag == False):
                
                    if(points < 3500*selection_tokens_filter[2]):
                        disp.error("Not enough points.")
                        continue
                    else:
                        points = points - 3500*selection_tokens_filter[2]
                        selection_tokens_filter[2] = selection_tokens_filter[2] + 1
                        selection_tokens_filter[3] = selection_tokens_filter[3] + 10
                        selection_tokens_filter[4] = selection_tokens_filter[4] + 75
                        
                elif(rune_flag == True):
                
                    if(points < (10000*(selection_tokens_filter[2]/10))):
                        disp.error("Not enough points.")
                        continue
                    elif(runes < (20*(selection_tokens_filter[2]/10))):
                        disp.error("Not enough runes.")
                        continue
                    else:
                        runes = runes - (20*(selection_tokens_filter[2]/10))
                        points = points - (10000*(selection_tokens_filter[2]/10))
                        selection_tokens_filter[2] = selection_tokens_filter[2] + 1
                        selection_tokens_filter[3] = selection_tokens_filter[3] + 40
                        selection_tokens_filter[4] = selection_tokens_filter[4] + 300
                        
            elif(selection_tokens_filter[1] == 'gold'):
                if(selection_tokens_filter[2]%10 == 0):
                    rune_flag = True
                    confirm = disp.custom_yesno(f"Spend {30000*(selection_tokens_filter[2]/10)} points to use {45*(selection_tokens_filter[2]/10)} runes?")
                else:
                    confirm = disp.custom_yesno(f"Spend {7500*selection_tokens_filter[2]} points to upgrade?")
        
                if(confirm == 1):
                    pass
                elif(confirm == 0):
                    continue
                elif(confirm == 2):
                    disp.error("Invalid choice.")
                    continue
                    
                if(rune_flag == False):
                
                    if(points < 7500*selection_tokens_filter[2]):
                        disp.error("Not enough points.")
                        continue
                    else:
                        points = points - 7500*selection_tokens_filter[2]
                        selection_tokens_filter[2] = selection_tokens_filter[2] + 1
                        selection_tokens_filter[3] = selection_tokens_filter[3] + 35
                        selection_tokens_filter[4] = selection_tokens_filter[4] + 130
                        
                elif(rune_flag == True):
                
                    if(points < (30000*(selection_tokens_filter[2]/10))):
                        disp.error("Not enough points.")
                        continue
                    elif(runes < (45*(selection_tokens_filter[2]/10))):
                        disp.error("Not enough runes.")
                        continue
                    else:
                        runes = runes - (45*(selection_tokens_filter[2]/10))
                        points = points - (30000*(selection_tokens_filter[2]/10))
                        selection_tokens_filter[2] = selection_tokens_filter[2] + 1
                        selection_tokens_filter[3] = selection_tokens_filter[3] + 90
                        selection_tokens_filter[4] = selection_tokens_filter[4] + 750
                        
                        
            elif(selection_tokens_filter[1] == 'platinum'):
                if(selection_tokens_filter[2]%10 == 0):
                    rune_flag = True
                    confirm = disp.custom_yesno(f"Spend {65000*(selection_tokens_filter[2]/10)} points to use {100*(selection_tokens_filter[2]/10)} runes?")
                else:
                    confirm = disp.custom_yesno(f"Spend {12000*selection_tokens_filter[2]} points to upgrade?")
        
                if(confirm == 1):
                    pass
                elif(confirm == 0):
                    continue
                elif(confirm == 2):
                    disp.error("Invalid choice.")
                    continue
                    
                if(rune_flag == False):
                
                    if(points < 12000*selection_tokens_filter[2]):
                        disp.error("Not enough points.")
                        continue
                    else:
                        points = points - 12000*selection_tokens_filter[2]
                        selection_tokens_filter[2] = selection_tokens_filter[2] + 1
                        selection_tokens_filter[3] = selection_tokens_filter[3] + 50
                        selection_tokens_filter[4] = selection_tokens_filter[4] + 200
                        
                elif(rune_flag == True):
                
                    if(points < (65000*(selection_tokens_filter[2]/10))):
                        disp.error("Not enough points.")
                        continue
                    elif(runes < (100*(selection_tokens_filter[2]/10))):
                        disp.error("Not enough runes.")
                        continue
                    else:
                        runes = runes - (100*(selection_tokens_filter[2]/10))
                        points = points - (65000*(selection_tokens_filter[2]/10))
                        selection_tokens_filter[2] = selection_tokens_filter[2] + 1
                        selection_tokens_filter[3] = selection_tokens_filter[3] + 150
                        selection_tokens_filter[4] = selection_tokens_filter[4] + 1100
                        
                        
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
            
            cur.execute(f"update \"siddhanth78/MainGame\".player_info set runes = {runes} where p_id = '{player_id}'")
            cur.execute(f"update \"siddhanth78/MainGame\".player_info set points = {points} where p_id = '{player_id}'")
            cur.execute(f"update \"siddhanth78/MainGame\".player_characters set level = {selection_tokens_filter[2]} where p_id = '{player_id}' and ch_id = '{selection_tokens_filter[5]}'")
            cur.execute(f"update \"siddhanth78/MainGame\".player_characters set attack = {selection_tokens_filter[3]} where p_id = '{player_id}' and ch_id = '{selection_tokens_filter[5]}'")
            cur.execute(f"update \"siddhanth78/MainGame\".player_characters set health = {selection_tokens_filter[4]} where p_id = '{player_id}' and ch_id = '{selection_tokens_filter[5]}'")
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
    