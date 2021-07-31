import random
import tkinter as tk
window = tk.Tk()
window.geometry("400x300")
window.title("Jogo: Pedra, Papel ou Tesoura")
#window.title("Rock Paper Scissors Game")
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""


def choice_to_number(choice):
    rps = {'pedra': 0, 'papel': 1, 'tesoura': 2}
    return rps[choice]


def number_to_choice(number):
    rps = {0: 'pedra', 1: 'papel', 2: 'tesoura'}
    return rps[number]


def random_computer_choice():
    return random.choice(['pedra', 'papel', 'tesoura'])


def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if(user == comp):
        print("Tie")
    elif((user - comp) % 3 == 1):
        print("You win")
        USER_SCORE += 1
    else:
        print("Comp wins")
        COMP_SCORE += 1
    text_area = tk.Text(master=window, height=12, width=30, bg="#FFFF99")
    text_area.grid(column=0, row=4)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n \
        Computer Score : {c} ".format(uc=USER_CHOICE, cc=COMP_CHOICE, u=USER_SCORE, c=COMP_SCORE)
    text_area.insert(tk.END, answer)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'pedra'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'papel'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'tesoura'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


button1 = tk.Button(text="    Pedra    ", bg="skyblue", command=rock)
button1.grid(column=0, row=1)
button2 = tk.Button(text="    Papel    ", bg="pink", command=paper)
button2.grid(column=0, row=2)
button3 = tk.Button(text="    Tesoura    ", bg="lightgreen", command=scissor)
button3.grid(column=0, row=3)

window.mainloop()
