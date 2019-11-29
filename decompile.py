import os

f_in = './input/'
f_out = './middle of the process/'

def decompile(f_in,f_out):
    f = open(f_in)
    file = open(f_out[:-4] + ".csv", 'w')
    txt = f.read()
    for lit in range(len(txt)):
        if txt[lit] != "\n":
            file.write(txt[lit] + ",")
        else:
            file.write(txt[lit])
    print(f"File \"{f_in[10:]}\" decompiled")
    f.close()

def running(f_in,f_out):
    files = os.listdir(f_in)
    for file in files:
        if file.endswith(".txt"):
            decompile(f_in + file, f_out + file)
        else:
            print(f"File \"{file}\" have wrong extension")
    else:
        if len(files) == 0:
            print(f"There is nothing to work in the folder \"{f_in[2:-1]}\"")

if __name__ == "__main__":
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