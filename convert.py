# import pandas as pd 
# import json
# data = pd.read_csv('mask_generations/Hartebeest.csv') 
# data.rename(columns={"HORNS                     Material": "a", "B": "c"})


#     token["attributes"].append(getAttribute("HORNS",i["HORNS                     Material"])),
#     token["attributes"].append(getAttribute("MASK",i["MASK                     Material"])),
#     token["attributes"].append(getAttribute("IMMORTALITY",i["IMMORTALITY                     Name"])),
#     token["attributes"].append(getAttribute("LABYRINTH",i["LABYRINTH                     Name"])),
#     token["attributes"].append(getAttribute("CHIP",i["CHIP                     Name"])),
#     token["attributes"].append(getAttribute("LIGHT",i["LIGHT                     Name"])),
# "FEATHERS",i["FEATHERS                     Material"])),

# data.head()

# data = data.drop(['Unnamed: 0'], axis=1) 
# data = data.drop(['Unnamed: 3'], axis=1) 
# data = data.drop(['Unnamed: 4'], axis=1) 
# data = data.drop(['HORNS Odds (% chance)'],axis=1)
# data = data.drop(['HORNS: Total Tickets'],axis=1)
# data = data.drop(['HORNS Tickets'],axis=1)
# data = data.drop(['MASK Odds (% chance)'],axis=1)
# data = data.drop(['MASK: Total Tickets'],axis=1)
# data = data.drop(['MASK Tickets'],axis=1)
# data = data.drop(['MASK Name'],axis=1)
# data = data.drop(['MASK ACCESSORIES Material'],axis=1)
# data = data.drop(['MASK ACCESSORIES Tickets'],axis=1)
# data = data.drop(['MASK ACCESSORIES: Total Tickets'],axis=1)
# data = data.drop(['MASK ACCESSORIES Odds (% chance)'],axis=1)
# data = data.drop(['CHIP LAYERS Name'],axis=1)
# data = data.drop(['CHIP LAYERS Material'],axis=1)
# data = data.drop(['CHIP LAYERS Tickets'],axis=1)
# data = data.drop(['CHIP LAYERS: Total Tickets'],axis=1)
# data = data.drop(['CHIP LAYERS Odds (% chance)'],axis=1)
# data = data.drop(['CHIPS Material'],axis=1)
# data = data.drop(['CHIPS Tickets'],axis=1)
# data = data.drop(['CHIPS: Total Tickets'],axis=1)
# data = data.drop(['CHIPS Odds (% chance)'],axis=1)
# data = data.drop(['IMMORTALITY Tickets'],axis=1)
# data = data.drop(['IMMORTALITY: Total Tickets'],axis=1)
# data = data.drop(['IMMORTALITY Odds (% chance)'],axis=1)
# data = data.drop(['LABYRINTH Tickets'],axis=1)
# data = data.drop(['LABYRINTH: Total Tickets'],axis=1)
# data = data.drop(['LABYRINTH Odds (% chance)'],axis=1)
# data = data.drop(['BOTTOM FEATHER ROPES Name'],axis=1)
# data = data.drop(['BOTTOM FEATHER ROPES Material'],axis=1)
# data = data.drop(['BOTTOM FEATHER ROPES Tickets'],axis=1)
# data = data.drop(['BOTTOM FEATHER ROPES: Total Tickets'],axis=1)
# data = data.drop(['BOTTOM FEATHER ROPES Odds (% chance)'],axis=1)
# data = data.drop(['TOP-BOTTOM FEATHERS Name'],axis=1)
# data = data.drop(['TOP-BOTTOM FEATHERS Material'],axis=1)
# data = data.drop(['TOP-BOTTOM FEATHERS Tickets'],axis=1)
# data = data.drop(['TOP-BOTTOM FEATHERS: Total Tickets'],axis=1)
# data = data.drop(['TOP-BOTTOM FEATHERS Odds (% chance)'],axis=1)
# data = data.drop(['COILED BEAD ROPES Name'],axis=1)
# data = data.drop(['COILED BEAD ROPES Material'],axis=1)
# data = data.drop(['COILED BEAD ROPES Tickets'],axis=1)
# data = data.drop(['COILED BEAD ROPES: Total Tickets'],axis=1)
# data = data.drop(['COILED BEAD ROPES Odds (% chance)'],axis=1) 
# data = data.drop(['STANDARD BEAD STRINGS Tickets'],axis=1) 
# data = data.drop(['STANDARD BEAD STRINGS Name'],axis=1) 
# data = data.drop(['STANDARD BEAD STRINGS Material'],axis=1) 
# data = data.drop(['STANDARD BEAD STRINGS: Total Tickets'],axis=1) 
# data = data.drop(['STANDARD BEAD STRINGS Odds (% chance)'],axis=1) 
# data = data.drop(['RARE BEAD STRINGS Name'],axis=1) 
# data = data.drop(['RARE BEAD STRINGS Material'],axis=1) 
# data = data.drop(['RARE BEAD STRINGS Tickets'],axis=1) 
# data = data.drop(['RARE BEAD STRINGS: Total Tickets'],axis=1) 
# data = data.drop(['RARE BEAD STRINGS Odds (% chance)'],axis=1) 
# data = data.drop(['STANDARD BEADS Name'],axis=1) 
# data = data.drop(['STANDARD BEADS Material'],axis=1) 
# data = data.drop(['STANDARD BEADS Tickets'],axis=1) 
# data = data.drop(['STANDARD BEADS: Total Tickets'],axis=1)
# data = data.drop(['STANDARD BEADS Odds (% chance)'],axis=1) 
# data = data.drop(['RARE BEADS Material'],axis=1) 
# data = data.drop(['RARE BEADS Tickets'],axis=1) 
# data = data.drop(['RARE BEADS: Total Tickets'],axis=1) 
# data = data.drop(['RARE BEADS Odds (% chance)'],axis=1) 
# data = data.drop(['HORN ROPES Name'],axis=1) 
# data = data.drop(['HORN ROPES Material'],axis=1) 
# data = data.drop(['HORN ROPES Tickets'],axis=1) 
# data = data.drop(['HORN ROPES: Total Tickets'],axis=1) 
# data = data.drop(['HORN ROPES Odds (% chance)'],axis=1) 

