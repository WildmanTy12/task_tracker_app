# 📝 Task Tracker CLI App

A lightweight, emoji-enhanced command-line interface (CLI) task tracker built in Python.  
This app lets you manage tasks with a clean UX, local JSON persistence, and clear user prompts — all without needing a database (yet).

---

## 🚀 Features

- ✅ Add new tasks
- ✏️ Update task titles or status
- ❌ Delete tasks with confirmation
- 📁 Persist tasks in a local `tasks.json` file
- 🧠 Clean, beginner-friendly code with docstrings and modular functions
- 🎨 Emoji-based status indicators for completed vs. in-progress tasks

---

## 📂 File Structure

```bash
task_tracker_app/
├── task_tracker.py      # Main CLI application
├── tasks.json           # (auto-generated) saved tasks file
└── README.md            # Project documentation
Note: tasks.json is not tracked in version control and is included in .gitignore.

📦 Requirements
Python 3.7+

No external packages required (uses only Python standard library)

📈 Planned Enhancements
🗄️ MySQL Database Integration
Move from local file storage to MySQL for better scalability and multi-user support.

🌐 Flask Web Interface
Add a basic web UI using Flask so tasks can be managed via browser.

✅ Unit Testing + CI
Build out tests and consider GitHub Actions for auto-validation on push.

🌈 Colorful CLI output
Add optional terminal colors for better UX (via colorama or similar)

💡 Usage
To run the app:

python3 task_tracker.py
Tasks will be saved automatically in tasks.json after every add, update, or delete.

🔒 Security / Git Hygiene
Local task data (tasks.json) is excluded from Git tracking

No credentials or secrets stored in this project

🙌 Author
Created by Tyson Wildman (@wildmanty12)

🗓️ License
MIT License — free to use, modify, and distribute.
