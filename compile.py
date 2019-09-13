import os

f_in = './middle of the process/'
f_out = './output/'


def compile(f_in, f_out):
    f = open(f_in)
    file = open(f_out[:-4] + ".txt", 'w')
    txt = f.read()
    txt = txt.replace(",", "")
    file.write(txt)
    print("File \"{}\" compiled".format(f_in[24:]))
    f.close()


if __name__ == "__main__":
    files = os.listdir(f_in)
    for file in files:
        if file.endswith(".csv"):
            compile(f_in + file, f_out + file)
        else:
            print("File \"{}\" have wrong extension".format(file))
