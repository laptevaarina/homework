with open('input.txt') as fin:
    number = fin.readline()

Rome = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
def rome_translate(number):
    new = 0
    last = 0
    for i in range(len(number)-1, -1, -1):
        num = Rome.get(number[i])
        if num >= last:
            new += num
        else:
            new -= num
        last = num
    return new

with open('output.txt', 'w') as fout:
    print(rome_translate(number), file = fout)