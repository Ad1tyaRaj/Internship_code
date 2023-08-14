import tkinter as tk
from tkinter import messagebox



class My_TodoList:
    def __init__(self, root):
        self.root = root
        self.root.title("My Todo List")
        self.My_tasks = []

        self.Mytask_entry = tk.Entry(root, width=40)
        self.Mytask_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task,bg="#89ff74")
        self.add_button.grid(row=0, column=2, padx=5, pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task,bg='#ff884d')
        self.remove_button.grid(row=1, column=2, padx=5, pady=5)

        self.clear_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks,bg='#bcf720')
        self.clear_button.grid(row=2, column=0, padx=5, pady=5)

        self.exit_button = tk.Button(root, text="Exit",command=self.exit_app,bg='#0cfffc')
        self.exit_button.grid(row=2, column=1, padx=5, pady=5)

        self.Mytask_listbox = tk.Listbox(root, width=50,bg='#d5d5d5')
        self.Mytask_listbox.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

        self.update_listbox()

    def add_task(self):
        task = self.Mytask_entry.get()
        if task:
            self.My_tasks.append(task)
            self.Mytask_entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.Mytask_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            del self.My_tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def clear_tasks(self):
        self.Mytask_listbox.delete(0, tk.END)

    def exit_app(self):
        self.root.destroy()

    def update_listbox(self):
        self.Mytask_listbox.delete(0, tk.END)
        for task in self.My_tasks:
            self.Mytask_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    this_app = My_TodoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()
