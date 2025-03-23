import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

# Define Git users
git_users = {
    "pappukrs": "digitalpappu101@gmail.com",
    "codeserver111": "codeserver111@gmail.com",
    "pappukh": "khautomations.pappu@gmail.com",
    "pappukrs123": "pappu@sensegrass.com"
}

# Function to set Git user in selected repo
def set_git_user(username, email):
    repo_path = filedialog.askdirectory(title="Select Git Repository")
    
    if not repo_path:
        messagebox.showerror("Error", "No repository selected.")
        return

    if not os.path.isdir(os.path.join(repo_path, ".git")):
        messagebox.showerror("Error", "Selected folder is not a Git repository.")
        return

    try:
        subprocess.run(["git", "-C", repo_path, "config", "user.name", username], check=True)
        subprocess.run(["git", "-C", repo_path, "config", "user.email", email], check=True)
        messagebox.showinfo("Success", f"Git user set to {username}\nEmail: {email}\nRepo: {repo_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to set Git user.\nError: {e}")

# Create GUI Window
root = tk.Tk()
root.title("Git User Selector")
root.geometry("350x300")

tk.Label(root, text="Select Git User:", font=("Arial", 14)).pack(pady=10)

# Create buttons for each user
for user, email in git_users.items():
    tk.Button(root, text=user, command=lambda u=user, e=email: set_git_user(u, e), width=25, font=("Arial", 12)).pack(pady=5)

root.mainloop()
