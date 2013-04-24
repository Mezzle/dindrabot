import json, os, sys

class UserManager():
    names = {}
    filename = ''

    def __init__(self):
        self.filename = os.path.join(os.path.split(__file__)[0], "names")
        if not os.path.exists(self.filename):
            self.save()

        if '%s%s' % (sys.version_info[0], sys.version_info[1]) == '25':
            self.names = json.read(open(self.filename).read())
        else:
            self.names = json.load(open(self.filename))

    def is_registered(self, nick):
        return nick in self.names

    def register(self, nick, email):
        self.names[nick] = email;

        self.save()

    def get_email(self, nick):
        if self.is_registered(nick):
            return self.names[nick]
        else:
            return None
        
    def save(self):
        fp = open(self.filename,  "w")
        if '%s%s' % (sys.version_info[0], sys.version_info[1]) == '25':
            fp.write(json.write(self.names))
        else:
            fp.write(json.dumps(self.names))
        fp.close()

