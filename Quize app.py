dic = dict()
dic['CPU'] = 'central processing unit'
dic['GPU'] = 'graphical processing unit'
dic['PSU'] = 'power suply unit'
dic['RAM'] = 'random access memory'
dic['ROM'] = 'read only memory'
counter = 0
wrongCounter = 0
num = 1

print("\t\t\tQuize for acronym: ")
print("Enter the appropriate phrase for the questions:")

for acronym in dic:
    answer = input(f"{num}) What does {acronym} stand for? ")
    if answer.lower() == dic[acronym]:
       counter += 1
       print("\tCorrect!")
    else:
        print("\tIncorrect!")
        wrongCounter += 1
    if wrongCounter == 2:
        print("Faild you have entered 2 wrong answers!!!")
        break
    num += 1

print(f"The final result is: {counter}/{num}")