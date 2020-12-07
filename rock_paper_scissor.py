# Importing Dependencies
from tkinter import *
from PIL import ImageTk, Image
import random

# GUI for the game
gameScreen = Tk()
gameScreen.geometry("750x550+200+200")
gameScreen.resizable(0, 0)
gameScreen.title('Rock Paper Scissor')


# Global Variables
user_win = 0
computer_win = 0
initial_user = ''
initial_computer = ''
initial_status = ''

user = StringVar(value = 'You 0')
computer = StringVar(value = 'Computer 0')
status = StringVar(value = 'Let\'s play')

# Functionality
def reset():
    global user_win
    global computer_win
    global initial_status
    user_win = 0
    computer_win = 0
    initial_user = f'You {str(user_win)}'
    initial_computer = f'Computer {str(computer_win)}'
    initial_status = 'Play Again'
    user.set(initial_user)
    computer.set(initial_computer)
    status.set(initial_status)

def getComputerChoice():
    choices = ['rock', 'paper', 'scissor']
    randomNum = random.randint(0, 2)
    return choices[randomNum]
    
switcher = {
        'rock_scissor': 'win',
        'scissor_paper': 'win',
        'paper_rock': 'win',
        'paper_scissor': 'lose',
        'rock_paper': 'lose',
        'scissor_rock': 'lose',
        'paper_paper': 'draw',
        'scissor_scissor': 'draw',
        'rock_rock': 'draw'
    }

def game(choose):
    global user_win
    global computer_win
    computerChoice = getComputerChoice()
    case = choose + '_' + computerChoice
    func = switcher.get(case, 'nothing')
    if func == 'win':
        user_win += 1
        initial_user = f'You {str(user_win)}'
        initial_status = f'You win !!\n You picked {choose} and computer picked {computerChoice}'
        user.set(initial_user)
        status.set(initial_status)
    if func == 'lose':
        computer_win += 1
        initial_computer = f'Computer {str(computer_win)}'
        initial_status = f'You lose !!\n You picked {choose} and computer picked {computerChoice}'
        computer.set(initial_computer)
        status.set(initial_status)
    if func == 'draw':
        initial_status = f'Draw !!\n Both Picked same'
        status.set(initial_status)

row1 = Frame(gameScreen, background = 'red')
row1.pack(expand = True, fill = "both")

# To Display User Score
display1 = Label(
    row1,
    text = 'You',
    font = ("Courier New", 20),
    textvariable = user,
    fg = '#000000',
    bg = '#DEDEDE'
)
display1.pack(side = LEFT, expand = True, fill = "both",)

# To Display Computer  Score
display2 = Label(
    row1,
    text = 'Computer',
    font = ("Courier New", 20),
    textvariable = computer,
    fg = '#000000',
    bg = '#DEDEDE'
)
display2.pack(side = LEFT, expand = True, fill = "both",)

row2  = Frame(gameScreen)
row2.pack(expand = True, fill = 'both')

# To Show the status
display5 = Label(
    row2,
    text = 'Label',
    font = ("Courier New", 20),
    textvariable = status,
    fg = '#000000'
)
display5.pack(side = LEFT, expand = True, fill = 'both')

# Reload Button
reload  = Image.open("./assets/reload.png")
reload = reload.resize((40, 40), Image.ANTIALIAS)
photo4= ImageTk.PhotoImage(reload)
btn4 = Button(gameScreen, image=photo4, border = 0, activebackground = '#c6c6c6', command = lambda: reset())
btn4.place(x = 690, y = 10)

row3 = Frame(gameScreen)
row3.pack(expand = True, fill = "both")

# Rock Button
img1  = Image.open("./assets/rock.png")
img1 = img1.resize((100, 100), Image.ANTIALIAS)
photo1= ImageTk.PhotoImage(img1)
btn1 = Button(row3, image=photo1, command = lambda: game('rock'), border = 0)
btn1.pack(side = LEFT, expand = True, fill = "both")

# Paper Button
img2  = Image.open("./assets/paper.png")
img2 = img2.resize((100, 100), Image.ANTIALIAS)
photo2= ImageTk.PhotoImage(img2)
btn2 = Button(row3, image=photo2, command = lambda: game('paper'), border = 0)
btn2.pack(side = LEFT, expand = True, fill = "both")

# Scissor Button
img3  = Image.open("./assets/scissor.png")
img3 = img3.resize((100, 100), Image.ANTIALIAS)
photo3= ImageTk.PhotoImage(img3)
btn3 = Button(row3, image=photo3, command = lambda: game('scissor'), border = 0)
btn3.pack(side = LEFT, expand = True, fill = "both")


# Continuos Loop
gameScreen.mainloop()