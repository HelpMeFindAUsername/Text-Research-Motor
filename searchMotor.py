import json

dictionary = []
stopWords = {"the", "a", "an", "in", "on", "at", "is", "and", "or"}


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
    src = []

    for search in input("Search: ").lower().split():
        if search not in stopWords:
            src.append(search)
    
    foundText, fndTxtInd = [], []
    
    for word in src:    
        for text in dictionary:
            if text.lower().rfind(word) > -1 and dictionary.index(text) not in fndTxtInd:
                foundText.append(text)
                fndTxtInd.append(dictionary.index(text))


    results = sorted(foundText, key=lambda t: sum(1 for w in src if w.lower() in t.lower()), reverse=True)
    

    print("\n")
    for result in results:
        print(f" -> {result}")
    print("\n")
    
main()
