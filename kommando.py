commands = {}
with open("commands.csv") as f:
    for line in f:
       (key, val) = line.split(",")
       commands[str(key)] = val
def kommando_check(key):
    if key.startswith('!commands'):
        msg = "Available commands are: " + alla_kommando()
        return msg
    if key.startswith('!add'):
        #Example: !add !newcommand,meddelande med mellanslag
        if key == "!add":
            return "The add command works like this example: !add !command_name, Message you want"
        else:
            key = key[5:]
            key1, key2 = key.split(",")
            key1 = key1.lower()
            #Make sure commands.csv is targetted!
            if key1 not in commands:
                file = open("commands.csv", "a")
                file.write( "\n" + key1 + "," + '"%s"'%key2)
                file.close()
                #add to dict
                commands[key1] = key2
                return "The command " + key1 + " was successfully added!"
            else:
                return "The command " + key1 + " already exists!"
    elif key in commands:
        return commands[key]
    else:
        return "That is not a valid command. See !commands"

def alla_kommando():
    kommandon = []
    for key in commands:
        kommandon.append(str(key))
    return str(kommandon)