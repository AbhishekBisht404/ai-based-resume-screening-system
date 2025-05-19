import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.title = tk.Label(root, text="My Tasks", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.build_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Input error", "Task cannot be empty!")
            return
        task = {"text": text, "completed": False}
        self.tasks.append(task)
        self.task_var.set("")
        self.build_task_list()

    def toggle_task(self, i):
        self.tasks[i]["completed"] = not self.tasks[i]["completed"]
        self.build_task_list()

    def delete_task(self, i):
        del self.tasks[i]
        self.build_task_list()

    def build_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame)
            frame.pack(fill="x", pady=2, padx=5)

            var = tk.IntVar(value=1 if task["completed"] else 0)
            check = tk.Checkbutton(
                frame,
                text=task["text"],
                variable=var,
                font=("Helvetica", 12),
                command=lambda i=i: self.toggle_task(i),
                anchor="w"
            )
            if task["completed"]:
                check.config(fg="gray")
            check.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.title = tk.Label(root, text="My Tasks", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.build_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Input error", "Task cannot be empty!")
            return
        task = {"text": text, "completed": False}
        self.tasks.append(task)
        self.task_var.set("")
        self.build_task_list()

    def toggle_task(self, i):
        self.tasks[i]["completed"] = not self.tasks[i]["completed"]
        self.build_task_list()

    def delete_task(self, i):
        del self.tasks[i]
        self.build_task_list()

    def build_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame)
            frame.pack(fill="x", pady=2, padx=5)

            var = tk.IntVar(value=1 if task["completed"] else 0)
            check = tk.Checkbutton(
                frame,
                text=task["text"],
                variable=var,
                font=("Helvetica", 12),
                command=lambda i=i: self.toggle_task(i),
                anchor="w"
            )
            if task["completed"]:
                check.config(fg="gray")
            check.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.title = tk.Label(root, text="My Tasks", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.build_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Input error", "Task cannot be empty!")
            return
        task = {"text": text, "completed": False}
        self.tasks.append(task)
        self.task_var.set("")
        self.build_task_list()

    def toggle_task(self, i):
        self.tasks[i]["completed"] = not self.tasks[i]["completed"]
        self.build_task_list()

    def delete_task(self, i):
        del self.tasks[i]
        self.build_task_list()

    def build_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame)
            frame.pack(fill="x", pady=2, padx=5)

            var = tk.IntVar(value=1 if task["completed"] else 0)
            check = tk.Checkbutton(
                frame,
                text=task["text"],
                variable=var,
                font=("Helvetica", 12),
                command=lambda i=i: self.toggle_task(i),
                anchor="w"
            )
            if task["completed"]:
                check.config(fg="gray")
            check.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.title = tk.Label(root, text="My Tasks", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.build_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Input error", "Task cannot be empty!")
            return
        task = {"text": text, "completed": False}
        self.tasks.append(task)
        self.task_var.set("")
        self.build_task_list()

    def toggle_task(self, i):
        self.tasks[i]["completed"] = not self.tasks[i]["completed"]
        self.build_task_list()

    def delete_task(self, i):
        del self.tasks[i]
        self.build_task_list()

    def build_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame)
            frame.pack(fill="x", pady=2, padx=5)

            var = tk.IntVar(value=1 if task["completed"] else 0)
            check = tk.Checkbutton(
                frame,
                text=task["text"],
                variable=var,
                font=("Helvetica", 12),
                command=lambda i=i: self.toggle_task(i),
                anchor="w"
            )
            if task["completed"]:
                check.config(fg="gray")
            check.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()


