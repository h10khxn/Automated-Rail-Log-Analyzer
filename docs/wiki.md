# Internal Documentation - Rail System Log Analyzer

## 📘 Overview

This internal tool is designed to assist developers in debugging simulated real-time embedded system logs by extracting and reporting `[WARNING]` and `[ERROR]` entries. It is structured using object-oriented principles and built to be modular, lightweight, and extensible.

---

## 🧠 Class: `LogAnalyzer`

The core of this tool is the `LogAnalyzer` class, which encapsulates all log-processing behavior.

### 🔹 Attributes

| Attribute         | Type    | Description                                      |
|------------------|---------|--------------------------------------------------|
| `log_file_path`   | `str`   | File path to the input log file                  |
| `log_lines`       | `list`  | Raw lines read from the log file                 |
| `warnings`        | `list`  | Lines identified as warnings                     |
| `errors`          | `list`  | Lines identified as errors                       |
| `warning_count`   | `int`   | Count of warning messages                        |
| `error_count`     | `int`   | Count of error messages                          |

---

### 🔹 Methods

#### `__init__(log_file_path)`
Initializes the analyzer with the path to the log file and sets up internal lists.

#### `read_log()`
Reads the log file line-by-line, strips whitespace, and stores the cleaned lines.

#### `analyze_log()`
Parses `log_lines`, filtering entries into `warnings` and `errors` lists.

#### `generate_summary()`
Prints:
- Total number of warnings and errors
- Each warning and error on a new line

---

## 🔄 Execution Flow

1. Initialize a `LogAnalyzer` object with the log file path.
2. Call `read_log()` to load and clean the log file.
3. Call `analyze_log()` to process and separate warnings/errors.
4. Call `generate_summary()` to view a breakdown of log issues.

---

## 🧪 Example

```python
analyzer = LogAnalyzer("../logs/system_log.txt")
analyzer.read_log()
analyzer.analyze_log()
analyzer.generate_summary()
