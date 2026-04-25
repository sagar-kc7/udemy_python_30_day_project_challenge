# Udemy Python 30-Day Project Challenge

A collection of Python exercises and mini-projects completed as part of the **"100 Days of Code: The Complete Python Pro Bootcamp"** course on Udemy. The work here covers roughly the first 30 days of the curriculum, progressing from beginner fundamentals through intermediate GUI and game projects.

---

## Repository Structure

| Folder | Days | Topic / Project |
|---|---|---|
| `Lab_1_17/` | 1 – 17 | Core Python fundamentals — organised day-by-day (see below) |
| `Lab_18/` | 18 | Turtle Dot Painting (Hirst-style spot art) |
| `Lab_19/` | 19 | Turtle Racing Game |
| `Lab_20_21_22_Snake_Game/` | 20 – 21 | Snake Game (OOP + Turtle) |
| `Lab_22_PONG_GAME/` | 22 | Pong Game (OOP + Turtle) |
| `Lab_23/` | 23 | Turtle Crossing / Car Manager Game |
| `Lab_24/` | 24 | *(empty — placeholder only)* |
| `Lab_25/` | 25 | U.S. States Quiz (Pandas + Turtle) |
| `Lab_26/` | 26 | *(empty — placeholder only)* |
| `Lab_27/` | 27 | Tkinter GUI — Miles-to-KM Converter |
| `Lab28_30/` | 28 – 30 | NATO Phonetic Alphabet (Pandas + list/dict comprehension) |
| `Lab_28_30/` | — | Duplicate project config (pyproject.toml only) |

### Lab_1_17 — Day-by-Day Breakdown

| Day | Key Topics | Capstone Project |
|---|---|---|
| 1 | Printing, variables, string manipulation, inputs | Band Name Generator |
| 2 | Data types, type conversion, maths operators | Tip Calculator |
| 3 | If/elif/else, modulo, logical operators | Treasure Island Adventure |
| 4 | Random module, lists | Rock Paper Scissors |
| 5 | For loops, range | Password Generator |
| 6 | Functions | Reeborg's World exercises |
| 7 | While loops, flags | Hangman |
| 8 | Functions with inputs, positional vs keyword args | Caesar Cipher |
| 9 | Dictionaries, nesting | Blind Auction |
| 10 | Functions with outputs, return values, docstrings | Calculator |
| 11 | Blackjack rules, OOP preview | Blackjack |
| 12 | Namespaces, scope, global variables | Number Guessing Game |
| 13 | Debugging (print, debugger, error types) | Debugging exercises |
| 14 | Higher-order data, comparisons | Higher or Lower Game |
| 15 | Modelling a problem with code | Coffee Machine |
| 16 – 30 | *(redirect — rest of days not included here)* | — |

---

## Prerequisites

- **Python 3.8 or later** — download from [python.org](https://www.python.org/downloads/)
- Most labs use only the **Python standard library** (`turtle`, `tkinter`, `random`, etc.) and need no extra packages.
- Two labs require **third-party packages**:

| Lab | Package | Install command |
|---|---|---|
| `Lab_25/` | `pandas` | `pip install pandas` |
| `Lab28_30/` | `pandas` | `pip install pandas` (or `poetry install` inside the folder) |

> **Note:** `Lab_18/main.py` references `colorgram` in commented-out code. That section is not needed to run the dot-painting script; the extracted colours are already hard-coded.

---

## Running a Lab Locally

```bash
# 1. Clone the repository
git clone https://github.com/sagar-kc7/udemy_python_30_day_project_challenge.git
cd udemy_python_30_day_project_challenge

# 2. (Optional) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies if required by the lab (see table above)
pip install pandas

# 4. Navigate to the lab and run its entry point
cd Lab_25
python main.py
```

Most labs follow the same pattern — navigate into the folder and run `python main.py`.

For `Lab28_30/` you can alternatively use [Poetry](https://python-poetry.org/):

```bash
cd Lab28_30
poetry install
poetry run python main.py
```

For `Lab_1_17/`, each day folder contains individual exercise files (`task.py` / `solution.py`) as well as a capstone `main.py` where one exists:

```bash
cd "Lab_1_17/Day 10/Calculator Project"
python main.py
```

---

## Notes

- Turtle and Tkinter projects open a graphical window — run them in an environment with display support (not a headless server).
