# -*- coding: utf-8 -*-
"""
=> Jumbled Words(the Permutations Game) <=
@author: APOORV KUMAR VERMA
"""
import random as ran
def play(player_name,player_points,picked_word,j_word):
    print(" ")
    print("it's your turn :",player_name)
    print("the Jumbled Words is :",j_word)
    ans = input("please write Answer :")
    if ans == picked_word:
        print("hurray ! your answer is right :-) ")
        player_points +=1
        print("Now your point is : ",player_points)
    else:
        print("oh! better luck next time.")
        print("the correct answer is :",picked_word)
    return player_name,player_points

def exit_msg(p1n,p2n,pp1,pp2):
        print("========= Score board ============= ")
        print("Player Name : ",p1n," Player Points :",pp1)
        print("Player Name : ",p2n," Player Points :",pp2)
        print("===================================")
        print("this Game coded by Apoorv verma")
        print("thank you for playing :-)")
        print("===================================")
        return ""
def word():
    words = ["Imagine","Mistake","Neglect","Oppress","computer","Partake","Persist"]
    word = ran.choice(words)
    return word

def jumble_word(word):
    while True:
        j_word = "".join(ran.sample(word,len(word)))
        if word == j_word:
            j_word = "".join(ran.sample(word,len(word)))
        else:
            return j_word
    

def main():
    print("===============================")
    print("welcom to the Permutations Game")
    print("========jumbled Words==========")
    p1n = input("Player 1 ,please Enter your Name :")
    p2n = input("Player 2 ,please Enter your Name :")
    pp1=0;pp2=0;turn=0;
    while True:
        picked_word = word()
        j_word = jumble_word(picked_word)
        if turn%2==0:
            p1n,pp1 = play(p1n,pp1,picked_word,j_word)
            turn = turn + 1
            k = input("press c to continue and q to quit : ")
            if k=='q':
                exit_msg(p1n,p2n,pp1,pp2)
                break 
        else:
            p2n,pp2 = play(p2n,pp2,picked_word,j_word)
            turn = turn + 1
            k = input("press c to continue and q to quit : ")
            if k=='q':
                exit_msg(p1n,p2n,pp1,pp2)
                break

if __name__ == "__main__":
    main()