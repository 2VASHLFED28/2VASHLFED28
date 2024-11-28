s = input("Введите строку:")
count = 0
vowels = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
for letter in s:
   if letter in vowels:
       count += 1
print("Количество гласных равно:")
print(count)

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
a = str(input("Введите строку: "))
print(reverse(a))

str = input('Введите строку: ')
word= input('Введите слово: ')


print('ДА' if word in str.lower() else 'НЕТ')
user_input = str(input())
output = user_input.replace(' ','_')
print(output)

user_input = input("Введите строку: ")


if user_input == user_input[::-1]:
    print("ЭТА СТРОКА ПАЛИНДРОМ")
else:
    print ("ЭТА СТРОКА НЕ ЯВЛЯЕТСЯ ПАЛИНДРОМОМ")