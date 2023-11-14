with open("dictionary/" + input("choose language (french/english) :") + ".txt", "r") as f:
    wordList = f.read().splitlines()

n = int(input("Number of letters: "))

nextList = []
for word in wordList:
    if len(word) == n:
        nextList.append(word)

wordList = nextList.copy()

while(True):
    cmd, x = input().split()
    
    nextList = []

    if cmd == "suggest":
        print(x + " possible words:")
        for word in wordList[0:int(x)]:
            print(word)
        print("\n")
        continue

    elif cmd == "ab":
        for word in wordList:
            if x not in word:
                nextList.append(word)

    elif cmd == "pr":
        for word in wordList:
            if x in word:
                nextList.append(word)

    elif cmd == "pos":
        position = int(input("Enter position: "))-1
        for word in wordList:
            if word[position] == x:
                nextList.append(word)

    elif cmd == "not":
        position = int(input("Enter position: "))-1
        for word in wordList:
            if word[position] != x:
                nextList.append(word)        

    else:
        print("???")
        continue    

    wordList = nextList