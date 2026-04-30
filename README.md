# Password Card Generator

A Python-based CLI tool that creates and uses physical cards to generate secure passwords. This project implements a concept similar to two-factor authentication (2FA): the password requires both "something you know" (your mental keyword) and "something you have" (the unique password card file).

## Features
* **Cryptographically Secure:** Uses Python's `secrets` module instead of standard `random` to generate secure character matrices.
* **Automated PDF Export:** Generates both a machine-readable `.txt` file and a clean, printable `.pdf` table for offline use.
* **User-Friendly Input:** Displays your keyword while typing to help you verify your input and avoid typos before generating the password.
* **Smart Workflow:** Automatically detects existing password cards in your directory to streamline usage.

## Usage
Simply execute the script `password_card.py`. On startup, the script will:
* Automatically check if you already have a password card.
* Generate a new `password_card.txt` and `password_card.pdf` if none exists. **Keep these files secure!**
* Prompt you to enter a memorable keyword (UPPERCASE ONLY).
* Trace this word through your unique matrix and output your secure password.

To retrieve the password in the future, simply run the script again with the `.txt` file in the same directory.

## Required Python Packages
Install the necessary dependencies via pip:
* `fpdf2` - Used for generating the PDF version of the password card.

## Example of a generated Password Card
<img width="914" height="334" alt="Password Card" src="https://github.com/user-attachments/assets/a1d0eeff-3c58-44d8-9316-c88379ff2ba4" />


## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

```
GNU General Public License v3.0
Copyright (c) 2026 Cryptix
```
