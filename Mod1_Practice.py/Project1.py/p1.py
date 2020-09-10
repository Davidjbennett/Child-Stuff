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
    affinityScores = similarities[name]
    return affinityScores

def main():
    #print(books)
    #print(ratings)
    print(similarities)
    pass

if __name__ == "__main__":
    main()

