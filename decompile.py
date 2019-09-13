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
    print("File \"{}\" decompiled".format(f_in[10:]))
    f.close()


if __name__ == "__main__":
    files = os.listdir(f_in)
    for file in files:
        if file.endswith(".txt"):
            decompile(f_in + file, f_out + file)
        else:
            print("File \"{}\" have wrong extension".format(file))
