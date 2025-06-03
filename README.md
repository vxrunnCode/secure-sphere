# SecureSphere 🔐

SecureSphere is a Python command-line utility to evaluate password strength, check passwords in bulk from a file, and generate strong, hard-to-crack passwords. It uses entropy calculations and a live common password database to rate passwords from Easy to Impossible.

---

## Features

- Check a single password’s strength  
- Bulk check passwords from a file  
- Generate strong random passwords with high entropy (rated Impossible)  
- Fetches a live list of the 10,000 most common passwords from an online source  
- Cross-platform: Works on Windows, Kali Linux, and other systems with Python 3.6+

---

## Requirements

- Python 3.6 or higher  
- `requests` library  
- `pyfiglet` library (for ASCII banner)

---

## Installation

1. **Clone the repository** (or download the files):

    ```bash
    git clone https://github.com/YOUR_USERNAME/secure-sphere.git
    cd secure-sphere
    ```

2. **Create a Python virtual environment** (recommended):

    ```bash
    python -m venv venv
    ```

    - Activate the virtual environment:  
      - On Windows: `venv\Scripts\activate`  
      - On Linux/macOS: `source venv/bin/activate`

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

Run the main program:

```bash
python password_tool.py


1. Check a single password  
Choose option `1`

Enter the password when prompted.

The program will print the strength rating (Easy, Medium, Hard, Hard but still can be cracked, Impossible).

---

2. Check passwords from a file  
Prepare a text file with one password per line.

Choose option `2`.

Enter the file path when prompted (e.g., `passwords.txt`).

The program will rate each password in the file.

---

3. Generate a strong password  
Choose option `3`.

Enter desired length (or press Enter for default 20 characters).

The program generates and displays a strong password rated **“Impossible”**.

