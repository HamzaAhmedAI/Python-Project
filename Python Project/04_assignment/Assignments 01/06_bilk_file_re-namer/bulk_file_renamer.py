import os

def main():
    i = 0
    path = "C:/Users/Lucifer_2.0/OneDrive/Pictures/Camera Roll/"
    for file_name in os.listdir(path):
        my_dest = ("img" + str(i) + ".png")
        my_source = path + file_name
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == "__main__":
    main()