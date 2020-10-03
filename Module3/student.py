
class Student():
    def __init__(self, name, number):
        self.name = name
        self.scores = [0] * number

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))
    
    def getName(self):
        '''returns the name of the student'''
        return self.name
    
    def getScore(self, i):
        '''Returns the score at the index i'''
        return self.scores[i]

    def setScore(self, i, score):
        ''''score' Sets the score for the selected index 'i' '''
        self.scores[i] = score
    
    def getAverage(self):
        return sum(self.scores)/len(self.scores)

    def getHighScore(self):
        high = 0
        for i in self.scores:
            if i > high:
                high = i
        return high



s = Student("becky", 1)
s2 = Student("Dave", 13)

print(Student.setScore(s, 0, 60))
print(Student.getHighScore(s))
