# ANTIVIRUS MD5
A basic antivirus program which detects malware signature based on MD5 hash of a file

## Basic Antivirus Project

This is a very basic antivirus project written in Python. It scans files and identifies potential malware or suspicious content.

# How to Use

1. Initialize the 'BasicAntivirus' class.
2. Call the 'scan_file' method with the file path as the argument.

# Code Structure

The BasicAntivirus class has two methods:

1) __init__: This method initializes the virus_db attribute with a list of virus signatures.
2) scan_file: This method takes a file path as an argument, calculates the MD5 hash of the file, and checks if the hash is in the virus_db.

# Usage

You can use this basic antivirus to scan any file for potential malware. Just replace the virus_db list with real virus signatures.

NOTE: Remember, this is a very basic example and should not be used as a real antivirus solution. It's always recommended to use a professional antivirus software to protect your system.


Example:

```python
av = BasicAntivirus()
result = av.scan_file('test.txt')
if result:
    print("Malware detected!")
else:
    print("File is clean.")

