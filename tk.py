import os 
import sys 

# Tool to generate templates for some programming languages 
# Args: 
# filename 
# -t <template>
# -r <replacement>
# TODO: How can we use AI power here 

def parse_args(args: list[str]):
    parsed = {}
    parsed["filename"] = args[0]
    for i in range(1, len(args)):
        if (args[i].startswith("-")):
            parsed[args[i]] = args[i + 1]
            i += 1
    return parsed

def load_template(path: str, replacement: str):
    with open(path, "r") as fobj:
        lines: list[str] = [line for line in fobj.readlines()]
        print(lines)
        if lines[0].strip() != "---":
            print("Expected header!")
            sys.exit(-1)
        ending = None
        count = 0
        for line in lines[1::]:
            count += 1
            if (line.strip() == "---"):
                break
            if (line.startswith("end")):
                ending = line[len("end:")::].strip()
        count += 1
        if (ending is None):
            print("You must at least specify the file ending!")
            sys.exit(-1)
        print(lines)
        return (ending, [line.replace("$$$", replacement) for line in lines[count::]])

def main(args):
    parsed: dict = parse_args(args[1::])
    cwd = os.getcwd()

    script_path = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.join(script_path, "templates")
    
    if (not os.path.exists(template_path)):
        os.mkdir(template_path)
    
    if not "-t" in parsed.keys():
        print("You must specify a template!")
        return
    
    for template in os.listdir(template_path):
        if (parsed["-t"] in template):
            ending, lines = load_template(os.path.join(template_path, template), parsed["-r"] if "-r" in parsed.keys() else "")
            name = parsed["filename"]
            path = os.path.join(cwd, f"{name}.{ending}")
            print(lines)
            with open(path, "w") as fobj:
                for line in [i for i in lines if i != "\n"]:
                    if (line.strip() == "$n$"):
                        fobj.write("\n")
                        continue
                    fobj.write(line)   
            return  
        
    print("No template found!")


if __name__ == "__main__":
    import sys
    main(sys.argv)