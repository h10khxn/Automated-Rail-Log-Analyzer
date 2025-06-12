# Rail System Log Analyzer

A safety-critical log parser for real-time embedded systems. This tool reads, analyzes, and summarizes log files for `[WARNING]` and `[ERROR]` messages — useful for debugging simulated embedded systems like those used in transportation, automation, or industrial environments.

---

## 🔧 Features

- Parses and cleans raw log files
- Detects and counts warnings and errors
- Outputs a clear summary to the console
- Structured using object-oriented principles
- Easily extendable for file output, CLI support, and automation

---

## 🛠 Tech Stack

- **Python 3**
- Shell scripting (`run.sh`) for automation

---

## 📂 Project Structure

rail-log-analyzer/
│
├── logs/
│ └── system_log.txt # Sample log file
│
│
├── scripts/
│ ├── parser.py # Main Python logic (LogAnalyzer class)
│ └── run.sh # Shell script to run the analyzer
│
├── docs/
│ └── wiki.md 
│
├── README.md # You're here 


---

## 🚀 How to Run

### 1. Clone the Repository

git clone https://github.com/h10khxn/Automated-Rail-Log-Analyzer.git
cd rail-log-analyzer/scripts

### 2. Run the shell command
./run.sh