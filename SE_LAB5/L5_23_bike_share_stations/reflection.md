# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, maintainability problems, and style violations early in development. Fixing these issues early can reduce debugging effort and improve software quality.

## 2. What did Pylint, Bandit, and Flake8 identify?

Pylint identified code-quality issues such as missing docstrings, inconsistent function naming, a mutable default argument, inconsistent return statements, and an unused variable. Bandit identified unsafe SQL string construction, use of a standard pseudo-random generator for PINs, and a silent broad exception handler. Flake8 identified long lines, trailing whitespace, an unused variable, and an incorrect comparison with None.

## 3. Which fixes were most important, and why?

The security fixes were especially important. Parameterized SQL queries prevent input values from being interpreted as SQL code. The secrets module provides a cryptographically secure way to generate PINs. Removing the silent exception handler also makes unexpected database errors visible. The remaining fixes improved correctness, readability, and maintainability.

## 4. What did you learn from this lab?

I learned that a program can run successfully and still contain security, correctness, and style problems. Using multiple static-analysis tools provides complementary perspectives: Pylint focuses on code quality, Bandit focuses on security, and Flake8 focuses on style. Rerunning the tools after making changes helps verify that the reported issues have been addressed. Static analysis is useful, but it does not replace functional testing or code review.
