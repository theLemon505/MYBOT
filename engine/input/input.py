def put(data):
    pass

bot = None

def await_data():
    text_data = input("enter command: ")
    if text_data != None:
        if text_data == "process-raw-data":
            data = input("please enter the direct path to the test data file: ")
            put(open(data))
        if text_data == "create-new-bot":
            params = {}
            params.update({"name":input("please enter bots name: ")})
            params.update({"type":input("please enter bots type: ")})
            bot = create_new_bot(params)

def create_new_bot(params):
    bot_file = open(params["name"]+".bot", "x")
    bot_file.write(params)
    return bot_file