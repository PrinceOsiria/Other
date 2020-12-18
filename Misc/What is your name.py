#######################################################################
#####Documentation: The following is a sick roast generator
#####Coded by Tyler Pryjda
#######################################################################


#######################################################################
#####Imports
#######################################################################
import tkinter


#######################################################################
#####Functions
#######################################################################

#####namebutton() - Accepts input from nameEntry for user name
def nameButton():

    #Variables
        #User Entry & cleartext
    name = str(nameEntry.get()).lower()
    cleartext = "\t\t\t\t"
        #Roasts
    default = name + "? More like DUMB!"
    dumb = name + "? More like SMART!"
    smart = name + "? More like GENIUS!!!"
    genius = name + "? More like DUMB! BAM FRIGGIN GOTEM SON!!!"
    tyler = name + "? Oh, hey dude. Long time no see!"
    poop = "you smell like " + name
    pee = "you drink " + name

    insult = tkinter.Label(root, text=cleartext)
    insult.grid(row=1,column=0)

    if name == "dumb":
        insult = tkinter.Label(root, text=dumb)  
    elif name == "smart":
        insult = tkinter.Label(root, text=smart)
    elif name == "genius":
        insult = tkinter.Label(root, text=genius)
    elif name == "tyler":
        insult = tkinter.Label(root, text=tyler)
    elif name == "poop":
        insult = tkinter.Label(root, text=poop)
    elif name == "pee":
        insult = tkinter.Label(root, text=pee)
    else:
        insult = tkinter.Label(root, text=default)
    
    insult.grid(row=1,column=0)    

    
    
#######################################################################
#####Variables
#######################################################################

    #Window Options
root = tkinter.Tk ()
root.title("Title")
root.resizable(False, True)
    
    #Label Options
greeting = tkinter.Label(root, text="Welcome! What is your name?")
greeting.grid(row=0,column=0)
    
    #Entry Options
nameEntry = tkinter.Entry(root, width=50, borderwidth=5)
nameEntry.grid(row=0, column=1)
    
    #Button Options
nameButton = tkinter.Button(root, text="[ ENTER ]", command=nameButton)
nameButton.grid(row=0, column=2)




#######################################################################
#####Main
#######################################################################

root.mainloop()
nameEntry = tkinter.Entry(root, width=50, borderwidth=5)


    