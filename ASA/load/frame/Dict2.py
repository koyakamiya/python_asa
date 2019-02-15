
class Dict2():

    def __init__(self, dic, json):
        self.index = {}
        self.frames = json
        for line in open(dic):
            n = line.strip().split(' ')
            self.index.update({n[0]: (int(n[1]), int(n[2]))})

    def isFrame(self, verb: str) -> bool:
        return verb in self.index

    def getFrame(self, verb):
        frame = None
        if self.isFrame(verb):
            for ins in self.frames['dict']:
                if ins['verb'] == verb:
                    frame = ins['frame']
                    break
        return frame
