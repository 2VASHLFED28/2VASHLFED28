- 👋 Hi, I’m @2VASHLFED
- 👀 I’m interested in ...
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...

<!---
2VASHLFED28/2VASHLFED28 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
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
