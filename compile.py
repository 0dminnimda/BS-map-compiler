# --------------------------------------
# author - https://github.com/0dminnimda
# --------------------------------------
import os

f_in = './middle of the process/'
f_out = './output/'

def compile(f_in,f_out):
    f = open(f_in)
    file = open(f_out[:-4] + ".txt", 'w')
    txt = f.read()
    txt = txt.replace(",", "")
    file.write(txt)
    print(f"File \"{f_in[24:]}\" compiled")
    f.close()

def running(f_in,f_out):
    files = os.listdir(f_in)
    for file in files:
        if file.endswith(".csv"):
            compile(f_in + file, f_out + file)
        else:
            print(f"File \"{file}\" have wrong extension")
    else:
        if len(files) == 0:
            print(f"There is nothing to work in the folder \"{f_in[2:-1]}\"")

if __name__ == "__main__":
    print("-"*42)
    print("| author - https://github.com/0dminnimda |")
    print("-"*42,"\n")
    try:
        running(f_in,f_out)
    except FileNotFoundError:
        try:
            from initialisation import func
            print("There is no initialization in the folder, initialization will running now")
            print("Running initialisation\n")
            print("-"*50)
            func()
            print("-"*50,"\n")
            running(f_in,f_out)
        except ModuleNotFoundError:
            print("There is no \"initialisation.py\" file in the folder, download it")

    input('\nPress ENTER to exit')