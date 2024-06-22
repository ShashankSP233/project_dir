import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
        save_tasks()
    except IndexError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = listbox_tasks.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("600x400")  # Larger default window size
root.configure(bg="lightblue")  # Setting the background color

listbox_tasks = tk.Listbox(root, height=15, width=40, font=("Arial", 12), bg="lightgreen")  # Larger Listbox
listbox_tasks.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Using grid for the listbox

scrollbar_tasks = tk.Scrollbar(root)
scrollbar_tasks.grid(row=0, column=1, sticky="ns")  # Using grid for the scrollbar

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50, font=("Arial", 12))  # Entry field
entry_task.grid(row=1, column=0, padx=10, pady=5)  # Using grid for the entry field

button_add_task = tk.Button(root, text="Add Task", width=15, command=add_task, font=("Arial", 12))  # Add Task button
button_add_task.grid(row=2, column=0, padx=10, pady=5)  # Using grid for Add Task button

button_delete_task = tk.Button(root, text="Delete Task", width=15, command=delete_task, font=("Arial", 12))  # Delete Task button
button_delete_task.grid(row=3, column=0, padx=10, pady=5)  # Using grid for Delete Task button

load_tasks()

root.grid_rowconfigure(0, weight=1)  # Row 0 of root grid should expand vertically
root.grid_columnconfigure(0, weight=1)  # Column 0 of root grid should expand horizontally

root.mainloop()
