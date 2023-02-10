# def first_function(name):
#     print(f"{'your name: '}{name}")
#
#
# first_function('vikash')
# \n --> will add empty line

def user_guessing_game(secret_number, stop):
    user_input = ''
    while user_input != stop:
        user_input = input("\nenter the number: ")
        if secret_number == user_input:
            print(f"{'Bingo correct number: '} {secret_number}")
        else:
            print('number not matching! try again!! you number is ' + user_input)


user_guessing_game("99", 'stop')
