from tkinter import *
from tkinter import ttk
import main


def q1(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)

    opts1 = ('Completed Masters', 'PhD', 'Bachelor Degree', 'High school or GED', 'Unfinished high school',
             'Unfinished PhD', 'Unfinished Bachelor', 'Unfinished Masters')
    box.set('PhD')
    box['values'] = opts1
    QText.set("What is your level of education?")
    subm['command'] = lambda: q2(box.get())


def q2(text):
    if text == 'Unfinished high school':
        main.answers.append(0)
    elif text == 'High school or GED':
        main.answers.append(1)
    elif text == 'Unfinished Bachelor':
        main.answers.append(2)
    elif text == 'Bachelor Degree':
        main.answers.append(3)
    elif text == 'Unfinished Masters':
        main.answers.append(4)
    elif text == 'Completed Masters':
        main.answers.append(5)
    elif text == 'Unfinished PhD':
        main.answers.append(6)
    elif text == 'PhD':
        main.answers.append(7)

    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you have your own computer?")
    subm['command'] = lambda: q3(box.get())


def q3(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)

    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Have you been hospitalized for a mental illness before?")
    subm['command'] = lambda: q4(box.get())


def q4(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)

    box.set(0)
    box['values'] = ''
    box['state'] = 'normal'
    QText.set("For how many days?")
    subm['command'] = lambda: q5(box.get())


def q5(text):
    if text.isdigit():
        main.answers.append(float(box.get()))
    else:
        main.answers.append(0)
    box['state'] = 'readonly'
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Are you legally disabled?")
    subm['command'] = lambda: q6(box.get())


def q6(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you have regular access to the internet?")
    subm['command'] = lambda: q7(box.get())


def q7(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you live w/ your parents?")
    subm['command'] = lambda: q8(box.get())


def q8(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you have a gap in your resume?")
    subm['command'] = lambda: q9(box.get())


def q9(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)
    box.set(0)
    box['values'] = ''
    box['state'] = 'normal'
    QText.set("For how many months?")
    subm['command'] = lambda: q10(box.get())


def q10(text):
    if text.isdigit():
        main.answers.append(int(box.get()))
    else:
        main.answers.append(0)
    box['state'] = 'readonly'
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Are you unemployed?")
    subm['command'] = lambda: q11(box.get())


def q11(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you read outside of work and school?")
    subm['command'] = lambda: q12(box.get())


def q12(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)
    box.set(0)
    box['values'] = ''
    box['state'] = 'normal'
    QText.set("How many times have you been hospitalized for your mental illness?")
    subm['command'] = lambda: q13(box.get())


def q13(text):
    if text.isdigit():
        main.answers.append(int(box.get()))
    else:
        main.answers.append(0)
    box['state'] = 'readonly'
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you have trouble concentrating?")
    subm['command'] = lambda: q14(box.get())


def q14(text):
    if text == 'Yes':
        main.answers.append(float(1))
    else:
        main.answers.append(float(0))
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Would you say that you often feel anxious")
    subm['command'] = lambda: q15(box.get())


def q15(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you often overthink a situation that has already happened")
    subm['command'] = lambda: q16(box.get())


def q16(text):
    if text == 'Yes':
        main.answers.append(float(1))
    else:
        main.answers.append(float(0))
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you suffer from rapid mood swings")
    subm['command'] = lambda: q17(box.get())


def q17(text):
    if text == 'Yes':
        main.answers.append(float(1))
    else:
        main.answers.append(float(0))
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you get panic attacks frequently")
    subm['command'] = lambda: q18(box.get())


def q18(text):
    if text == 'Yes':
        main.answers.append(float(1))
    else:
        main.answers.append(float(0))
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Do you suffer from compulsive behavior")
    subm['command'] = lambda: q19(box.get())


def q19(text):
    if text == 'Yes':
        main.answers.append(float(1))
    else:
        main.answers.append(float(0))
    opts1 = ('Yes', 'No')
    box.set('Yes')
    box['values'] = opts1
    QText.set("Are you often tired")
    subm['command'] = lambda: q20(box.get())


def q20(text):
    if text == 'Yes':
        main.answers.append(1)
    else:
        main.answers.append(0)
    opts1 = ('1-17', '18-30', '31-51', '51 and over')
    box.set('1-24')
    box['values'] = opts1
    QText.set("Pick your age range")
    subm['command'] = lambda: q21(box.get())


def q21(text):
    if text == '1-17':
        main.answers.append(0)
    elif text == '18-30':
        main.answers.append(1)
    elif text == '31-51':
        main.answers.append(2)
    else:
        main.answers.append(3)
    opts1 = ('Male', 'Female')
    box.set('Male')
    box['values'] = opts1
    QText.set("Select your gender")
    subm['command'] = lambda: q22(box.get())


def q22(text):
    if text == 'Male':
        main.answers.append(1)
    else:
        main.answers.append(0)
    box.set(0)
    box['values'] = ''
    box['state'] = 'normal'
    QText.set("State your annual income")
    subm['command'] = lambda: q23(box.get())


def q23(text):
    if text.isdigit():
        main.answers.append(float(box.get())/20)
    else:
        main.answers.append(0)
    main.predict(main.answers)


root = Tk()

# Window Formatting
root.title("Depression Questionnaire")
root.geometry('900x600')
root.resizable(False, False)
# BG
background = PhotoImage(file='sunflowers.png')
bg = Label(root, image=background)
bg.place(x=0, y=0)

frame1 = Frame(root, bg="#FFA500")
frame1.pack(padx=5, pady=5)

title = Label(root, text="Depression Questionnaire", font=("Arial", 25))
title.pack(pady=50)

QText = StringVar()
QText.set("Do you identify as having a mental illness?")
Q = Label(root, textvariable=QText)
Q.pack(pady=50)

opts = ('Yes', 'No')
box = ttk.Combobox(root, state='readonly', width=27, values=opts)
box.set('Yes')
box.pack(pady=50)

subm = Button(root, text='Submit', command=lambda: q1(box.get()), font=("Arial", 17))
subm.pack(pady=50)

root.mainloop()
