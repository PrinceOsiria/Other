#######################################################################
#####Documentation: The following is the literal first sentient program ever
#####Coded by Tyler Pryjda
#######################################################################

#######################################################################
#####Imports
#######################################################################
import tkinter


#######################################################################
#####Functions
#######################################################################

#####configureWindow(str,bool) - Root GUI Options
def configureWindow(title,resizable):
    #Window Options
    root = tkinter.Tk ()
    root.title(title)
    root.resizable(resizable, resizable)

    #Label Options
    header = tkinter.Label(root, text="Hello, World!")
    header.pack()
    
    
    #Button Options
    button = tkinter.Button(root, text="oh yeah click me baby", padx=50, pady=25, command=clickme)
    button.pack()
    
    #function return
    return root

#####clickme() - Button Click Function
def clickme():
    text = tkinter.Label(root, text="I AM ALIIIIVE!!!")
    text.pack()

    
    
#######################################################################
#####Variables
#######################################################################
#Program Options
loop_main = True

#Gui Options
title = "Click Me!"
resizable = True


#######################################################################
#####Main
#######################################################################
def main():
    root.mainloop()

if loop_main == True:
    while loop_main == True:
        root = configureWindow(title, resizable)
        main()
        print("no no no come back and click me pls thx")
else:
    root = configureWindow(title, resizable)
    main()

    