<h1 align="center" style="color: #4A90E2;">Secure Chat</h1>

## <span style="color:#E94E77;">Overview</span>
**Secure Chat** is a hybrid cryptographic chat application built in Python. It demonstrates **secure end-to-end encrypted communication** between two users using combined cryptographic techniques like:

- <span style="color:#4A90E2;">Diffie-Hellman key exchange</span> for secure shared AES key agreement
- <span style="color:#4A90E2;">RSA asymmetric encryption</span> and digital signatures for authentication
- <span style="color:#4A90E2;">AES symmetric encryption</span> for message confidentiality

The project includes an **interactive Tkinter GUI** supporting encrypted messaging, signature verification, and decrypted message display in real-time.

---

## <span style="color:#E94E77;">Features</span>

- 🔐 **Secure key exchange:** Diffie-Hellman to establish AES session keys  
- 🔐 **Message encryption/decryption:** AES provides message confidentiality  
- ✍️ **Digital signature:** RSA signing and verification for authenticity  
- 🖥️ **Interactive GUI:** Color-coded chat display with encrypted, decrypted, and signature messages  
- 📋 **Copy encrypted messages:** Easily copy ciphertext to clipboard  
- 🧹 **Clear chat:** Reset chat window instantly  

---

## <span style="color:#E94E77;">Installation</span>

1. **Clone this repository:**

<h1 align="center" style="color: #4A90E2;">Secure Chat</h1>

## <span style="color:#E94E77;">Overview</span>
**Secure Chat** is a hybrid cryptographic chat application built in Python. It demonstrates **secure end-to-end encrypted communication** between two users using combined cryptographic techniques like:

- <span style="color:#4A90E2;">Diffie-Hellman key exchange</span> for secure shared AES key agreement
- <span style="color:#4A90E2;">RSA asymmetric encryption</span> and digital signatures for authentication
- <span style="color:#4A90E2;">AES symmetric encryption</span> for message confidentiality

The project includes an **interactive Tkinter GUI** supporting encrypted messaging, signature verification, and decrypted message display in real-time.

---

## <span style="color:#E94E77;">Features</span>

- 🔐 **Secure key exchange:** Diffie-Hellman to establish AES session keys  
- 🔐 **Message encryption/decryption:** AES provides message confidentiality  
- ✍️ **Digital signature:** RSA signing and verification for authenticity  
- 🖥️ **Interactive GUI:** Color-coded chat display with encrypted, decrypted, and signature messages  
- 📋 **Copy encrypted messages:** Easily copy ciphertext to clipboard  
- 🧹 **Clear chat:** Reset chat window instantly  

---

## <span style="color:#E94E77;">Installation</span>

1. **Clone this repository:**
<h1 align="center" style="color: #4A90E2;">Secure Chat</h1>

## <span style="color:#E94E77;">Overview</span>
**Secure Chat** is a hybrid cryptographic chat application built in Python. It demonstrates **secure end-to-end encrypted communication** between two users using combined cryptographic techniques like:

- <span style="color:#4A90E2;">Diffie-Hellman key exchange</span> for secure shared AES key agreement
- <span style="color:#4A90E2;">RSA asymmetric encryption</span> and digital signatures for authentication
- <span style="color:#4A90E2;">AES symmetric encryption</span> for message confidentiality

The project includes an **interactive Tkinter GUI** supporting encrypted messaging, signature verification, and decrypted message display in real-time.

---

## <span style="color:#E94E77;">Features</span>

- 🔐 **Secure key exchange:** Diffie-Hellman to establish AES session keys  
- 🔐 **Message encryption/decryption:** AES provides message confidentiality  
- ✍️ **Digital signature:** RSA signing and verification for authenticity  
- 🖥️ **Interactive GUI:** Color-coded chat display with encrypted, decrypted, and signature messages  
- 📋 **Copy encrypted messages:** Easily copy ciphertext to clipboard  
- 🧹 **Clear chat:** Reset chat window instantly  

---

## <span style="color:#E94E77;">Installation</span>

1. **Clone this repository:**  git clone <repository-url>
2. **Navigate into the project directory:** cd HybridCryptoSecureCommSystem
3.  **Install dependencies:** pip install pycryptodome pyperclip pillow

## <span style="color:#E94E77;">Usage</span>

Run the GUI application module from the project root:
python -m interface.gui


This launches the secure chat window where two users (USER_1 and USER_2) can exchange encrypted and signed messages.

---

## <span style="color:#E94E77;">Project Structure</span>

SecureChat/
├── core/
│ └── message_handler.py # Core cryptographic logic
├── crypto/
│ ├── aes_module.py # AES implementation
│ ├── rsa_module.py # RSA implementation
│ └── diffie_hellman.py # Diffie-Hellman key exchange
├── interface/
│ ├── gui.py # Tkinter GUI app
│ └── init.py
├── main.py # Optional CLI or main
├── README.md # This file
├── background.png # Background image for GUI (optional)
└── requirements.txt # Optional package list


---

## <span style="color:#E94E77;">How It Works</span>

1. Each user generates RSA and Diffie-Hellman key pairs.  
2. They exchange DH public keys to create a shared AES secret key.  
3. Messages are AES encrypted and RSA signed before sending.  
4. Receiver verifies the signature and decrypts the message.  
5. GUI displays original, encrypted (hidden behind panel), decrypted, and signature status messages.

---

## <span style="color:#E94E77;">Author</span>
Shravya Ravindra





