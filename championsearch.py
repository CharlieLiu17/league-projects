import requests
import json
from googleapiclient.discovery import build
import webbrowser
import config

def spell_switch(spell):
    return {
        'q': '0',
        'w': '1',
        'e': '2',
        'r': '3',
    }.get(spell, '0')

def store_and_print(spells, spells_parsed):
    i = 0
    for num in spells:  
        spells_parsed[str(i)] = num.get("cooldownBurn")
        print(num.get("name") + " cooldown:\n  " + num.get("cooldownBurn"))
        i += 1

api_key = config.api_key
running = True
patch = "12.10.1" 
champions = requests.get("http://ddragon.leagueoflegends.com/cdn/" + patch + "/data/en_US/champion.json")
champions.json

while (running):
    spells_parsed = {}
    spells_parsed_one = {}

    my_champ = input("Your Champion Name: ")
    my_champ = my_champ.lower().title().replace(" ", "")
    enemy_champ = input("The Enemy Champion Name: ")
    enemy_champ = enemy_champ.lower().title().replace(" ", "")
    my_ability_input = input("Which ability for my champion do I want to look at? ").lower()
    enemy_ability_input = input("Which ability for the enemy champion do I want to look at? ").lower()
    running = False
    if (enemy_champ in champions.json().get("data")):
        champion_data = requests.get("http://ddragon.leagueoflegends.com/cdn/"+patch+"/data/en_US/champion/" + enemy_champ + ".json")
        spells = champion_data.json().get("data").get(enemy_champ).get("spells")
        print(isinstance(spells, list))
        store_and_print(spells, spells_parsed)

        if (my_champ in champions.json().get("data")):
            champion_data_one = requests.get("http://ddragon.leagueoflegends.com/cdn/"+patch+"/data/en_US/champion/" + my_champ + ".json")
            print(my_champ)
            spells = champion_data_one.json(    ).get("data").get(my_champ).get("spells")
            
            store_and_print(spells, spells_parsed_one)
    else:
        print("Sorry, either you input invalid champion name(s), or our parsing is shit")
        break
        
    
    #print(spells_parsed)
    enemy_ability = spells_parsed.get(spell_switch(enemy_ability_input)).split("/")   #list
    my_ability = spells_parsed_one.get(spell_switch(my_ability_input)).split("/")     #list
    i = 0
    print("\nDifference between key cooldowns of " + enemy_champ + "'s " + enemy_ability_input + " and " + my_champ + "'s " + my_ability_input + " is:")
    while (i < len(enemy_ability) or i < len(my_ability)):
        if (i < len(enemy_ability)):
            enemy_result = float(enemy_ability[i])
        else:
            enemy_result = float(enemy_ability[0])
        if (i < len(my_ability)):
            my_result = float(my_ability[i])
        else:
            my_result = float(my_ability[0])
        print("  " + str(abs(enemy_result - my_result)) + "/", end='')
        i += 1
    print("\n")

    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(q=my_champ + " vs " + enemy_champ, part="snippet", type="video", videoDefinition="high")

    response = request.execute()
    video_id = response.get("items")[0].get("id").get("videoId")
    print(video_id)
    webbrowser.open('https://www.youtube.com/watch?v=' + str(video_id))
    webbrowser.open('https://na.op.gg/champion/' + my_champ)


    # video_request = youtube.videos().list(
    #     part = "snippet",
    #     maxResults = "1",
    #     id = video_id
    # )
    # response = video_request.execute()
    # print(response)
    
    
    

        

    
    



