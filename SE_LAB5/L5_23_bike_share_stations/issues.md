# Lab 5: Static Code Analysis — Issue Report

Repository: L5_23_bike_share_stations

## Issues Identified and Fixed

| Issue | Type / Severity | Original Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| SQL query built through string concatenation | Security / Medium | 9 | User-controlled station names were concatenated into SQL, creating an SQL injection risk. | Used parameterized SQL queries with placeholders. |
| Insecure random PIN generation | Security / Low | 22 | `random.randint()` is not suitable for security-sensitive values. | Replaced `random` with Python's `secrets` module. |
| Broad exception silently ignored | Security / Low; Code quality | 32–35 | `except Exception: pass` concealed database errors. | Removed the silent exception handler so unexpected errors are visible. |
| Mutable default argument | Bug / Code quality | 8 | `log=[]` could share a list between calls that omit the argument. | Changed the default to `None` and initialized a new list inside the function. |
| Inconsistent return values | Code quality | 14–19 | The rental function returned `True` on success but implicitly returned `None` on failure. | Made the function return `True` or `False` consistently. |
| Non-standard function names | Style / Code quality | Multiple | CamelCase function names did not follow Python's `snake_case` convention. | Renamed functions and updated their call sites. |
| Missing docstrings | Code quality | Multiple | The module and functions did not explain their purpose. | Added module and function docstrings. |
| Unused variable | Code quality | 27 | `summary` was assigned but never used. | Removed the unnecessary variable. |
| Incorrect comparison with `None` | Code quality | 40 | Used `== None` instead of an identity check. | Used `is None` and handled missing database rows safely. |
| Long lines and trailing whitespace | Style | Multiple | Several lines exceeded configured style limits or contained trailing whitespace. | Reformatted SQL statements and removed unnecessary whitespace. |
| Missing final newline | Style | End of file | The original file did not end with a newline. | Added the final newline. |

## Verification Summary

- Original Pylint score: 3.89/10
- Final Pylint score: 10.00/10
- Original Bandit findings: 3 (1 medium, 2 low)
- Final Bandit result: No issues identified in the verified scan
- Final Flake8 result: No violations reported

Note: Line numbers refer to the original version of the Python file.
