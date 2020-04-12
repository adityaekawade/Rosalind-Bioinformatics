x = 907 
y = 948
c = (x**2) + (y**2) 
print(c)


a = 'flimsy'
b = 'miserable'
c = b[0:1] + a[2:]
print len(a)
print c


str = "AuAPkBTPmGDDl60lnQGhCCrfIj3MgopB5nXByzChbwcYKTylototritoncf2x2nNNoUTb0KoNG58TYd6lGIPyybXgkfgeHyGUQemXSqv9PhbicinctoresIC4OBo9sO5QLlNvbYICrq94QlrIcFjeh7Eyxaf160UuwDcmHUzBSeEVVsigeOSmbhx"
a = str[45:57]
b = str[107:118]
print('' + a + ' ' + b)


a = 100
b = 200 
sum = 0
for i in range(a, b):
    if i%2 != 0:
        sum += i
print(sum)


def conditionsAndLoop(a,b):
    sum = 0
    for i in range(a, b):
        if i % 2 != 0:
            sum += i
    return sum


print(conditionsAndLoop(4498, 9436))



with open('file.txt', 'r') as f:
    myfile = f.readlines()

NumberOfLines = 0
for line in myfile:
    NumberOfLines += 1
print(NumberOfLines)

newFile = open('OddNumberedFile.txt', 'w')

for i in range(1, NumberOfLines, 2):
    # print (myfile[i])
    newFile.write(myfile[i])

newFile.close()


str = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
arr = list(str.split(" "))
obj = {}
for i in arr:
    if i in obj: 
        obj[i] += 1
    else: 
        obj[i] = 1

for i in obj:
    print(i, '', obj[i])

