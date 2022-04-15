import os
import os.path
import time
import bitdotio
import display_module as disp
import nltk.tokenize as tokenize

#-----------------------------------------------------------------------------------

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

b = bitdotio.bitdotio(api) #establish connection using API key

conn = b.get_connection() #connect to db
cur = conn.cursor() #cursor

char_list = [] #characters list

path = os.getcwd() #current working dir

options = ['Search', 'Buy', 'Exit'] #menu options

menu = disp.menu(title = "Main Menu",
                items = options,
                reuse = 1
                    )       #main menu

#-----------------------------------------------------------------------------------
os.system('cls')

cur.execute(f"select name, rank, attack, health from \"siddhanth78/MainGame\".characters")

for x in cur.fetchall():
    char_list.append(x)

for x in char_list:
    disp.box(title = x[0],
            m = f"Rank: {x[1]}\nAttack: {x[2]}\nHealth: {x[3]}")
            

print("Characters ^^^")

while True:
    print(menu)
    choice = input("Enter your choice: ")
    
    if(choice == "1"):
        disp.warn("Search is case-sensitive.")
        
        while True:
            search = input("Enter <field> <query> (Enter 'quit' to exit search): ")
            
            if(search.lower() == 'quit'):
                print()
                break
                
            tokens = tokenize.word_tokenize(search)
            searchlist = []
        
            if(tokens[0].lower() == "name" or tokens[0].lower == "rank"):
                cur.execute(f"select name, rank, attack, health from \"siddhanth78/MainGame\".characters where name like '%{tokens[1]}%'")
            else:
                disp.error("Invalid field.\nValid fields: name, rank")
                continue
        
            for x in cur.fetchall():
                searchlist.append(x)
            
            if(searchlist == []):
                print("No results found.\n")
                continue
            
            for x in searchlist:
                disp.box(title = x[0],
                        m = f"Rank: {x[1]}\nAttack: {x[2]}\nHealth: {x[3]}")
                    
    elif(choice == "2"):
        print("COMING SOON\n")
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

