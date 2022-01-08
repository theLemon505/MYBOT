import json
import os

def init_generator():
    print('initializing bot generator')
    text = input("please enter generation command: ")

    if text == "create new bot":
        params = {}
        params.update({"name":input("please enter the new bots name: ")})
        params.update({"type":input("please enter the new bots type: ")})
        input_layer = int(input("please enter number of input nurons: "))
        hidden_layers = []
        layers = int(input("please enter numb.r of hidden layers: "))
        for i in range(layers):
            hidden_layers.append(int(input("please enter number of hidden layer " + str(i + 1) + " nurons: ")))
        output_layer = int(input("please enter number of output nurons: "))
        params.update({"layers":{}})
        params["layers"].update({"input":input_layer})
        params["layers"].update({"hidden":hidden_layers})
        params["layers"].update({"output":output_layer})
        params.update({"intents":{}})
        create_bot(params)

    if text == "update bot":
        f = input("please enter path to the bots json file: ")
        bot_file = json.load(open(f))
        params = open(f, "r")
        changes = input("please enter the parameter youd like to change: ")
        if bot_file[changes] != None:
            bot_file[changes]
            bot_file[changes] = input("please enter the values youd like to update: ")
            json.dump(bot_file, open(f, "w"), indent=4)
            print("updating bot")

def create_bot(params):
    print('creating new bot')
    os.mkdir(params["name"])
    bot_file = open(params["name"] + "/" + params["name"] + ".json", "x")    
    json_object = json.dumps(params, indent = 4) 
    bot_file.write(json_object)
