"""Guessing nmber game"""
import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("there is currently no high score, its your for taking")
    else:
        print("High score is {} attempts" .format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1,10))
    print("hello, wlcm to game")
    player_name = input("what is your name")
    attempts= ()
guess = input("pick a number between 1 and 10")
    if int(guess) <1 or int(guess) >10
        ValueError("please guess a number in given range")
    if int(guess) == random_number:
        print("noice")
        attempts += 1
        attempts_list.append(attempts)
        print("it took u {} attempts" .format(attempts))
        play_again = input("wanna play again?")
