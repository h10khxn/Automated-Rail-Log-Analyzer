import os
class LogAnalyzer:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.log_lines = []
        self.warnings = []
        self.errors = []
        self.warning_count = 0
        self.error_count = 0

    def read_log(self):
        #Parsing over the log file to extract lines and cleaning white spaces
        with open(self.log_file_path, 'r') as file:
            self.log_lines = [line.strip() for line in file.readlines()]

    def analyze_log(self):
        #Analyzing the log lines for warnings and errors
        for line in self.log_lines:
            if "WARNING" in line:
                self.warnings.append(line)
                self.warning_count += 1
            elif "ERROR" in line:
                self.errors.append(line)
                self.error_count += 1

    def generate_summary(self):
        print("Number of warnings:" , self.warning_count) 
        print("Number of Errors:" , self.error_count)
        print("Errors:")
        for e in self.errors:
            print(" -", e)

        print("Warnings:")
        for w in self.warnings:
            print(" -", w)

analyzer = LogAnalyzer("../logs/system_log.txt")
analyzer.read_log()
analyzer.analyze_log()
analyzer.generate_summary()