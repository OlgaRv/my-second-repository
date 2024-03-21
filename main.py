import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def del_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="chocolate")

root = tk.Tk()
root.title("Task list")
root.configure(background="aquamarine")

text1 = tk.Label(root, text="Введите задачу: ", bg="aquamarine")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="blue violet",fg="white")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

del_task_button = tk.Button(root, text="Удалить задачу", command=del_task)
del_task_button.pack(pady=5)

mark_task_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_task_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач: ", bg="aquamarine")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=10, width=50, bg="DarkSlateGray1")
task_listBox.pack(pady=10)

root.mainloop()