import operator 
from operator import itemgetter
from io import StringIO

#Read in booklist
with open("booklist.txt", 'r') as f:
    pass
    books = []
    for line in f:
        books.append(tuple(line.strip().split(',')))

#Read in Ratings
with open("ratings.txt", 'r') as f:
    ratings = {}
    while True:
        name = f.readline().strip().lower()
        if not name:
            break
        scores = f.readline().strip().split()
        ratings[name] = [int(score) for score in scores]

def dotprod(x, y):
    assert len(x) == len(y)
    return sum(x[i]*y[i] for i in range(len(x)))

similarities = {}

def compute_scores():
    for name1 in ratings:
        for name2 in ratings:
            if name1 != name2:
                affinityScore = dotprod(ratings[name1], ratings[name2])
                if affinityScore > 0:
                    similarities[name1] = similarities.get(name1, {})
                    similarities[name1][name2] = affinityScore

compute_scores()

def friends(name):
    all_friends = similarities[name]
    top_friends = [name for name,_ in sorted(all_friends.items(), key=operator.itemgetter(1), reverse = True)]
    return top_friends[0:2]

def recommend(name):
    my_friends = friends(name)

    recommendations = []
    my_ratings = ratings[name]

    for friend in my_friends:
        friend_ratings = ratings[friend]
        for i in range(len(friend_ratings)):
            if friend_ratings[i] >= 3 and my_ratings[i] == 0:
                book = books[i]
                if not book in recommendations:
                    recommendations.append(book)
    print(recommendations)
    return sorted(recommendations, key=aut_title)

def aut_title(book):
    aut = book[0].split()
    return (aut[-1], aut[0], book[1])

def report():
    s = StringIO()
    for name in sorted(similarities.keys()):
        print(name+':',friends(name), file=s)
        for a in recommend(name):
            print('\t',a,file=s)
        print(file=s)
    return s.getvalue()

def main():
    with open('recommendations.txt', 'w') as f:
        print(report(), file=f, end='')

if __name__ == "__main__":
    main()

