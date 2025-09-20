import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import pyperclip
from core.message_handler import SecureCommunicator

class SecureChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hybrid Crypto Secure Chat")
        self.user1 = SecureCommunicator()
        self.user2 = SecureCommunicator()
        # Exchange DH public keys and create shared keys
        self.user1.create_shared_key(self.user2.dh_public_key)
        self.user2.create_shared_key(self.user1.dh_public_key)
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(root, width=70, height=20, state='disabled', font=('Arial', 10), bg='#f0f0f0')
        self.chat_display.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.chat_display.tag_configure('bold', font=('Arial', 10, 'bold'))
        self.chat_display.tag_configure('black', foreground='black')
        self.chat_display.tag_configure('blue', foreground='blue')
        self.chat_display.tag_configure('green', foreground='green')
        self.chat_display.tag_configure('red', foreground='red')
        # Encrypted messages display
        self.encrypted_display = scrolledtext.ScrolledText(root, width=70, height=10, state='disabled', font=('Courier New', 9), bg='#e8e8e8')
        self.encrypted_display.grid(row=1, column=0, columnspan=3, padx=10)
        # Entry box
        self.message_entry = tk.Entry(root, width=58, font=('Arial', 12))
        self.message_entry.grid(row=2, column=0, padx=10, pady=10)
        # Buttons
        send_button = tk.Button(root, text="Send from USER_1", command=self.send_message_user1)
        send_button.grid(row=2, column=1, padx=5)
        send_button_user2 = tk.Button(root, text="Send from USER_2", command=self.send_message_user2)
        send_button_user2.grid(row=2, column=2, padx=5)
        clear_button = tk.Button(root, text="Clear Chat", command=self.clear_chat)
        clear_button.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        copy_button = tk.Button(root, text="Copy Encrypted", command=self.copy_encrypted)
        copy_button.grid(row=3, column=2, padx=10, pady=5, sticky='e')
    def display_message(self, sender, message, color="black"):
        time_str = datetime.now().strftime("%H:%M:%S")
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"[{time_str}] {sender}: ", ('bold', color))
        self.chat_display.insert(tk.END, f"{message}\n", (color,))
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
    def display_encrypted(self, encrypted_text):
        self.encrypted_display.config(state='normal')
        self.encrypted_display.insert(tk.END, f"{encrypted_text}\n")
        self.encrypted_display.config(state='disabled')
        self.encrypted_display.see(tk.END)
    def clear_chat(self):
        self.chat_display.config(state='normal')
        self.chat_display.delete('1.0', tk.END)
        self.chat_display.config(state='disabled')
        self.encrypted_display.config(state='normal')
        self.encrypted_display.delete('1.0', tk.END)
        self.encrypted_display.config(state='disabled')
    def copy_encrypted(self):
        encrypted_text = self.encrypted_display.get('1.0', tk.END).strip()
        if encrypted_text:
            pyperclip.copy(encrypted_text)
            messagebox.showinfo("Copied", "Encrypted text copied to clipboard")
        else:
            messagebox.showwarning("Empty", "No encrypted text to copy")
    def send_message_user1(self):
        message = self.message_entry.get().strip()
        if not message:
            messagebox.showerror("Error", "Message cannot be empty")
            return
        self.display_message("USER_1 (Original)", message, "black")
        try:
            signature = self.user1.sign_message(message)
            iv, encrypted = self.user1.encrypt_message(message)
            self.display_encrypted(encrypted)
            self.display_message("USER_1 (Encrypted)", "[See Encrypted Box]", "blue")
            decrypted = self.user2.decrypt_message(iv, encrypted)
            self.display_message("USER_2 (Decrypted)", decrypted, "green")
            valid = self.user2.verify_signature(message, signature, self.user1.public_key)
            sig_msg = "Signature Valid" if valid else "Signature Invalid"
            self.display_message("USER_2 (Signature)", sig_msg, "green" if valid else "red")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        self.message_entry.delete(0, tk.END)
    def send_message_user2(self):
        message = self.message_entry.get().strip()
        if not message:
            messagebox.showerror("Error", "Message cannot be empty")
            return
        self.display_message("USER_2 (Original)", message, "black")
        try:
            signature = self.user2.sign_message(message)
            iv, encrypted = self.user2.encrypt_message(message)
            self.display_encrypted(encrypted)
            self.display_message("USER_2 (Encrypted)", "[See Encrypted Box]", "blue")
            decrypted = self.user1.decrypt_message(iv, encrypted)
            self.display_message("USER_1 (Decrypted)", decrypted, "green")
            valid = self.user1.verify_signature(message, signature, self.user2.public_key)
            sig_msg = "Signature Valid" if valid else "Signature Invalid"
            self.display_message("USER_1 (Signature)", sig_msg, "green" if valid else "red")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        self.message_entry.delete(0, tk.END)
if __name__=="__main__":
    root = tk.Tk()
    app = SecureChatGUI(root)
    root.mainloop()
