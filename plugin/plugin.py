import json

def init_plugin():
    bot_file = open(input("please enter the path to the bot's json file: "))
    bot_json = json.load(bot_file)
    create_nural_network(bot_json["layers"])

def create_nural_network(layers):
    pass