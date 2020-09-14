def solution(number):
    sum = 0
    counter = 0

    while counter < number/3:
        sum += counter*3
        counter +=1
    
    counter = 0
    while counter < number/5:
        sum += counter*5
        counter+=1

    return sum

print(solution(10))