import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.title = tk.Label(root, text="My Tasks", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.build_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Input error", "Task cannot be empty!")
            return
        task = {"text": text, "completed": False}
        self.tasks.append(task)
        self.task_var.set("")
        self.build_task_list()

    def toggle_task(self, i):
        self.tasks[i]["completed"] = not self.tasks[i]["completed"]
        self.build_task_list()

    def delete_task(self, i):
        del self.tasks[i]
        self.build_task_list()

    def build_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame)
            frame.pack(fill="x", pady=2, padx=5)

            var = tk.IntVar(value=1 if task["completed"] else 0)
            check = tk.Checkbutton(
                frame,
                text=task["text"],
                variable=var,
                font=("Helvetica", 12),
                command=lambda i=i: self.toggle_task(i),
                anchor="w"
            )
            if task["completed"]:
                check.config(fg="gray")
            check.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.title = tk.Label(root, text="My Tasks", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.build_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Input error", "Task cannot be empty!")
            return
        task = {"text": text, "completed": False}
        self.tasks.append(task)
        self.task_var.set("")
        self.build_task_list()

    def toggle_task(self, i):
        self.tasks[i]["completed"] = not self.tasks[i]["completed"]
        self.build_task_list()

    def delete_task(self, i):
        del self.tasks[i]
        self.build_task_list()

    def build_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame)
            frame.pack(fill="x", pady=2, padx=5)

            var = tk.IntVar(value=1 if task["completed"] else 0)
            check = tk.Checkbutton(
                frame,
                text=task["text"],
                variable=var,
                font=("Helvetica", 12),
                command=lambda i=i: self.toggle_task(i),
                anchor="w"
            )
            if task["completed"]:
                check.config(fg="gray")
            check.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.title = tk.Label(root, text="My Tasks", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.build_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Input error", "Task cannot be empty!")
            return
        task = {"text": text, "completed": False}
        self.tasks.append(task)
        self.task_var.set("")
        self.build_task_list()

    def toggle_task(self, i):
        self.tasks[i]["completed"] = not self.tasks[i]["completed"]
        self.build_task_list()

    def delete_task(self, i):
        del self.tasks[i]
        self.build_task_list()

    def build_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame)
            frame.pack(fill="x", pady=2, padx=5)

            var = tk.IntVar(value=1 if task["completed"] else 0)
            check = tk.Checkbutton(
                frame,
                text=task["text"],
                variable=var,
                font=("Helvetica", 12),
                command=lambda i=i: self.toggle_task(i),
                anchor="w"
            )
            if task["completed"]:
                check.config(fg="gray")
            check.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.title = tk.Label(root, text="My Tasks", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.build_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Input error", "Task cannot be empty!")
            return
        task = {"text": text, "completed": False}
        self.tasks.append(task)
        self.task_var.set("")
        self.build_task_list()

    def toggle_task(self, i):
        self.tasks[i]["completed"] = not self.tasks[i]["completed"]
        self.build_task_list()

    def delete_task(self, i):
        del self.tasks[i]
        self.build_task_list()

    def build_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame)
            frame.pack(fill="x", pady=2, padx=5)

            var = tk.IntVar(value=1 if task["completed"] else 0)
            check = tk.Checkbutton(
                frame,
                text=task["text"],
                variable=var,
                font=("Helvetica", 12),
                command=lambda i=i: self.toggle_task(i),
                anchor="w"
            )
            if task["completed"]:
                check.config(fg="gray")
            check.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "tasks.json"

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self.title = tk.Label(root, text="My Tasks", font=("Helvetica", 16, "bold"))
        self.title.pack(pady=10)

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.frame, textvariable=self.task_var, width=25)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root)
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.task_frame = tk.Frame(self.canvas)

        self.task_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.task_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.build_task_list()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        text = self.task_var.get().strip()
        if not text:
            messagebox.showwarning("Input error", "Task cannot be empty!")
            return
        task = {"text": text, "completed": False}
        self.tasks.append(task)
        self.task_var.set("")
        self.build_task_list()

    def toggle_task(self, i):
        self.tasks[i]["completed"] = not self.tasks[i]["completed"]
        self.build_task_list()

    def delete_task(self, i):
        del self.tasks[i]
        self.build_task_list()

    def build_task_list(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            frame = tk.Frame(self.task_frame)
            frame.pack(fill="x", pady=2, padx=5)

            var = tk.IntVar(value=1 if task["completed"] else 0)
            check = tk.Checkbutton(
                frame,
                text=task["text"],
                variable=var,
                font=("Helvetica", 12),
                command=lambda i=i: self.toggle_task(i),
                anchor="w"
            )
            if task["completed"]:
                check.config(fg="gray")
            check.pack(side="left", fill="x", expand=True)

            del_btn = tk.Button(frame, text="🗑", command=lambda i=i: self.delete_task(i))
            del_btn.pack(side="right")

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()

