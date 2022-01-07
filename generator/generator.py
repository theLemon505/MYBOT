import json

def init_generator():
    print('initializing bot generator')
    text = input("please enter generation command: ")
    if text == "create new bot":
        params = {}
        params.update({"name":input("please enter the new bots name: ")})
        params.update({"type":input("please enter the new bots type: ")})
        input_layer = int(input("please enter number of input nurons: "))
        hidden_layers = []
        layers = int(input("please enter number of hidden layers: "))
        for layer in layers:
            hidden_layers.append(int(input("please enter number of hidden layer " + layer + " nurons")))
        output_layer = int(input("please enter number of output nurons: "))
        params.update({"nurons":{"input":input_layer}})
        params.append({"nurons":{"hidden":hidden_layers}})
        params.append({"nurons":{"output":output_layer}})
        create_bot(params)

def create_bot(params):
    print('creating new bot')
    bot_file = open(params["name"] + ".json", "x")    
    json_object = json.dumps(params, indent = 4) 
    bot_file.write(json_object)