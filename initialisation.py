# --------------------------------------
# author - https://github.com/0dminnimda
# --------------------------------------
import os


def func():
    path = os.getcwd()
    name = ["/input/", "/middle of the process/", "/output/"]
    print(f"File Path: {path}\n")

    try:
        for i in range(3):
            os.mkdir(path+name[i])
    except OSError:
        print("Error during initialization,", end="")
        print(" probably initialization has already occurred")
    else:
        print ("Initialization completed successfully")

if __name__ == "__main__":
    print("-"*42)
    print("| author - https://github.com/0dminnimda |")
    print("-"*42, "\n")
    func()
    input('\nPress ENTER to exit')
