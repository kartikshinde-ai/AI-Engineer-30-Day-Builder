# Day 03 — AI-Assisted Coding & Debugging Practice

## 🎯 Goal

Learn how to understand, test, debug, and improve AI-generated code instead of blindly copying it.

---

# 1. Functions, Inputs & Outputs

## What is a Function?

A function is a reusable block of code designed to perform a specific task.

## Inputs

Inputs are the values provided to a function so that it can perform its task.

## Processing

Processing is the logic performed by the function using the provided inputs.

## Output

The output is the result produced by the function.

### Basic Structure

**Input → Function / Processing → Output**

### Example

```python
def calculate_total(price, quantity):
    total = price * quantity
    return total

2.CSV Filtering Practice

Objective

Understand how a Python program can read a CSV file, apply a condition, and produce filtered output.

Expected Flow

CSV File → Read Data → Apply Condition → Filter Rows → Output

Code Analysis Checklist

Before running AI-generated code, identify:

Input
Main function
Processing logic
Condition
Output
Possible errors    

3. JSON & API Response
What is JSON?

JSON (JavaScript Object Notation) is a lightweight format used to represent and exchange structured data between applications.

4. Errors, Debugging & Logs
What is an Error?

An error occurs when a program cannot execute as expected.

Errors can be caused by incorrect syntax, invalid data, missing files, incorrect variable names, or unexpected conditions.

What is Debugging?

Debugging is the process of identifying the cause of an error, fixing it, and testing the program again.

Basic Debugging Flow

Error → Read Message → Identify Cause → Fix → Test Again

Reading Error Messages

An error message can provide useful information such as:

Error type
File name
Line number
Description of the problem

The error message should be understood before changing the code.

What are Logs?

Logs are records of events or information generated while a program or application is running.

They can help developers understand:

What happened
When it happened
Where a problem occurred
What operation was being performed

5.Common Error & Fix Examples

These are learning examples, not errors encountered during today's skipped practical.

Error 1 — Incorrect Variable Name
Problem
name = "Kartik"
print(nam)
Error
NameError: name 'nam' is not defined
Cause

The variable was created as name, but the code tried to use nam.

Fix
name = "Kartik"
print(name)
Lesson

Always check variable names carefully when reading an error message.

Error 2 — Missing File
Problem
with open("students.csv", "r") as file:
    data = file.read()

If students.csv does not exist in the expected location, Python can raise:

FileNotFoundError
Cause

The program cannot find the specified file.

Fix

Make sure:

The file exists.
The filename is correct.
The file is in the expected directory.
The file path is correct.
Lesson

File-related errors should be investigated by checking the filename, path, and working directory

6. AI-Assisted Coding Workflow

AI-generated code should not be blindly copied and executed.

Professional Workflow

Generate → Read → Identify Inputs → Understand Logic → Identify Output → Run → Debug → Test

Before using AI-generated code, ask:

What does this code do?
What inputs does it take?
What output does it produce?
What can fail?
Can I explain the main blocks of the code?