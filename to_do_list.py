import tkinter
import tkinter.messagebox
import pickle

window=tkinter.Tk()
#window.geometry("250x250")
window.maxsize(800,800)
window.title("To Do List")
# tat=Label(text="This is my today's to-do list")
# tat.pack()

#frame
list_frame=tkinter.Frame(window)
list_frame.pack()
todo_box=tkinter.Listbox(list_frame,height=20, width=50)

todo_box.pack(side=tkinter.LEFT)

#Scroll up and down through the page
scroller=tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)

#add task
todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command=list_frame.yview)
task_add=tkinter.Entry(window,width=70,background="light blue", relief="groove")
task_add.pack() 



#function to add task
def task_adding():
    todo=task_add.get()
    if todo !="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(message="Please enter a task to add!")
        

# function to delete the task
def task_removing():
    try:
        index_todo=list_frame.curselection()[0]
        list_frame.delete(index_todo) 
    except:
        tkinter.messagebox.showwarning(message="Please choose a task to delete!")


#function to load tasks
def task_load():
    try:
        todo_list=pickle.load(open("tasks.dat","rb"))
        list_frame.delete(0,tkinter.END)
        for todo in tasks: 
            list_frame.insert(tkinter.END,todo )
    except:
        tkinter.messagebox.showwarning(message="Cannot find task.dat")


#function to save task
def task_save():
    todo_list=list_frame.get(0,list_frame.size())
    pickle.dump(todo_list,open("tasks.dat","wb"))


    #add text button
add_task_button=tkinter.Button(window,
     text="Add Task", font=("georgia 10 bold"),
     background="green",
     width=15,
     padx=2,
     pady=2,
     relief="raised",
     command=task_adding
)
add_task_button.pack(side="left")

#delete button
remove_task_button=tkinter.Button(window,
     text="Delete Task", font=("georgia 10 bold"),
     background= "red",
     height=1,
     width=15,
     padx=2,
     pady=2,
     relief="raised",
     command=task_removing 
)
remove_task_button.pack(side="right")

#load task button
load_task_button=tkinter.Button(window,
     text="Load Tasks", font=("georgia 10 bold"),
     background= "yellow",
     height=1,
     width=15,
     padx=2,
     pady=2,
     relief="raised",
     command=task_load
)
load_task_button.pack(side="bottom",anchor="sw")

#save task button
save_task_button=tkinter.Button(window,
     text="Save", font=("georgia 10 bold"),
     background= "orange",
     height=1,
     width=15,
     padx=2,
     pady=2,
     relief="raised",
     command=task_save
)
save_task_button.pack(side="bottom",anchor="se")


window.mainloop()