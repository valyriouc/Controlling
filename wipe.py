import shutil
import os 

# Removes all subdirectories for the specified path with the specified name 
def clean(path, pattern):
    for i in os.listdir(path):
        combined = os.path.join(path, i)
        if (os.path.isdir(combined) and i == pattern):
            print(f"Removing {combined}")
            shutil.rmtree(combined)
        if (os.path.isdir(combined)):
            clean(combined, pattern)

def main(args):
    args = args[1::]
    cwd = os.getcwd()
    for del_dir in args:
        clean(cwd, del_dir)
            
if __name__ == "__main__":
    import sys
    main(sys.argv)