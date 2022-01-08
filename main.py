from generator.generator import init_generator
from plugin.plugin import init_plugin

if __name__ == "__main__":
    text = input("please enter initialization command: ")
    if text == "generate":
        init_generator()
        print("entering plugin")
        init_plugin()
    elif text == "plugin":
        init_plugin()
        init_plugin()