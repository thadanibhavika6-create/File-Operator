# File-Operator

# 📔 Personal Journal Manager

A simple yet powerful **command-line journal application** built with Python. Write your thoughts, track your day, search past entries, and manage your personal journal — all from the terminal!

---

## 📖 About the Project

**Personal Journal Manager** is a lightweight, beginner-friendly CLI tool designed to help you maintain a daily journal directly from your terminal — no internet, no database, no extra setup required.

The idea behind this project is simple: journaling should be **quick, private, and distraction-free**. Every entry you write is automatically timestamped and stored in a local text file (`journal.txt`), so your thoughts stay organized by date and time without any manual effort.

<img width="1536" height="1024" alt="ChatGPT Image Aug 18, 2026, 07_53_36 PM" src="https://github.com/user-attachments/assets/35056756-49e4-4ee1-b210-e70ee812fe22" />


---
This project was built as a practical way to explore core Python concepts such as:

- **File handling** (reading, writing, and appending to files)
- **Exception handling** (gracefully managing missing files, permission errors, etc.)
- **String manipulation** (splitting and searching text data)
- **Object-Oriented Programming** (the entire app is structured using a single `JournalManager` class)
- **Building interactive CLI applications** with a menu-driven interface

Whether you want to jot down your daily thoughts, track personal goals, or simply practice mindfulness through writing, this tool provides a simple and reliable way to do it — right from your command line.

---

## ✨ Features

- 📝 **Add New Entry** — Write a journal entry with an automatic timestamp
- 📖 **View All Entries** — Read all your saved journal entries in one place
- 🔍 **Search Entries** — Find entries by keyword or date
- 🗑️ **Delete All Entries** — Clear your journal with a confirmation prompt
- 💾 **Persistent Storage** — Entries are saved locally in a `journal.txt` file
- ⚠️ **Error Handling** — Handles missing files and permission errors gracefully

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Modules Used:** `os`, `datetime`
- **Storage:** Plain text file (`journal.txt`)

---

## 📂 Project Structure

```
├── journal_manager.py   # Main application file
├── journal.txt          # Auto-generated file storing journal entries
└── README.md            # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone this repository or download the script:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Run the application:
   ```bash
   python journal_manager.py
   ```

---

## 🎮 Usage

Once you run the program, you'll see a menu like this:

```
Welcome to Personal Journal Manager!
Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Enter your choice:
```

Simply enter the number corresponding to the action you want to perform, and follow the on-screen prompts.

### Example

```
Enter your choice: 1
Enter your journal entry: Today was a productive day!
Entry added successfully!
```

Your entry will be saved with a timestamp like:

```
[2026-08-18 14:32:05]
Today was a productive day!
```

---

## 📌 Menu Options Explained

| Option | Action | Description |
|--------|--------|-------------|
| 1 | Add a New Entry | Adds a new timestamped entry to your journal |
| 2 | View All Entries | Displays all previously saved entries |
| 3 | Search for an Entry | Searches entries by keyword or date |
| 4 | Delete All Entries | Deletes the journal file after confirmation |
| 5 | Exit | Closes the application |

---

## 🔮 Future Improvements

- [ ] Edit existing entries
- [ ] Export entries to PDF
- [ ] Add mood/tags to entries
- [ ] GUI or Web-based version
- [ ] Encrypt journal entries for privacy

---
# 🖼️ sample output

<img width="1150" height="1050" alt="personal_journal_manager_output (1)" src="https://github.com/user-attachments/assets/c14c348d-8b16-49e5-a2b4-0bcb3095ba49" />

---
[Watch_Video_Here](https://drive.google.com/file/d/17xq_-tml94IKCkd2PmRM1F2ZgpfOREjN/view?usp=drivesdk)

---

## 👤 Author

Bhavika Thadani
📍Ahmedabad
---

## 🤝 Contributions

Contributions, issues, and feature requests are welcome! Feel free to fork this project and submit a pull request.

---

⭐ If you like this project, don't forget to give it a star!

---

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-9B59B6)
![Made with](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)
