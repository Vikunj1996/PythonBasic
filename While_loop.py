# a = 0;
#
# while a < 5:
#     print(a)
#     a = a + 1
#
# for a in range(10):
#     print(f"{'inside for loop range value : '} {a}")

user_input = ''

while user_input != '-1':
    user_input = input("Guess the number between 1 to 100: ")
    if 1 <= int(user_input) <= 100:
        print(f"{'number is between 1 to 100: '} {user_input}")
    else:
        print(f"{'number is: '}{user_input}")
    print("let play again!")
