import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook, load_workbook
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(BASE_DIR, "admission_data.xlsx")
logo_file = os.path.join(BASE_DIR, "logo.png")
# ---------- SAVE TO EXCEL ----------
def save_to_excel(data):
    if os.path.exists(file_name):
        wb = load_workbook(file_name)
        sheet = wb.active
    else:
        wb = Workbook()
        sheet = wb.active
        sheet.append([
            "Name", "Father", "Mother",
            "Percentage", "School", "Stream"
        ])
    sheet.append(data)
    wb.save(file_name)
# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("College Admission Form")
root.geometry("600x500")
root.configure(bg= "white")
# ---------- PAGE 1 ----------
def show_page1():
    clear_window()
    if os.path.exists(logo_file):
        try:
            global logo_image
            img = Image.open(logo_file)
            img = img.resize((120, 120), Image.Resampling.LANCZOS)
            logo_image = ImageTk.PhotoImage(img)
            tk.Label(root, image=logo_image, bg="white").pack(pady=(10, 0))
        except Exception:
            pass
    tk.Label(root, text="ST. THOMAS COLLEGE OF ENGINEERING & TECHNOLOGY",
             font=("Times New Roman", 24, "bold"),fg="white", bg="blue", wraplength=500, justify="center").pack(pady=20)
    tk.Label(root, text="APPROVED BY AICTE, NEW DELHI & AFFILIATED TO MAKAUT WB",
             font=("Arial", 10, "bold")).pack(pady=10)
    tk.Label(root, text="Do you want to take admission?",
             font=("Arial", 13)).pack(pady=30)
    tk.Button(root, text="Yes", width=12, command=show_page2,fg ="black", bg="lightblue").pack(pady=10)
    tk.Button(root, text="No", width=12, command=root.destroy).pack(pady=10)
# ---------- PAGE 2 ----------
def show_page2():
    clear_window()
    global name_entry, father_entry, mother_entry
    global percentage_entry, school_entry, stream_var
    tk.Label(root, text="Admission Form",
             font=("Arial", 16, "bold"), bg="lightblue", fg="black").pack(pady=10)
    # Name
    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root, width=40)
    name_entry.pack()
    # Father
    tk.Label(root, text="Father's Name").pack()
    father_entry = tk.Entry(root, width=40)
    father_entry.pack()
    # Mother
    tk.Label(root, text="Mother's Name").pack()
    mother_entry = tk.Entry(root, width=40)
    mother_entry.pack()
    # Percentage
    tk.Label(root, text="Previous Percentage").pack()
    percentage_entry = tk.Entry(root, width=40)
    percentage_entry.pack()
    # School
    tk.Label(root, text="Previous School Name").pack()
    school_entry = tk.Entry(root, width=40)
    school_entry.pack()
    # Stream Dropdown
    tk.Label(root, text="Select Stream").pack()
    stream_var = tk.StringVar()
    stream_var.set("B.Tech in Computer Science and Engineering")
    tk.OptionMenu(
        root,
        stream_var,
        "B.Tech in Computer Science and Engineering",
        "B.Tech in Information Technology",
        "B.Tech in Artificial Intelligence and Machine Learning",
        "B.Tech in Electronics and Communication",
        "B.Tech in Electrical Engineering"
    ).pack(pady=5)
   # Buttons
    tk.Button(root, text="Submit", command=submit_form, width=15,fg="white", bg="green").pack(pady=10)
    tk.Button(root, text="Back", command=show_page1, width=15).pack()
# ---------- SUBMIT ----------
def submit_form():
    name = name_entry.get()
    father = father_entry.get()
    mother = mother_entry.get()
    percentage = percentage_entry.get()
    school = school_entry.get()
    stream = stream_var.get()
    # Validation
    if not name or not father or not mother or not percentage or not school:
        messagebox.showerror("Error", "Please fill all required fields")
        return

    try:
        percentage = float(percentage)
        if percentage < 0 or percentage > 100:
            raise ValueError
    except (TypeError, ValueError):
        messagebox.showerror("Error", "Percentage must be a number between 0 and 100")
        return

    data = [name, father, mother, percentage, school, stream]
    save_to_excel(data)
    messagebox.showinfo("Success", "Form Submitted Successfully!")
    clear_fields()
# ---------- CLEAR ----------
def clear_fields():
    name_entry.delete(0, tk.END)
    father_entry.delete(0, tk.END)
    mother_entry.delete(0, tk.END)
    percentage_entry.delete(0, tk.END)
    school_entry.delete(0, tk.END)
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
# ---------- START ----------
show_page1()
root.mainloop()
