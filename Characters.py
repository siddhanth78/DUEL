import os
import os.path
import bitdotio
import display_module as disp
import nltk.tokenize as tokenize

#-----------------------------------------------------------------------------------

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

b = bitdotio.bitdotio(api) #establish connection using API key

conn = b.get_connection() #connect to db
cur = conn.cursor() #cursor

char_list = [] #characters list

char_info = [] #player's character info
names_and_ranks = [] #player's characters' names and ranks

upgrades = {}

bronze_chars = [] #bronze characters
silver_chars = [] #silver characters
gold_chars = [] #gold characters
platinum_chars = [] #platinum characters

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

    if(x[1] == "bronze"):
        bronze_chars.append(x)
    elif(x[1] == "silver"):
        silver_chars.append(x)
    elif(x[1] == "gold"):
        gold_chars.append(x)
    elif(x[1] == "platinum"):
        platinum_chars.append(x)
        
    disp.box(title = x[0],
            m = f"Rank: {x[1]}\nAttack: {x[2]}\nHealth: {x[3]}")
            
print("Your characters ^^^")
    
while True:
    print(menu)
    choice = input("Enter your choice: ")
    
    if(choice == '1'):
        b = bitdotio.bitdotio(api)
        conn = b.get_connection()
        cur = conn.cursor()
        disp.warn("Search is case-sensitive.")
        
        while True:
            b = bitdotio.bitdotio(api)
            conn = b.get_connection()
            cur = conn.cursor()
            search = input("Enter <field> <query> (Enter 'quit' to exit search): ")
            
            if(search.lower() == 'quit'):
                print()
                break
                
            tokens = tokenize.word_tokenize(search)
            searchlist = []
            name_and_rank_list = []
            all_info = []
            results = []
            
            b = bitdotio.bitdotio(api)
            conn = b.get_connection()
            cur = conn.cursor()
        
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
    
        char_menu_options = []
    
        for x in char_info:
            char_menu_options.append(f"{x[0]} [Rank: {x[1]}] <Current Stats: [Atk: {x[2]}] [Hlth: {x[3]}] [Lvl: {x[4]}]>")
            
        for i in range(0, len(char_menu_options)):
            upgrades[str(i+1)] = char_menu_options[i]
    
        char_menu = disp.menu("Your characters",
                                char_menu_options, 1)
        
        while True:
            print(char_menu)
            upgrade_choice = input("Enter your choice: ")
            
            if(upgrade_choice not in upgrades.keys()):
                disp.error("Invalid choice.")
                continue
                
            selection = upgrades[upgrade_choice]
            selection_tokens = tokenize.word_tokenize(selection)
            selection_tokens_filter = [selection_tokens[0], selection_tokens[4], int(selection_tokens[13]), int(selection_tokens[18]), int(selection_tokens[23])]
            
            break
            
        
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
    