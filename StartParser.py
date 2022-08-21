from os import system, walk
from os.path import abspath, join as pathJoin
import yaml


def find_all_link_file(base):
    for root, ds, fs in walk(base):
        for f in fs:
            if f.endswith('.lnk'):
                fullname = pathJoin(root, f)
                yield fullname


class StartParser:
    def __init__(self, cmd_path, link_path):
        self.CmdSet = {}
        self.link_path = link_path
        self.cmd_path = cmd_path
        self.Key = 'quit'

        self.__getLink__()
        self.__load_cmdyml__()

        # print(self.CmdSet)

    def add_cmd_list(self, keyword: str, cmdList: list):
        cmd = ""
        for atomCmd in cmdList:
            cmd = cmd + atomCmd + "\n"
        self.add_cmd(keyword, cmd)

    def add_cmd(self, keyword: str, cmd: str):
        # Duplicate detection
        if keyword in self.CmdSet:
            return False
        self.CmdSet[keyword] = cmd
        return True

    def __load_cmdyml__(self):
        # load cmd.yml
        with open(self.cmd_path) as f:
            CmdYmlSet = yaml.load(f, Loader=yaml.FullLoader)
            for key, item in CmdYmlSet.items():
                keywordList = item['keyword']
                cmdList = item['cmd']
                for keyword in keywordList:
                    self.add_cmd_list(keyword, cmdList)

    def __getLink__(self):
        link_path = abspath(self.link_path)
        for link in find_all_link_file(link_path):
            link = link.split('\\')[-1]
            keyword = "link: " + link
            cmdList = "start " + pathJoin(link_path, link)
            self.add_cmd(keyword, cmdList)

    def __operate_cmd__(self, cmd):
        system(cmd)

    def __Parse__(self):
        flag = False
        word = self.Key
        linkword = "link: " + word + ".lnk"
        cmd = self.CmdSet.get(linkword)
        if not cmd is None:
            print(cmd)
            flag = True
        else:
            cmd = self.CmdSet.get(word)
            if not cmd is None:
                print(cmd)
                flag = True
        if flag:
            self.__operate_cmd__(cmd)

        return flag

    def apply(self):
        UIstr = "=" * 80 + '\n' + "what you wanna do".center(80) + "\n" + "=" * 80 + '\n'
        self.Key = input(UIstr)
        while not self.__Parse__():
            self.Key = input(
                "Wrong Input!\n"
                "See " + abspath(self.cmd_path) + " for more input detail\n"
                                                  "Please enter again (\"exit\" to quit)\n"
            )


def main():
    with open("./config.yml", "r+") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        # CMD_PATH = abspath("./")
        LINK_PATH = abspath("./resource/links")
        # 如果有config，则读取，否则就从默认地址找
        if 'YML_PATH' in config.keys():
            YML_PATH = abspath(config['YML_PATH'])

        if 'LINK_PATH' in config.keys():
            LINK_PATH = abspath(config['LINK_PATH'])
        f.close()
        S = StartParser(YML_PATH, LINK_PATH)
        S.apply()

    return


if __name__ == '__main__':
    main()
