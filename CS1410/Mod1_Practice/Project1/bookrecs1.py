readBooks = open("booklist.txt", 'r')
bookList = []
for book in readBooks:
    tempList = book.strip().split(",")
    bookList.append((tempList[0], tempList[1]))

readRatings = open("ratings.txt","r")
count = 1
name = "name"
ratingsList = []
for line in readRatings:
    if count % 2 != 0:
        name = line.strip().lower()
    else:
        numList = line.split()
        numberList = []
        for l in numList:
            l = int(l)
            numberList.append(l)
        newDic = {"name": name, "ratings": numberList}
        ratingsList.append(newDic)
    count += 1


for name in ratingsList:
    friendList = []
    for other in ratingsList:
        value = 0
        count = 0
        if other["name"] != name["name"]:
            for number in name["ratings"]:
                value += number * other["ratings"][count]
                count += 1
        friendList.append({"friend": other["name"], "score": value})
    large = 0
    largeName = "name"
    largest = 0
    largestName = "name"
    for friend in friendList:
        if friend["score"] > largest:
            largest = friend["score"]
            largestName = friend["friend"]
        elif friend["score"] > large:
            large = friend["score"]
            largeName = friend["friend"]
    name["friends"] = [largestName,largeName]


def friends(name):
    for x in ratingsList:
        if name == x["name"]:
            return sorted(x["friends"])
  

def dotprod(x,y):
    assert len(x) == len(y)
    return sum(x[i]*y[i] for i in range(len(x)))


for user in ratingsList:
    goodBooks = []
    unreadBooks = []
    count = 0
    for num in user["ratings"]:
        if num >= 3:
            goodBooks.append(bookList[count])
        if num == 0:
            unreadBooks.append(bookList[count])
        count += 1
    user["goodbooks"] = goodBooks
    user["unreadbooks"] = unreadBooks

#Function that returns recommended books for a given user based off of the books they haven't read and the books that their friends have read.
#Added sorting by Author last name using a Lambda function.
def recommend(name):
    tempList = []
    theirRecommended = []
    for user in ratingsList:
        if user["name"] == name:
            for x in ratingsList:
                if x["name"] == user["friends"][0]:
                    tempList.extend(x["goodbooks"])
            for y in ratingsList:
                if y["name"] == user["friends"][1]:
                    tempList.extend(y["goodbooks"])
        if user["name"] == name:
            for book in tempList:
                if book in user["unreadbooks"]:
                    theirRecommended.append(book)
    sortedList = []
    theirRecommended = list(dict.fromkeys(theirRecommended))
    sortedList.extend(sorted(theirRecommended, key=lambda x: x[0].split(" ")[-1]))
    return sortedList
  

def report():
    myString = ""
    for person in sorted(ratingsList, key = lambda i: i['name']):
        myString += (person['name'] + " : " + str(sorted(person["friends"])))
        myString += "\n"
        for y in recommend(person['name']):
            myString += "\t" + str(y) + "\n"
        myString += "\n"
    return myString


def main():
    with open('recommendations.txt', 'w') as rec_file:
        print(report(), file=rec_file)
    #print(report())

if __name__ == '__main__':
    main()