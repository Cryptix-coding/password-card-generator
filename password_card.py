# Copyright (C) 2026 Cryptix
# SPDX-License-Identifier: GPL-3.0-or-later 

import os
import secrets
from fpdf import FPDF

# Constants for grid generation
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!()=?{[]}@#$%&*+-_'
HEAD = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQR', 'STU', 'VWX', 'YZß', '.!?']

def random_string(length=3):
    # Generate a secure 3-character string
    return ''.join(secrets.choice(ALPHABET) for _ in range(length))

def generate_password_card():
    # Create a 10x10 matrix with random strings
    return [[random_string() for _ in range(10)] for _ in range(10)]

def save_pc(filename, pc):
    # Save the matrix to a text file
    with open(filename, 'w') as out:
        out.write('\n'.join(''.join(row) for row in pc))

def load_pc(filename):
    # Load the matrix from a text file into a list
    pc = []
    with open(filename, 'r') as pc_in:
        for row in pc_in:
            row = row.strip()
            pc.append([row[i:i+3] for i in range(0, len(row), 3)])
    return pc

def generate_password(pc, keyword):
    # Trace keyword through the matrix to build password
    password = ""
    rows = len(pc)
    for row_idx, char in enumerate(keyword):
        for col_idx, group in enumerate(HEAD):
            if char in group:
                password += pc[row_idx % rows][col_idx]
                break
    return password

def write_pdf(filename="password_card.pdf"):
    # Export the matrix as a formatted PDF table
    pc = load_pc("password_card.txt")
    document = FPDF()
    document.add_page()
    document.set_font('helvetica', size=11)
    
    c_width = 10 
    d_width = 9
    
    html_table = '<h1>Password Card</h1>\n<table border="1"><thead>\n'
    html_table += f'<tr bgcolor="#AED6F1"><th width="{c_width}%">Counter</th>'
    for th in HEAD:
        html_table += f'<th width="{d_width}%">{th}</th>'
    html_table += '</tr>\n</thead><tbody>'
    
    for i, row in enumerate(pc, start=1):
        color = "#D6EAF8" if i % 2 != 0 else "#FFFFFF"
        html_table += f'<tr bgcolor="{color}"><td>{i}</td>'
        for cell in row:
            html_table += f'<td>{cell}</td>'
        html_table += '</tr>'
    html_table += '</tbody></table>'

    document.write_html(html_table)
    document.output(filename)

def create_new_card():
    # Generate and save both txt and pdf files
    print("[Info] Generating new password card...")
    save_pc("password_card.txt", generate_password_card())
    write_pdf()
    print("[Success] Saved 'password_card.txt' and 'password_card.pdf'.")

def main():
    # Main CLI workflow
    print("\n[Info] Starting Secure Password Card Generator...")
    
    if os.path.exists("password_card.txt"):
        action = input("[Info] Found an existing 'password_card.txt'. Do you want to use it? (y/n): ").strip().lower()
        if action == 'n':
            create_new_card()
    else:
        print("[Info] No existing password card found.")
        create_new_card()
        
    keyword = input("[Info] Enter your keyword (UPPERCASE ONLY): ").strip()
    
    try:
        print("[Info] Tracing coordinates and generating secure password...")
        generated_password = generate_password(load_pc("password_card.txt"), keyword)
        print(f"\n[Success] Your Secure Password: {generated_password}\n")
    except Exception as e:
        print(f"[Error] Failed to generate password: {e}")
        
    print("[Info] Process finished.\n")

if __name__ == "__main__":
    main()