import random


def password_append(difficulty, adjective, nouns, number1, number2, special1, special2):
    if difficulty == 4:  # Extreme password with special case at start and random capitalization
        result = special1 + adjective + nouns + number1 + number2 + special2
    if difficulty == 3:  # Extreme password with special case in between adj and noun along with random capitalization
        result = adjective + special1 + nouns + number1 + number2 + special2
    if difficulty == 2:  # Hard password with special case at the end and caps adj and noun
        result = adjective + nouns + number1 + number2 + special1
    if difficulty == 1:  # Easy password with cap adj and noun
        result = adjective + nouns + number1 + number2
    return result


def random_caps(str):
    result = ''
    for i in str:
        if random.choice([True, False]):
            result += i.upper()
        else:
            result += i.lower()
    return result


def pass_extr(pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special, pass_special2):
    start_or_center_choice = [0, 1]
    start_or_center = random.choice(start_or_center_choice)
    pass_adjective = random_caps(pass_adjective)
    pass_nouns = random_caps(pass_nouns)
    if start_or_center == 0:
        extr_password = password_append(4, pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special,
                                        pass_special2)
        return extr_password
    elif start_or_center == 1:
        extr_password = password_append(3, pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special,
                                        pass_special2)
        return extr_password


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
        extr_password = pass_extr(pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special,
                                  pass_special2)
        return extr_password
    elif choice == 1:  # Hard Password
        hard_password = password_append(2, pass_adjective, pass_nouns, pass_number1, pass_number2, pass_special, '')
        return hard_password
    elif choice == 0:  # Easy Pasword
        return password_append(1, pass_adjective, pass_nouns, pass_number1, pass_number2, '', '')


if __name__ == '__main__':
    while True:
        password_choices = ["Extreme", "extreme", "Hard", "hard", "Easy", "easy"]
        loop_choices = ["Yes", "yes", "No", "no"]
        user_choice = str(input("Would you like to generate an Extreme, Hard, or Easy password?: "))
        while user_choice not in password_choices:
            print("Invalid input, try again")
            user_choice = str(input("Would you like to generate an Extreme, Hard, or Easy password?: "))
        if user_choice == "Extreme" or user_choice == "extreme":
            password = password_generate(2)
        elif user_choice == "Hard" or user_choice == "hard":
            password = password_generate(1)
        elif user_choice == "Easy" or user_choice == "easy":
            password = password_generate(0)
        print(password)
        user_loop = str(input("Would you like to generate another password? (Yes or No): "))
        while user_loop not in loop_choices:
            print("Invalid input, try again")
            user_loop = str(input("Would you like to generate another password? (Yes or No): "))
        if user_loop == 'No' or user_loop == 'no':
            break

