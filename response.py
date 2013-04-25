import json, os, sys


class SimpleResponse:
    commands = {}
    filename = ''

    built_ins = ['add', 'delete', 'modify', 'help']

    def __init__(self):
        self.filename = os.path.join(os.path.split(__file__)[0], "responses.json")
        if not os.path.exists(self.filename):
            self.save()
        if '%s%s' % (sys.version_info[0], sys.version_info[1]) == '25':
            self.commands = json.read(open(self.filename).read())
        else:
            self.commands = json.load(open(self.filename))

    def has_response(self, command):

        split_command = [command.partition(" ")[0].lower(), command.partition(" ")[2]]

        if split_command[0] in self.built_ins or split_command[0] in self.commands:
            return True

        return False

    def get_response(self, command, speaker, is_mod):

        split_command = [command.partition(" ")[0].lower(), command.partition(" ")[2]]

        if split_command[0] == 'help':
            return self.help()

        if split_command[0] in self.built_ins:
            if not is_mod:
                return "You are not allowed to use this command"
            else:
                if split_command[0] == 'add':
                    return self.add(split_command[1].partition(" ")[0].lower(), split_command[1].partition(" ")[2])
                if split_command[0] == 'delete':
                    return self.delete(split_command[1].lower())
                if split_command[0] == 'modify':
                    return self.modify(split_command[1].partition(" ")[0].lower(), split_command[1].partition(" ")[2])

        return self.commands[split_command[0]].replace(':speaker', speaker)

    def add(self, command, response):
        if command in self.commands:
            return "!%s already exists" % (command)

        self.commands[command] = response
        self.save()

        return "!%s added." % (command)

    def modify(self, command, response):
        if command not in self.commands:
            return "!%s does not exist" % (command)

        self.commands[command] = response
        self.save()

        return "!%s edited." % (command)

    def delete(self, command):
        if command not in self.commands:
            return "!%s does not exist" % (command)

        del self.commands[command]
        self.save()

        return "!%s deleted." % (command)

    def save(self):
        fp = open(self.filename,  "w")
        if '%s%s' % (sys.version_info[0], sys.version_info[1]) == '25':
            fp.write(json.write(self.commands))
        else:
            fp.write(json.dumps(self.commands, sort_keys=True,
...                  indent=4, separators=(',', ': ')))
        fp.close()

    def help(self):
        mergedlist = self.built_ins + self.commands.keys()

        return "Possible commands: !%s" % (", !".join(sorted(mergedlist)))
