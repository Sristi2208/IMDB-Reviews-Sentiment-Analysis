# -*- coding: utf-8 -*-
"""
Created on Thu May  1 02:40:49 2021

@author: keert
"""

# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sys import exit
import tkinter as tk
# import all methods and classes from the tkinter
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Function for clearing the
# contents of all entry boxes
# And text area.
def clearAll() :

	# deleting the content from the entry box
	negativeField.delete(0, END)
	neutralField.delete(0, END)
	positiveField.delete(0, END)
	overallField.delete(0, END)

	# whole content of text area is deleted
	textArea.delete(1.0, END)
	
# function to print sentiments
# of the sentence.
def detect_sentiment():

	# get a whole input content from text box
    sentence = textArea.get("1.0", "end")

	# Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

	# polarity_scores method of SentimentIntensityAnalyzer
	# oject gives a sentiment dictionary.
	# which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    string = sentiment_dict['neg']*100 
    negativeField.insert(10, string)
    x = sentiment_dict['neg']
	

    string = sentiment_dict['neu']*100
    neutralField.insert(10, string)
    y = sentiment_dict['neu']
    
    string = sentiment_dict['pos']*100
    positiveField.insert(10, string)
    z = sentiment_dict['pos']
	# decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        string = "Positive"

    elif sentiment_dict['compound'] <= - 0.05 :
        string = "Negative"
	

    else :
        string = "Neutral"

    overallField.insert(10, string)
    return(x,y,z)
		


# Driver Code
if __name__ == "__main__" :
	

	# Create a GUI window
    gui = Tk()
	# Set the background colour of GUI window
    gui.config(background = "#B3E5FC")

	# set the name of tkinter GUI window
    gui.title("Sentiment Detector")
    windowWidth = gui.winfo_reqwidth()
    windowHeight = gui.winfo_reqheight()
    print("Width",windowWidth,"Height",windowHeight)
    positionRight = int(gui.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(gui.winfo_screenheight()/2 - windowHeight/2)
    gui.geometry("+{}+{}".format(positionRight, positionDown))

	# Set the configuration of GUI window
    #gui.geometry("250x400")

	# create a label : Enter Your Task
    enterText = Label(gui, text = "Enter Your Sentence",
									bg = "#BCD9EA")

	# create a text area for the root
	# with lunida 13 font
	# text area is for writing the content
    textArea = Text(gui, height = 5, width = 70, font = "lucida 13")

	# create a Submit Button and place into the root window
	# when user press the button, the command or
	# function affiliated to that button is executed
    check = Button(gui, text = "Check Sentiment", fg = "Black",
						bg = "#81D4FA", command = detect_sentiment)

	# Create a negative : label
    negative = Label(gui, text = "Negative Percentage: ",
										bg = "#BCD9EA")

	# Create a neutral : label
    neutral = Label(gui, text = "Neutral Percentage: ",
									bg = "#BCD9EA")

	# Create a positive : label
    positive = Label(gui, text = "Positive Percentage: ",
										bg = "#BCD9EA")

	# Create a overall : label
    overall = Label(gui, text = "Sentence Overall Rated As: ",
									bg = "#BCD9EA")

	# create a text entry box
    negativeField = Entry(gui)

	# create a text entry box
    neutralField = Entry(gui)

	# create a text entry box
    positiveField = Entry(gui)

	# create a text entry box
    overallField = Entry(gui)



	# create a Clear Button and place into the root window
	# when user press the button, the command or
	# function affiliated to that button is executed .
    clear = Button(gui, text = "Clear", fg = "Black",
					bg = "#81D4FA", command = clearAll)
	

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure.
    enterText.grid(row = 0, column = 2 ,padx=10, pady=(5,30))
	
    textArea.grid(row = 1, column = 2, padx = 100)
	
    check.grid(row = 2, column = 2, padx=100, pady=(5,40))
	
    negative.grid(row = 3, column = 2, padx=100)
	
    neutral.grid(row = 5, column = 2)
	
    positive.grid(row = 7, column = 2)
	
    overall.grid(row = 9, column = 2)
	
    negativeField.grid(row = 4, column = 2, padx=10, pady=(5,30))

    neutralField.grid(row = 6, column = 2,padx=10, pady=(5,30))
					
    positiveField.grid(row = 8, column = 2,padx=10, pady=(5,30))
	
    overallField.grid(row = 10, column = 2,padx=10, pady=(5,30))
	
    clear.grid(row = 11, column = 2,padx=10, pady=(5,30))

    c = tk.Canvas(gui, width=200, height=200)    
    
 
    
    root= tk.Tk()
    
    canvas1 = tk.Canvas(root, width = 800, height = 300)
    canvas1.pack()
    label1 = tk.Label(root, text='Pie Chart')
    label1.config(font=('Arial', 20))
    canvas1.create_window(400, 50, window=label1)
    
    def create_charts():
        global x1
        global x2
        global x3
        global pie2
        x1 = float(negativeField.get())
        print(x1)
        x2 = float(neutralField.get())
        print(x2)
        x3 = float(positiveField.get())
        print(x3)

        figure2 = Figure(figsize=(4,3), dpi=100) 
        subplot2 = figure2.add_subplot(111) 
        labels2 = 'Negative', 'Neutral', 'Positive' 
        pieSizes = [float(x1),float(x2),float(x3)]
        my_colors2 = ['#bcd9ea','#0079bf','#5ba4cf']
        explode2 = (0, 0.1, 0)  
        subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90) 
        subplot2.axis('equal')  
        pie2 = FigureCanvasTkAgg(figure2, root)
        pie2.get_tk_widget().pack()
    
    def clear_charts():
        pie2.get_tk_widget().pack_forget()
            
    button1 = tk.Button (root, text=' Create Charts ',command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold')) 
    canvas1.create_window(400, 180, window=button1)
    
    button2 = tk.Button (root, text='  Clear Charts  ', command=clear_charts, bg='lightskyblue2', font=('Arial', 11, 'bold'))
    canvas1.create_window(400, 220, window=button2)
    root,gui.mainloop()



	
    
	
