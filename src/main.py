import sys

def main():
    if len(sys.argv) <= 1:
        print("Expected argument")
        return
    inputtext = []
    with open(sys.argv[1], "r") as file:
        for line in file.readlines():
            inputtext.append(line.replace("\n", ""))

    for line in inputtext:
        print(line)

if __name__ == "__main__":
    main()