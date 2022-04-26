import os
import os.path
import bitdotio
import display_module as disp
import random
import keyboard

#-----------------------------------------------------------------------------------

api = "3drdz_rgsnUgWm8bUjMzT5enE3Kdv"

b = bitdotio.bitdotio(api) #establish connection using API key

conn = b.get_connection() #connect to db
cur = conn.cursor() #cursor

#-----------------------------------------------------------------------------------

print("Vulcan was once a barren land.")
print("Many civilizations have been wiped out by the super volcano that stands tall in the middle of the island.")
print("Every 10000 years, the volcano erupts and engulfs the entire area, leaving no survivors.")
print("Nine mass volcanic events have occurred.")
print("Then came along the Society of Engineers.\nPress 'enter' to continue.\n")

keyboard.wait('enter')

print("The origins of this civilization remains unknown, but there are traces of them that lead back to before the sixth mass volcanic event.")
print("They were experts in harvesting resources from abundant and obscure sources alike, and are masters of crafting.")
print("The engineers had learnt to extract minerals and other materials from the volcano and regions surrounding it.")
print("This resulted in the volcano going permanently dormant, with mass volcanic events no more.")
print("200000 years had passed, and they lived in peace and only continued growing.")
print("Then, the unimaginable happened.\nPress 'enter' to continue.\n")

keyboard.wait('enter')

print("Th volcano erupted.")
print("Because of the resource harvesting, the eruption was not too destructive, but it did result in several lives being lost.")
print("Mage, the leader of the society, called for a council.")
print("Among the council members was one intelligent and ambitious, but rebellious, egoistic and ill-tempered man.")
print("His name was Nexus.\nPress 'enter' to continue.\n")

keyboard.wait('enter')

print("Nexus began to doubt the capabilities of the newer generation of engineers as the volcanic event killed thousands.")
print("He raised his voice against Mage, staring down into her soul with his eyes blood-red and filled with tears.")
print("Nexus revealed that his family was killed in the event.")
print("Mage gave him her condolences, but Nexus refused to listen.")
print("He stormed out of the council, and was never seen since.")
print("Many years passed. A search party was sent out. But, nobody found him.")
print("Mage eventually called it off.")
print("The very next day, a device was set off at the headquarters of the society. The device exploded and destroyed the entire island.")
print("Now, Vulcan is a historical site.")
print("To this day, it remains a mystery as to what happened to Nexus and the Society of Engineers.\nPress 'enter' to continue.\n")

keyboard.wait('enter')

print("We are now the fourth generation of post-Vulcan engineers.")
print("Although we craft on Ptorin, our headquarters remain hidden so that even if our island is wiped, the headquarters will still exist.")
print("To save time rebuilding, of course.")
print("The council now only intervenes during major events, if you were wondering all these years why you've never seen a member.")
print("Alright, get back to work now. Oh wait, you don't have a job here. My bad, hahahaha!\nPress 'enter' to continue.\n")

keyboard.wait('enter')