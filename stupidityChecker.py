import time
from tkinter import *
import random
import os
from time import sleep

programPath = os.path.dirname(os.path.realpath(__file__))

window = Tk()
window.geometry("350x300")
window.resizable(False, False)
window.title("Stupidity Checker: Are you stupid?")

checkButtonIcon = PhotoImage(file="%s\\icons\\check.png" % programPath)
backButtonIcon = PhotoImage(file="%s\\icons\\back.png" % programPath)
helpButtonIcon = PhotoImage(file="%s\\icons\\help.png" % programPath)
approvedIcon = PhotoImage(file="%s\\icons\\approved.png" % programPath)

with open("answers.config") as answersConfig:
	answers = answersConfig.read().split("\n")
answersConfig.close()

with open("checks.config") as checksConfig:
	checks = checksConfig.read().split("\n")
checksConfig.close()


def check(checkedTimes):
	shouldCheckTimes = random.randint(4, 7)
	while checkedTimes <= shouldCheckTimes:
		for widget in window.winfo_children():
			widget.destroy()
		checkingLabel = Label(window, text=random.choice(checks), font=(None, 36), wraplength=350)
		checkingLabel.pack(anchor=CENTER, pady=(40, 0))
		time.sleep(0)
		window.update()
		checkedTimes = checkedTimes + 1
	stupidScreen()

def stupidScreen():
	for widget in window.winfo_children():
		widget.destroy()
	answer = random.choice(answers)

	print(len(answer))
	if len(answer) <= 20:
		answerFont = 40
		answerPadding = 70
	elif len(answer) <= 30:
		answerFont = 35
		answerPadding = 50
	else:
		answerFont = 20
		answerPadding = 40

	answerLabel = Label(window, text=answer, font=(None, answerFont), wraplength=350)
	answerLabel.pack(side=TOP, pady=(answerPadding, 0))

	approvedButton = Button(window, image=approvedIcon, border="0", state=DISABLED)
	approvedButton.pack(side=RIGHT, anchor=S)

	backButton = Button(window, image=backButtonIcon, border="0", command=lambda:main())
	backButton.pack(side=LEFT, anchor=S)


def helpPage():
	for widget in window.winfo_children():
		widget.destroy()
	helpLabel = Label(window, text="This program is a joke and was not intended to be used for embarrassment purposes." , font=(None, 25), wraplength=350)
	helpLabel.pack(side=TOP, pady=(15, 0))

	backButton = Button(window, image=backButtonIcon, border="0", command=lambda: main())
	backButton.pack(side=LEFT, anchor=S)

def main():
	for widget in window.winfo_children():
		widget.destroy()

	titleLabel = Label(window, text="Are you stupid?", font=(None, 36))
	titleLabel.pack(side=TOP, pady=(12, 2))

	descriptionLabel = Label(window, text="The most accurate stupidity checker", font=(None, 12))
	descriptionLabel.pack(anchor="ne")

	checkButton = Button(window, border="0", image=checkButtonIcon, command=lambda:check(0))
	checkButton.pack(side=RIGHT, anchor="s")

	helpButton = Button(window, border="0", image=helpButtonIcon, command=lambda:helpPage())
	helpButton.pack(side=LEFT, anchor="s")

	window.mainloop()

main()