# data1 = data.to_json(r'v1.2.json',orient='records') 
# print(data1) 

# IMAGES_BASE_URI = 'ipfs://' 
# PROJECT_NAME = 'Mask'




# def getAttribute(key,value):
#     return{
#         "trait_type":key,
#         "value":value
#     }
    ###### DAO
# for i in range (0,7110):
#     token_id= i 
#     token = {
#         "name": PROJECT_NAME + '#' + str(token_id),
#         "image": "ipfs://",,
#         "description": "descript inscribe and everything else "
#     } 
#     # token["attributes"].append(getAttribute("DAO",100))
#     with open('./metadata/MASK/'+ st(token_id), 'w') as outfile:
#         json.dump(token,outfile,indent=4)

import pandas as pd 
import json
import os


csv = input('input the csv file: ')

if csv == 'hartebeast-top':
    data = pd.read_csv('Hartebeast-top/mask_generations/{}.csv'.format(csv)) 
    data1 = data.to_json(r'v1.2.json',orient='records') 
    print(data1)
    f = open('hartebeast-top/v1.2.json') 
    data = json.load(f) 

    IMAGES_BASE_URI = 'ipfs://{}'
    PROJECT_NAME = 'Initiate Hartebeast Top Feathers Mask ' 

    def getAttribute(key,value):
        return{
            "trait_type":key[:17],
            "value":value[:18]
        } 

    for i in data:
        token_id =i['                    '][5:]
        token = {
            "image":IMAGES_BASE_URI +str(token_id) + '.glb',
            "tokenId":token_id,
            "name": PROJECT_NAME +'#'+str(token_id),
            "attributes": []
        }
        token["attributes"].append(getAttribute("MASK","HARTEBEAST")),
        token["attributes"].append(getAttribute("CULTURE","Native American")),
        # token["attributes"].append(getAttribute("TEXTURES",i["MASK                     Material"])),
        token["attributes"].append(getAttribute("HORNS TEXTURE",i["HORNS                     Material"])),
        token["attributes"].append(getAttribute("MASK TEXTURE",i["MASK                     Material"])),
        token["attributes"].append(getAttribute("IMMORTALITY",i["IMMORTALITY                     Name"])),
        token["attributes"].append(getAttribute("LABYRINTH",i["LABYRINTH                     Name"])),
        token["attributes"].append(getAttribute("CHIP",i["CHIP                     Name"])),
        token["attributes"].append(getAttribute("LIGHT",i["LIGHT                     Name"])),
        token["attributes"].append(getAttribute("FEATHERS",i["FEATHERS                     Material"])),
        with open('mask_json/Hartebeast-top_' + str(token_id), 'w') as outfile:
            json.dump(token,outfile,indent=4) 
    f.close()



