# Smart-password-Generator
A lightweight Python desktop application for creating customizable, randomized passwords with built-in validation

> **Generate smarter. Protect better.**

A simple and user-friendly desktop password generator built with **Python and Tkinter**.  
The application creates randomized passwords based on a user-defined length while ensuring that each password contains digits, letters, and special characters.

---

## ✨ Why This Project?

Creating strong passwords is important for protecting online accounts.

This project provides a simple solution where users can generate a customized password within seconds without manually creating complicated combinations.

---

## 🚀 Features

- 🔢 Choose password length from **8 to 16 characters**
- 🔐 Generates randomized passwords
- 🔢 Includes **at least 3 digits**
- 🔣 Includes **at least 1 special character**
- 🔤 Uses uppercase and lowercase letters
- 🔀 Randomly shuffles all generated characters
- 📋 Copy the generated password with one click
- 🧹 Clear the generated password
- ⚠️ Validates incorrect password lengths
- 🖥️ Simple graphical user interface

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core programming and password generation |
| 🖼️ Tkinter | Graphical User Interface |
| 🎲 Random | Random character generation |
| 🔤 String | Letters, digits and special characters |

---

## ⚙️ How It Works

The password is generated in a few simple steps:

```text
User enters password length
          ↓
     Validate length
          ↓
 Generate 1 special character
          ↓
    Generate 3 digits
          ↓
 Generate remaining letters
          ↓
     Combine characters
          ↓
       Shuffle them
          ↓
   Display the password
