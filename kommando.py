# -*- coding: utf-8 -*-
commands = {}
#Remember to set definitive path
with open("/usr/local/src/sthlmesport-bot/commands.csv") as f:
    for line in f:
        if line.find(","):
            (key, val) = line.split(",",1)
            commands[str(key)] = val
def kommando_check(message,is_admin):
    if message.startswith('!commands'):
        msg = "Available commands are: " + alla_kommando()
        return msg
    if message.lower().startswith('!add') and is_admin == True:
        #Example: !add !newcommand,meddelande med mellanslag
        if message.lower() == "!add":
            return "The add command works like this example: !add !command_name, Message you want"
        else:
            message = message[5:]
            key1, key2 = message.split(",",1)
            key1 = key1.lower()
            key2 = key2.lstrip(' ')
            #Make sure commands.csv is targetted!
            if key1 not in commands:
                file = open("commands.csv", "a")
                file.write(key1 + "," + key2 + "\n")
                file.close()
                #add to dict
                commands[key1] = key2
                return "The command " + key1 + " was successfully added!"
            else:
                return "The command " + key1 + " already exists!"
    elif message.lower().startswith('!remove') and is_admin == True:
        if message.lower() == "!remove":
            return  "The remove command works like this example: !remove !command_name"
        else:
            key1, key2 = message.split(" ")
            if key2 not in commands:
                return "The command does not exist"
            else:
                commands.pop(key2, None)
                file = open("commands.csv", "w")
                for key in commands:
                    writer = (key + "," + commands.get(key)).strip("\n")
                    file.write(writer + "\n")
                file.close()
                return "The command " + key2 + " has been removed"
    elif (message.lower().startswith('!add') or message.lower().startswith('!remove')) and is_admin == False:
        return "Sorry only Admins can do that!"
    elif message in commands:
        return commands[message]
    else:
        return "That is not a valid command. See !commands"

def alla_kommando():
    kommandon = []
    for message in commands:
        kommandon.append(str(message))
    return str(kommandon)
