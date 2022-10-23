from tkinter.font import Font
from tkinter import *


class ToDoList:

    def __init__(self):

        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("My ToDo List")

        self.myFont = Font(family='Arial', size=18, weight="bold")

        self.myFrame = Frame(self.root)
        self.myFrame.pack(pady=20)

        self.myList = Listbox(
            self.myFrame,
            font=self.myFont,
            width=30, height=5,
            bg="SystemButtonFace",
            bd=0,
            fg="#464646",
            highlightthickness=0,
            selectbackground="#a6a6a6",
            activestyle="none"
        )
        self.myList.pack(side=LEFT, fill=BOTH)

        self.myStuff = ["finish homework", "do laundry", "buy a milk", "call the doctor",
                        "clean my room", "clean my room 2"]
        for item in self.myStuff:
            self.myList.insert(END, item)

        # Create scrollbar
        self.myScrollbar = Scrollbar(self.myFrame)
        self.myScrollbar.pack(side=RIGHT, fill=BOTH)

        # Add scrollbar
        self.myList.config(yscrollcommand=self.myScrollbar.set)
        self.myScrollbar.config(command=self.myList.yview)

        # create text box to add items to the list
        self.myEntry = Entry(self.root, font=("Helvetica", 24))
        self.myEntry.pack(pady=20)

        # Create a buttons frame
        self.myButtonsFrame = Frame(self.root)
        self.myButtonsFrame.pack(pady=20)

        # Create a buttons
        self.deleteButton = Button(self.myButtonsFrame, text="Delete task", command=self.delete_task)
        self.addButton = Button(self.myButtonsFrame, text="Add task", command=self.add_task)
        self.crossOffButton = Button(self.myButtonsFrame, text="cross off task", command=self.cross_off_task)
        self.delCrossButton = Button(self.myButtonsFrame, text="delete crossed task", command=self.delete_crossed_task)

        self.addButton.grid(row=0, column=0)
        self.deleteButton.grid(row=0, column=1, padx=20)
        self.crossOffButton.grid(row=0, column=2)
        self.delCrossButton.grid(row=0, column=3, padx=20)

        self.root.mainloop()

    # Buttons functions
    def delete_task(self):
        self.myList.delete(ANCHOR)

    def add_task(self):
        self.myList.insert(END, self.myEntry.get())
        self.myEntry.delete(0, END)

    def cross_off_task(self):
        pass

    def delete_crossed_task(self):
        pass