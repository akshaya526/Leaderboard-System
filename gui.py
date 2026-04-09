import tkinter as tk
from client_secure import SecureClient

def update_display(data):
    def update():
        leaderboard_box.delete(0, tk.END)
        for line in data.split("\n"):
            if line.strip():
                leaderboard_box.insert(tk.END, line)

    root.after(0, update)


def send_update():
    name = name_entry.get().strip()
    score = score_entry.get().strip()

    if name and score and score.isdigit():
        client.update_score(name, score)

        # Clear fields
        name_entry.delete(0, tk.END)
        score_entry.delete(0, tk.END)
        name_entry.focus()
    else:
        print("Invalid input")


def refresh():
    print("Refreshing leaderboard...")   # debug
    client.get_leaderboard()


# UI Setup
root = tk.Tk()
root.title("Secure Leaderboard System")
root.geometry("400x500")

tk.Label(root, text="Leaderboard System", font=("Arial", 16, "bold")).pack(pady=10)

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Score").grid(row=1, column=0, padx=5)
score_entry = tk.Entry(frame)
score_entry.grid(row=1, column=1, padx=5)

# Buttons
tk.Button(root, text="Update Score", width=20, command=send_update).pack(pady=5)
tk.Button(root, text="Refresh Leaderboard", width=20, command=refresh).pack(pady=5)

# Leaderboard display
leaderboard_box = tk.Listbox(root, width=40, height=15)
leaderboard_box.pack(pady=10)


# Start client
client = SecureClient(update_display)

root.mainloop()