import tkinter as tk
from tkinter import messagebox
from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel, CTkComboBox, CTkFrame, set_appearance_mode
import math
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# تنظیم تم و حالت نمایش
set_appearance_mode("dark")

# ایجاد پنجره اصلی
root = CTk()
root.title("ماشین حساب مهندسی پیشرفته")
root.geometry("700x650")

# تعریف متغیرهای حافظه و تاریخچه
memory = 0
history = []

# ایجاد جعبه ورودی برای نمایش و ورودی اعداد و عبارات
entry = CTkEntry(root, width=580, height=50, font=('Arial', 20), corner_radius=10)
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

# تعریف متغیرها برای منوهای کشویی
units = ["meters", "kilometers", "grams", "kilograms", "celsius", "fahrenheit"]
from_unit_var = tk.StringVar(value=units[0])
to_unit_var = tk.StringVar(value=units[1])

# ایجاد قاب اصلی
frame = CTkFrame(root, corner_radius=10, bg_color="#2e2e2e")
frame.grid(row=1, column=0, columnspan=6, padx=10, pady=10)

# تابع برای افزودن اعداد و عبارات به جعبه ورودی
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# تابع برای پاک کردن جعبه ورودی
def button_clear():
    entry.delete(0, tk.END)

# تابع برای محاسبه نتیجه و نمایش آن
def button_equal():
    try:
        result = eval(entry.get())
        history.append(f"{entry.get()} = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

# تابع برای انجام محاسبات پیشرفته
def button_advanced(operation):
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        if operation == "sqrt":
            result = math.sqrt(value)
        elif operation == "log":
            result = math.log10(value)
        elif operation == "ln":
            result = math.log(value)
        elif operation == "exp":
            result = math.exp(value)
        elif operation == "abs":
            result = math.fabs(value)
        elif operation == "fact":
            result = math.factorial(int(value))
        elif operation == "sin":
            result = math.sin(math.radians(value))
        elif operation == "cos":
            result = math.cos(math.radians(value))
        elif operation == "tan":
            result = math.tan(math.radians(value))
        elif operation == "asin":
            result = math.degrees(math.asin(value))
        elif operation == "acos":
            result = math.degrees(math.acos(value))
        elif operation == "atan":
            result = math.degrees(math.atan(value))
        elif operation == "sinh":
            result = math.sinh(value)
        elif operation == "cosh":
            result = math.cosh(value)
        elif operation == "tanh":
            result = math.tanh(value)
        elif operation == "radians":
            result = math.radians(value)
        elif operation == "degrees":
            result = math.degrees(value)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

# توابع حافظه
def button_memory(operation):
    global memory
    try:
        value = float(entry.get())
        if operation == "M+":
            memory += value
        elif operation == "M-":
            memory -= value
        elif operation == "MR":
            entry.delete(0, tk.END)
            entry.insert(0, memory)
        elif operation == "MC":
            memory = 0
        entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

# تابع برای رسم نمودار توابع
def plot_function():
    try:
        func = entry.get()
        x = np.linspace(-10, 10, 400)
        y = eval(func)
        plt.plot(x, y)
        plt.title(f'Graph of {func}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Function: {e}")

# تابع برای تبدیل واحدها
def convert_units():
    try:
        value = float(entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        if from_unit == "meters" and to_unit == "kilometers":
            result = value / 1000
        elif from_unit == "kilometers" and to_unit == "meters":
            result = value * 1000
        elif from_unit == "grams" and to_unit == "kilograms":
            result = value / 1000
        elif from_unit == "kilograms" and to_unit == "grams":
            result = value * 1000
        elif from_unit == "celsius" and to_unit == "fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            result = (value - 32) * 5/9
        else:
            raise ValueError("Invalid conversion")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Input: {e}")

# تابع برای نمایش تاریخ و زمان
def show_datetime():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    messagebox.showinfo("Current Date & Time", current_time)

# ایجاد دکمه‌ها با اندازه و رنگ مناسب
buttons = [
    ["7", "8", "9", "/", "√", "log"],
    ["4", "5", "6", "*", "ln", "exp"],
    ["1", "2", "3", "-", "abs", "!"],
    ["0", ".", "=", "+", "plot"],
    ["sin", "cos", "tan", "asin", "acos", "atan"],
    ["sinh", "cosh", "tanh", "radians", "degrees"],
    ["M+", "M-", "MR", "MC"],
]

# رنگ دکمه‌ها
button_colors = {
    "=": "#4CAF50",  # سبز
    "C": "#F44336",  # قرمز
    "Convert": "#FFC107",  # زرد
    "Date/Time": "#03A9F4",  # آبی
    "plot": "#8BC34A",  # سبز روشن
    "M+": "#FF5722",  # نارنجی
    "M-": "#FF5722",  # نارنجی
    "MR": "#FF5722",  # نارنجی
    "MC": "#FF5722",  # نارنجی
}

# قرار دادن دکمه‌ها در قاب
for r, row in enumerate(buttons):
    for c, btn in enumerate(row):
        if btn in ["Convert", "Date/Time"]:
            if btn == "Convert":
                CTkButton(frame, text=btn, command=convert_units, width=120, height=40, fg_color=button_colors[btn]).grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
            elif btn == "Date/Time":
                CTkButton(frame, text=btn, command=show_datetime, width=120, height=40, fg_color=button_colors[btn]).grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
        elif btn in ["sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh", "tanh", "radians", "degrees", "plot", "M+", "M-", "MR", "MC"]:
            CTkButton(frame, text=btn, command=lambda b=btn: button_advanced(b) if b not in ["M+", "M-", "MR", "MC"] else button_memory(b), width=60, height=40, fg_color=button_colors.get(btn, "#607D8B")).grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
        else:
            CTkButton(frame, text=btn, command=lambda b=btn: button_click(b) if b not in ["=", "C"] else (button_equal() if b == "=" else button_clear()), width=60, height=40, fg_color="#607D8B").grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# ایجاد جعبه ورودی برای تاریخ و زمان
datetime_label = CTkLabel(root, text="", font=('Arial', 16), anchor="w")
datetime_label.grid(row=2, column=0, columnspan=6, padx=10, pady=10, sticky="w")

def update_datetime():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    datetime_label.configure(text=current_time)
    root.after(1000, update_datetime)  # به‌روزرسانی هر ثانیه

update_datetime()

# ایجاد منوهای کشویی برای تبدیل واحدها
from_unit_menu = CTkComboBox(frame, values=units, variable=from_unit_var, width=120, height=40)
to_unit_menu = CTkComboBox(frame, values=units, variable=to_unit_var, width=120, height=40)
from_unit_menu.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")
to_unit_menu.grid(row=7, column=1, padx=5, pady=5, sticky="nsew")

# ایجاد دکمه تبدیل و تاریخ/زمان
CTkButton(frame, text="Convert", command=convert_units, width=120, height=40, fg_color=button_colors["Convert"]).grid(row=7, column=2, padx=5, pady=5, sticky="nsew")
CTkButton(frame, text="Date/Time", command=show_datetime, width=120, height=40, fg_color=button_colors["Date/Time"]).grid(row=7, column=3, padx=5, pady=5, sticky="nsew")

# تنظیم اندازه ستون‌ها و ردیف‌ها
for i in range(6):
    frame.grid_columnconfigure(i, weight=1)
for i in range(8):
    frame.grid_rowconfigure(i, weight=1)

# اجرای حلقه اصلی برنامه
root.mainloop()
