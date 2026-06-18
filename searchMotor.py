import json

dictionary = []

with open("dictionary.json", "r", encoding="utf-8") as dic:
     for txt in dic:
        txtClean = txt.strip().rstrip(",")

        if txtClean:
            dictionary.append(json.loads(txtClean))

def saveList():
    with open("dictionary.json", "w", encoding="utf-8") as dic:
        for text in dictionary:
            dic.write(json.dumps(text)+",\n")

def main():
    ex:bool = False
    
    while ex == False:
        choice = input("What do you want to do?\n 1. Add text\n 2. Search text\n 0. Exit\nInsert your choice: ")
        match choice:
            case "1":
                addDic()
            case "2":
                search()
            case "0":
                saveList()
                ex = True
            case _:
                print("Option not valid!")
            
def addDic():
    text = input("Insert the text you want to add: ")
    
    dictionary.append(text)
    
    print("Text added!\n\n")

    
    
def search():
    src = input("Search: ").split(" ")

    foundText, fndTxtInd = [], []
    
    for word in src:    
        for text in dictionary:
            if text.rfind(word) > -1 and dictionary.index(text) not in fndTxtInd:
                foundText.append(text)
                fndTxtInd.append(dictionary.index(text))

    for i in range(len(foundText)-1):
        for j in range(len(foundText)-1-i):
            if len(foundText[j]) < len(foundText[j+1]):
                foundText[j], foundText[j+1] = foundText[j+1], foundText[j]

    print("\n")
    for text in foundText:
        print(f" -> {text}")
    print("\n")
    
main()
