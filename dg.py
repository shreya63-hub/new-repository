


from tkinter import *

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.listbox = Listbox(self.root)
        self.listbox.pack(padx=10, pady=10)
        self.entry = Entry(self.root)
        self.entry.pack(padx=10, pady=5)
        self.addButton = Button(self.root, text="Add Task", command=self.add_task)
        self.addButton.pack(padx=10, pady=5)
        self.delButton = Button(self.root, text="Delete Task", command=self.delete_task)
        self.delButton.pack(padx=10, pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except:
            pass

root = Tk()
root.title("Python To-Do List")
root.geometry("300x400")

to_do_list = ToDoList(root)
root.mainloop()

