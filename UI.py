import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Streak Study App")
root.geometry("800x600")
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 14))

nav_frame = tk.Frame(root, bg="#f0f0f0")
nav_frame.pack(side="left", fill="y")

screens = [
    "🏠 Home Dashboard", "📚 Learning Module", "🔥 Streak Tracker",
    "🎖 Rewards Center", "🧠 Quiz Zone", "👤 Profile", "🔔 Notification Hub"
]

def show_screen(name):
    for widget in content_frame.winfo_children():
        widget.destroy()
    ttk.Label(content_frame, text=name, font=("Helvetica", 20, "bold")).pack(pady=20)
    ttk.Label(content_frame, text="Coming soon: Emotional + gamified features!").pack()

for screen in screens:
    ttk.Button(nav_frame, text=screen, command=lambda s=screen: show_screen(s)).pack(fill="x", pady=5)

content_frame = tk.Frame(root, bg="white")
content_frame.pack(side="right", expand=True, fill="both")

show_screen("🏠 Home Dashboard")

root.mainloop()