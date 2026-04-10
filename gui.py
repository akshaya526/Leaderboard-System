import tkinter as tk
from client_secure import SecureClient

def update_display(data):
    def update():
        leaderboard_box.delete(0, tk.END)
        for line in data.split("\n"):
            if line.strip():
                leaderboard_box.insert(tk.END, line)

    root.after(0, update)


def connect_to_server():
    global client
    host = ip_entry.get().strip()
    if not host:
        host = "127.0.0.1"
    
    try:
        client = SecureClient(update_display, host)
        connect_button.config(state=tk.DISABLED, text="Connected")
        update_button.config(state=tk.NORMAL)
        refresh_button.config(state=tk.NORMAL)
        print(f"Connected to {host}")
    except Exception as e:
        print(f"Failed to connect: {e}")
        leaderboard_box.delete(0, tk.END)
        leaderboard_box.insert(tk.END, f"Error: Could not connect to {host}")
        leaderboard_box.insert(tk.END, str(e))


def send_update():
    if not client: return
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
    if not client: return
    print("Refreshing leaderboard...")   # debug
    client.get_leaderboard()


# UI Setup
root = tk.Tk()
root.title("Secure Leaderboard System")
root.geometry("400x600")

tk.Label(root, text="Leaderboard System", font=("Arial", 16, "bold")).pack(pady=10)

# Connection Frame
conn_frame = tk.LabelFrame(root, text="Connection Settings")
conn_frame.pack(pady=10, fill="x", padx=10)

tk.Label(conn_frame, text="Server IP:").grid(row=0, column=0, padx=5, pady=5)
ip_entry = tk.Entry(conn_frame)
ip_entry.insert(0, "127.0.0.1")
ip_entry.grid(row=0, column=1, padx=5, pady=5)

connect_button = tk.Button(conn_frame, text="Connect", command=connect_to_server)
connect_button.grid(row=0, column=2, padx=5, pady=5)

# Input Frame
frame = tk.LabelFrame(root, text="Update Score")
frame.pack(pady=10, fill="x", padx=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Score").grid(row=1, column=0, padx=5, pady=5)
score_entry = tk.Entry(frame)
score_entry.grid(row=1, column=1, padx=5, pady=5)

# Buttons
update_button = tk.Button(root, text="Update Score", width=20, command=send_update, state=tk.DISABLED)
update_button.pack(pady=5)
refresh_button = tk.Button(root, text="Refresh Leaderboard", width=20, command=refresh, state=tk.DISABLED)
refresh_button.pack(pady=5)

# Leaderboard display
leaderboard_box = tk.Listbox(root, width=40, height=15)
leaderboard_box.pack(pady=10)


# Initialize client as None
client = None

root.mainloop()