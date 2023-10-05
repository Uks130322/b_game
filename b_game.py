"""
Play with your computer!
"""

import random


class ValueTooLarge(ValueError):
    pass


class ValueTooSmall(ValueError):
    pass


def game() -> None:
    """
    input number from 0 to 1000 and win or loose
    :return: None
    """
    hello = ('Hello! Will you play with me?\n', 'Hi, play with me, please!\n', "Hello, sweetie, let's play ;)\n",
             "Hello! It's really funny game!\n")
    again = ("Let's play again, please! ", "Wait, let me try again. ", "Sorry, i made a mistake, can we repeat? ",
             "Are you sure? Maybe once again? ", "I changed my mind, let's repeat. ",
             "I don't like your number, please, choose another one. ", "No, no, let me recoup. ")
    lose = ("Bad game. I won't play.", "I'm sure you're cheating, go away", "Damn, you win, happy now?",
            "I don't wanna play anymore")
    win = ('I won! ', 'You lose. ', "You're a loser. ", "I'm a winner! ")
    lap = 0
    i_lose = True

    print(random.choice(hello))

    while i_lose:
        try:
            your_number = int(input('Please enter your number from 0 to 1000:\n'))

            if your_number < 0:
                raise ValueTooSmall
            if your_number > 1000:
                raise ValueTooLarge

            my_number = random.randrange(0, 1001)
            print('Your number: ', your_number, '\nMy number: ', my_number)

            if your_number < my_number:
                print(random.choice(win), 'Take off your clothes.')
                i_lose = False
            else:
                lap += 1
                if lap < 5:
                    print(random.choice(again))
                else:
                    print(random.choice(lose))
                    i_lose = False

        except ValueTooLarge:
            print("Your number is too large! Please enter another number")
        except ValueTooSmall:
            print("Your number is too small! Please enter another number")
        except ValueError:
            print("It's not a number! Please enter your number from 0 to 1000.")


def main():
    game()


if __name__ == '__main__':
    main()
else:
    print('b_game loaded as a module')
