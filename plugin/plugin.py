import tensorflow as tf
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import json
from .trainer import Trainer
import pickle

def init_plugin():
    f = input("please enter the path to the bot's json file: ")
    bot_file = open(f)
    bot_json = json.load(bot_file)
    print("loading " + bot_json["name"] + "...")
    train = input("would you like to train your bot's nlp? (y/n):")
    if train == "y":
        data_set_path = input("please enter path to the training data set (this should be an intents file in json format): ")
        data_set = open(data_set_path)
        data = json.load(data_set)
        write_json(data, f)
        print("training...")
        Trainer(json.loads(open(f).read()), ["!",".","?",","])
    elif train == "n":
        chat(bot_json)

def chat(json_data):
    print("chat with " + json_data["name"])
    lemmatizer = WordNetLemmatizer()
    intents = json_data["intents"]
    words = pickle.load(open("words.pkl", "rb"))
    classes = pickle.load(open("classes.pkl", "rb"))
    model = load_model("speech.model")

def write_json(new_data, filename):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["intents"] = new_data["intents"]
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def create_nural_network(layers):
    pass
