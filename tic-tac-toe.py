from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "      " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"

            
      ##judgement for win
      row = i//3
      col = i%3
      
      ##if 3 row elements are straight, win
      if list[(row*3)]["text"] == list[(row*3) + 1]["text"] == list[(row*3) + 2]["text"] != "      " :
            win()
      
      ##if 3 column elements are straight, win
      if list[(col)]["text"] == list[col+3]["text"] == list[col+6]["text"] != "      " :
            win()
      
      ##if 3 elements are straight for diagonal, win
      if list[0]["text"] == list[4]["text"] == list[8]["text"] != "      " :
            win()
      if list[2]["text"] == list[4]["text"] == list[6]["text"] != "      " :
            win()

      
##message for win
def win() :
      global flag
      if flag == False :
            msg = Message(window, text = "WIN!")
            msg.grid(row = 3, column = 0)
      flag = True
      
      
window = Tk()
player = "X"
list= []

flag = False

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


