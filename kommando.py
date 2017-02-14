commands = {}
with open("commands.csv") as f:
    for line in f:
       (key, val) = line.split(",")
       commands[str(key)] = val
def kommando_check(key):
	if key.startswith('!commands'):
		msg = "Available commands are: " + alla_kommando()
		return msg
	elif key in commands:
		return commands[key]
	else:
		return "That is not a valid command. See !commands"

def alla_kommando():
	kommandon = []
	for key in commands:
		kommandon.append(str(key))
	return str(kommandon)