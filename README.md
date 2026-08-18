# File-Operator

# 📔 Personal Journal Manager

A simple yet powerful **command-line journal application** built with Python. Write your thoughts, track your day, search past entries, and manage your personal journal — all from the terminal!

---

## 📖 About the Project

**Personal Journal Manager** is a lightweight, beginner-friendly CLI tool designed to help you maintain a daily journal directly from your terminal — no internet, no database, no extra setup required.

The idea behind this project is simple: journaling should be **quick, private, and distraction-free**. Every entry you write is automatically timestamped and stored in a local text file (`journal.txt`), so your thoughts stay organized by date and time without any manual effort.

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

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork this project and submit a pull request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

Bhavika Thadani
📍Ahmedabad
---

# 🖼️ sample output
**Welcome Menu:**
<img width="399" height="129" alt="image" src="https://github.com/user-attachments/assets/dbb4e7d1-e622-4c5f-b289-1b22045a14d3" />

⭐ If you like this project, don't forget to give it a star!
