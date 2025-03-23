import tkinter as tk
from tkinter import messagebox
import subprocess

# Define users
git_users = {
    "pappukrs": ("digitalpappu101@gmail.com"),
    "codeserver111": ("codeserver111@gmail.com"),
    "pappukh": ("khautomations.pappu@gmail.com"),
    "pappukrs123": ("pappu@sensegrass.com")
}

# Function to set Git user
def set_git_user(username, email):
    try:
        subprocess.run(["git", "config", "user.name", username], check=True)
        subprocess.run(["git", "config", "user.email", email], check=True)
        messagebox.showinfo("Success", f"Git user set to {username}\nEmail: {email}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to set Git user.\n{e}")

# Create GUI Window
root = tk.Tk()
root.title("Git User Selector")
root.geometry("300x250")

tk.Label(root, text="Select Git User:", font=("Arial", 14)).pack(pady=10)

# Create buttons for each user
for user, email in git_users.items():
    tk.Button(root, text=user, command=lambda u=user, e=email: set_git_user(u, e), width=20, font=("Arial", 12)).pack(pady=5)

# Run the GUI
root.mainloop()
