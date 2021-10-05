import os
import yaml

YML_PATH = "./cmd.yml"


class StartParser:
    def __init__(self):
        f = open(YML_PATH)
        self.CmdSet = yaml.load(f, Loader=yaml.FullLoader)
        self.Key = 'quit'
        f.close()

    def __Parse__(self):
        flag = False
        for obj in self.CmdSet.values():
            if self.Key in obj['keyword']:
                flag = True
                for cmd in obj['cmd']:
                    print(cmd)
                    os.system(cmd)
        return flag

    def apply(self):
        self.Key = input(
            "======================================\n"
            "          what you wanna do\n"
            "======================================\n"
        )
        while not self.__Parse__():
            self.Key = input(
                "Wrong Input!\n"
                "See " + os.path.abspath(YML_PATH) + " for more input detail\n"
                "Please enter again (\"exit\" to quit)\n"
            )


def yaml_test():
    f = open("./resource/cmd.yml")
    key = 'vc'
    CmdSet = yaml.load(f, Loader=yaml.FullLoader)
    for obj in CmdSet.values():
        if key in obj['keyword']:
            for cmd in obj['cmd']:
                print(cmd)
                os.system(cmd)
    f.close()

if __name__ == '__main__':
    f = open("./config.yml")
    config = yaml.load(f, Loader=yaml.FullLoader)
    if 'YML_PATH' in config.keys():
        YML_PATH = os.path.abspath(config['YML_PATH'])
    f.close()
    parser = StartParser()
    parser.apply()
