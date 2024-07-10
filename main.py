import random


def password_append(difficulty, adjective, nouns, number1, number2, special1, special2):
    result_append = ""
    if difficulty == 4:  # Extreme password with special case at start and random capitalization
        result_append = special1 + adjective + nouns + number1 + number2 + special2
    if difficulty == 3:  # Extreme password with special case in between adj and noun along with random capitalization
        result_append = adjective + special1 + nouns + number1 + number2 + special2
    if difficulty == 2:  # Hard password with special case at the end and caps adj and noun
        result_append = adjective + nouns + number1 + number2 + special1
    if difficulty == 1:  # Easy password with cap adj and noun
        result_append = adjective + nouns + number1 + number2
    return result_append


def random_caps(string):
    result = ''
    for i in string:
        if random.choice([True, False]):
            result += i.upper()
        else:
            result += i.lower()
    return result


def pass_extreme(pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special, pass_special2):
    start_or_center_choice = [0, 1]
    start_or_center = random.choice(start_or_center_choice)
    pass_adjective = random_caps(pass_adjective)
    pass_nouns = random_caps(pass_nouns)
    if start_or_center == 0:
        extreme_password = password_append(4, pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special,
                                           pass_special2)
        return extreme_password
    elif start_or_center == 1:
        extreme_password = password_append(3, pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special,
                                           pass_special2)
        return extreme_password


def password_generate(choice):
    adjectives_choices = ["Lovely", "Joyful", "Adorable", "Charming", "Stunning", "Agreeable", "Mysterious",
                          "Cheerful", "Colorful", "Exciting", "Fearless", "Goregous", "Elegant"]
    noun_choices = ["Programmer", "Doctor", "Mechanic", "Engineer", "Farmer", "Student", "Lawyer", "Firefighter",
                    "Accountant", "Company", "Flower", "Invention", "Knowledge", "Distance"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special = ["!", "?", "/", "$", "%", "(", ")", "[", "]", ",", "."]
    pass_adjective = random.choice(adjectives_choices)
    pass_nouns = random.choice(noun_choices)
    pass_number1 = random.choice(numbers)
    pass_number2 = random.choice(numbers)
    pass_special = random.choice(special)
    pass_special2 = random.choice(special)
    if choice == 2:  # Extreme Password
        extreme_password = pass_extreme(pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special,
                                        pass_special2)
        return extreme_password
    elif choice == 1:  # Hard Password
        hard_password = password_append(2, pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special, '')
        return hard_password
    elif choice == 0:  # Easy Password
        return password_append(1, pass_adjective, pass_nouns, pass_number1, pass_number2, '', '')


if __name__ == '__main__':
    while True:
        password_choices = ["extreme", "hard", "easy"]
        loop_choices = ["yes", "no"]
        user_choice = str(input("Would you like to generate an Extreme, Hard, or Easy password?: "))
        user_choice = user_choice.lower()
        while user_choice not in password_choices:
            print("Invalid input, try again")
            user_choice = str(input("Would you like to generate an Extreme, Hard, or Easy password?: "))
            user_choice = user_choice.lower()
        if user_choice == user_choice == "extreme":
            password = password_generate(2)
        elif user_choice == "hard":
            password = password_generate(1)
        elif user_choice == "easy":
            password = password_generate(0)
        print(password)
        user_loop = str(input("Would you like to generate another password? (Yes or No): "))
        user_loop = user_loop.lower()
        while user_loop not in loop_choices:
            print("Invalid input, try again")
            user_loop = str(input("Would you like to generate another password? (Yes or No): "))
            user_loop = user_loop.lower()
        if user_loop == 'no':
            break
