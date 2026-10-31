# LAB6 — Code and Branch Coverage Analysis

This folder contains the Lab 6 shopping-cart application and two independent
pytest suites, as required by the lab handout.

## Files

- `shopping_cart.py` — application supplied for the exercise.
- `CodeCoverageTest_shopping_cart.py` — tests intended to execute every
  application statement.
- `BranchCoverageTest_shopping_cart.py` — tests intended to exercise both
  outcomes of the application's conditional branches.
- `requirements.txt` — test and coverage dependencies.

## Setup

Run these commands from inside `LAB6`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 1. Code / statement coverage

```bash
coverage erase
coverage run --source=shopping_cart -m pytest -v CodeCoverageTest_shopping_cart.py
coverage report -m
```

## 2. Branch coverage

```bash
coverage erase
coverage run --branch --source=shopping_cart -m pytest -v BranchCoverageTest_shopping_cart.py
coverage report -m
```

The `--source=shopping_cart` option limits the report to the application module,
rather than counting the test files themselves.

## Evidence and submission

After running each command successfully, capture a genuine terminal screenshot
showing the pytest result and the corresponding `coverage report -m` result.
Save the screenshots in this folder as:

- `code_coverage_screenshot.png`
- `branch_coverage_screenshot.png`

Do not create or submit placeholder screenshots. The screenshots must come
from your own terminal after executing the commands.

## Git commits

Run these from the repository root. The first two commits keep the two required
test suites in separate commits. After capturing genuine terminal screenshots,
add them in a third evidence commit.

```bash
git add LAB6/shopping_cart.py LAB6/CodeCoverageTest_shopping_cart.py LAB6/README.md LAB6/requirements.txt LAB6/.gitignore
git commit -m "lab6: add code coverage tests"

git add LAB6/BranchCoverageTest_shopping_cart.py
git commit -m "lab6: add branch coverage tests"

# Run both coverage commands, capture the terminal screenshots, then:
git add LAB6/code_coverage_screenshot.png LAB6/branch_coverage_screenshot.png
git commit -m "lab6: add coverage evidence"
```

Do not commit generated `.coverage`, `.pytest_cache`, `__pycache__`, or `.venv`
files. The screenshots are intentionally not included as placeholders; capture
them from your own terminal after running the tests.
