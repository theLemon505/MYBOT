import json
import random
import numpy as np
import pickle

import nltk
from nltk.stem import WordNetLemmatizer


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


class Trainer:
    def __init__(self, json_data, ignore):
        self.lemmatizer = WordNetLemmatizer()
        self.intents = json_data["intents"]
        self.words = []
        self.classes = []
        self.documents = []
        self.ignore_letters = ignore

        for intent in self.intents:
            for pattern in intent["patterns"]:
                word_list = nltk.word_tokenize(pattern)
                self.words.extend(word_list)
                self.documents.append((word_list, intent["tag"]))
                if intent["tag"] not in self.classes:
                    self.classes.append(intent["tag"])
        
        self.words = [self.lemmatizer.lemmatize(word) for word in self.words if word not in self.ignore_letters]
        self.words = sorted(set(self.words))
        

        self.classes = sorted(set(self.classes))

        pickle.dump(self.words, open("words.pkl", "wb"))
        pickle.dump(self.words, open("classes.pkl", "wb"))

        training = []
        ouput_empty = [0] * len(self.classes)
        
        for document in self.documents:
            bag = []
            word_patterns = document[0]
            word_patterns = [self.lemmatizer.lemmatize(word.lower) for word in word_patterns]

            for word in self.words:
                bag.append(1) if word in word_patterns else bag.append(0)

            output_row = list(ouput_empty)
            output_row[self.classes.index(document[1])] = 1
            training.append([bag, output_row])

        random.shuffle(training)
        training = np.array(training)

        train_x = list(training[:, 0])
        train_y = list(training[:, 1])

        model = Sequential()   
        layers = json_data["layers"]
        input_layer = layers["input"]
        hidden_layers = layers["hidden"]
        model.add(Dense(input_layer, input_shape=(len(train_x[0])), activation="relu"))
        model.add(Dropout(0.5))
        for layer in hidden_layers:
            model.add(Dense(hidden_layer[layer]))