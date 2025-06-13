# Rail System Log Analyzer

A safety-critical log parser for real-time embedded systems. This tool reads, analyzes, and generates AI based natural-language summaries of log files containing `[WARNING]` and `[ERROR]` messages — ideal for debugging simulated systems like those used in transportation, automation, and industrial control.

---

## 🔧 Features

- Parses and cleans raw log files
- Detects and counts all warning and error messages
- Generates natural-language summaries using a locally hosted BART transformer model
- Displays a full breakdown and AI-generated summary in the terminal
- Structured with clean object-oriented Python
- Easy to extend for file output, real-time feeds, dashboards, or anomaly detection

---

## 🛠 Tech Stack

- **Python 3**
- **Transformers (Hugging Face)**
- **BART-large-cnn** for summarization
- Shell scripting (`run.sh`) for execution

> ⚠️ Make sure you install dependencies before running:
```bash
pip install transformers torch


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
