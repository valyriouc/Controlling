import os 
import sys

class Platforms:
    WIN = "win32",
    LINUX = "linux"

def help():
    text = "Coming soon..."
    print(text)
    sys.exit(-1)

def save(args: list[str]):
    shortcut = " "
    if "-s" in args: 
        index = args.index("-s")
        if len(args) <= index + 1:
            help()
        shortcut = args[index + 1]
    wd = os.getcwd()
    script_path = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(script_path, "config.txt")
    if (not os.path.exists(config_file)):
        with open(config_file, "w") as fobj:
            content = f"{wd}:{shortcut}"
            fobj.write(content)
    else:
        content = None
        with open(config_file, "r") as fobj:
            content = fobj.readlines()

        with open(config_file, "w") as fobj:
            new = f"{wd}:{shortcut}"
            new_content = [new]
            new_content.extend(content)
            text = ""
            first = True
            for i in new_content:
                if first == True:
                    text += i
                    first = False
                else:
                    text += f"\n{i}"
            fobj.write(text)
    update_history(wd)

def update_history(path: str):
    history = []
    history.append(path)
    history.extend(read_history())
    history_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "history.txt")
    with open(history_file, "w") as fobj:
        for i in history:
            fobj.write(i + "\n")

def read_history() -> list[str]:
    history_file = os.path.dirname(os.path.realpath(__file__))
    history_file = os.path.join(history_file, "history.txt")
    if (not os.path.exists(history_file)):
        return [] 
    else:
        with open(history_file, "r") as fobj:
            return [line.strip() for line in fobj.readlines()]

def print_history(args):
    for line in read_history():
        print(line)

def backward(args: list[str]):
    count = 1
    if "-c" in args:
        index = args.index("-c")
        if len(args) <= index + 1:
            help()
        count = int(args[index + 1])
    history = read_history()
    print(history[count])
    update_history(history[count])

def go(args: list[str]):
    script_path = os.path.dirname(os.path.realpath(__file__))
    config_file = os.path.join(script_path, "config.txt")
    if os.path.exists(config_file):
        going_to = args[0]
        with open(config_file, "r")  as fobj:
            content = fobj.readlines()
            for i in content:
                splitted = i.rsplit(":", 1)
                if splitted[1].strip() != " " and going_to==splitted[1].strip():
                    print(splitted[0].strip())
                    update_history(splitted[0].strip())
                else:
                    pass 
        
keywords = {
    'b': backward,
    's': save,
    'h': print_history,
    'g': go
}

def main(args: list[str]):
    func = keywords[args[0]]
    func(args[1::])

if __name__ == "__main__":
    main(sys.argv[1::])