if csv == 'hartebeast-plain':
    data = pd.read_csv('Hartebeast-plain/mask_generations/{}.csv'.format(csv)) 
    data1 = data.to_json(r'v1.2.json',orient='records') 
    print(data1)
    f = open('hartebeast-plain/v1.2.json') 
    data = json.load(f) 

    IMAGES_BASE_URI = 'ipfs://{}'
    PROJECT_NAME = 'Initiate Mask ' 

    def getAttribute(key,value):
        return{
            "trait_type":key[:17],
            "value":value[:18]
        } 

    for i in data:
        token_id =i['Unnamed: 0'][5:]
        token = {
            "image":IMAGES_BASE_URI +str(token_id) + '.glb',
            "tokenId":token_id,
            "name": PROJECT_NAME +'#'+str(token_id),
            "attributes": []
        }


        token["attributes"].append(getAttribute("HORNS                                                      Material",i["HORNS                                                      Material"])),
        token["attributes"].append(getAttribute("MASK                                                           Material",i["MASK                                                           Material"])),
        token["attributes"].append(getAttribute("IMMORTALITY                                                    Name",i["IMMORTALITY                                                    Name"])),
        token["attributes"].append(getAttribute("LABYRINTH                                                      Name",i["LABYRINTH                                                      Name"])),
        token["attributes"].append(getAttribute("LIGHTS                                                         Name",i["LIGHTS                                                         Name"])),
        # token["attributes"].append(getAttribute("",i[""])),
        # token["attributes"].append(getAttribute("",i[""])),



        with open('mask_json/Hartebeast-Plain_' + str(token_id), 'w') as outfile:
            json.dump(token,outfile,indent=4) 
    f.close()


if csv == 'kitsune':
    data = pd.read_csv('kitsune/mask_generations/{}.csv'.format(csv)) 
    data1 = data.to_json(r'v1.2.json',orient='records') 
    print(data1)
    f = open('kitsune/v1.2.json') 
    data = json.load(f) 

    IMAGES_BASE_URI = 'ipfs://{}'
    PROJECT_NAME = 'Kitsune Mask ' 

    def getAttribute(key,value):
        return{
            "trait_type":key[:17],
            "value":value[:18]
        } 

    for i in data:
        # directory_path = 'mask_json/'
        token_id =i['Unnamed: 0'][5:] 
        token = {
            "image":IMAGES_BASE_URI +str(token_id) + '.glb',
            "tokenId":token_id ,
            "name": PROJECT_NAME +'#'+str(token_id),
            "attributes": []
        }
        # token["attributes"].append(getAttribute("HORNS                                                      Material",i["HORNS                                                      Material"])),
        token["attributes"].append(getAttribute("MASK Material",i["MASK Material"])),
        token["attributes"].append(getAttribute("IMMORTALITY                                                     Name",i["IMMORTALITY                                                     Name"])),
        token["attributes"].append(getAttribute("LABYRINTH                                                       Name",i["LABYRINTH                                                       Name"])),
        token["attributes"].append(getAttribute("LIGHTS                                                          Name",i["LIGHTS                                                          Name"])),
        # token["attributes"].append(getAttribute("",i[""])),
        # token["attributes"].append(getAttribute("",i[""])),
        # token["attributes"].append(getAttribute("",i[""])),
        with open('mask_json/Kitsune_' + str(token_id), 'w') as outfile:
            json.dump(token,outfile,indent=4) 
    f.close()
    
else:
    print('Mask not yet added to collection for metadata, contact ZOMBIE')





    
