from num2words import num2words

total = 0
for i in range(1,1001):
    total += len(num2words(i)) - ((num2words(i)).count(" ")) - ((num2words(i)).count("-"))

print(total)
