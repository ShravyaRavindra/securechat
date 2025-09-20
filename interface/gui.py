import tkinter as tk
from tkinter import scrolledtext, messagebox
from core.message_handler import SecureCommunicator

class SecureChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hybrid Crypto Secure Chat")

        self.alice = SecureCommunicator()
        self.bob = SecureCommunicator()

        # Exchange DH public keys and create shared keys
        self.alice.create_shared_key(self.bob.dh_public_key)
        self.bob.create_shared_key(self.alice.dh_public_key)

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(root, width=60, height=20, state='disabled')
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Message input box
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.grid(row=1, column=0, padx=10, pady=5)

        # Send button
        send_button = tk.Button(root, text="Send from Alice", command=self.send_message_alice)
        send_button.grid(row=1, column=1, padx=10)

        send_button_bob = tk.Button(root, text="Send from Bob", command=self.send_message_bob)
        send_button_bob.grid(row=2, column=1, padx=10)

    def display_message(self, sender, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def send_message_alice(self):
      message = self.message_entry.get()
      print(f"Alice sends: {message}")  # For debugging, see in terminal
      if not message.strip():
         messagebox.showerror("Error", "Message cannot be empty")
         return
      self.display_message("Alice (Original)", message)
      try:
        signature = self.alice.sign_message(message)
        iv, encrypted = self.alice.encrypt_message(message)
        decrypted = self.bob.decrypt_message(iv, encrypted)
        is_valid = self.bob.verify_signature(message, signature, self.alice.public_key)
        self.display_message("Bob (Decrypted)", decrypted)
        self.display_message("Bob (Signature Verified)", str(is_valid))
      except Exception as e:
        messagebox.showerror("Error", str(e))
      self.message_entry.delete(0, tk.END)


    def send_message_bob(self):
        message = self.message_entry.get()
        if not message.strip():
           messagebox.showerror("Error", "Message cannot be empty")
           return
        self.display_message("Bob (Original)", message)

    # Bob signs the message
        signature = self.bob.sign_message(message)

    # Bob encrypts message
        iv, encrypted = self.bob.encrypt_message(message)

    # Alice decrypts the message
        decrypted = self.alice.decrypt_message(iv, encrypted)

    # Alice verifies the signature using Bob's public key
        is_valid = self.alice.verify_signature(message, signature, self.bob.public_key)

        self.display_message("Alice (Decrypted)", decrypted)
        self.display_message("Alice (Signature Verified)", str(is_valid))

        self.message_entry.delete(0, tk.END)



if __name__ == "__main__":
    root = tk.Tk()
    app = SecureChatGUI(root)
    root.mainloop()
