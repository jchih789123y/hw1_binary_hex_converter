import tkinter as tk

window = tk.Tk()
window.title("進位轉換器")
window.geometry("400x500")

result_label = tk.Label(window, text="")
result_label.pack()

# 十轉二
def dec_to_bin(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n = n // 2
    return result

# 十六轉十
def hex_to_dec(hex_str):
    hex_text = "0123456789ABCDEF"
    result = 0
    for ch in hex_str:
        result = result * 16 + hex_text.index(ch)
    return result

# 二轉十
def bin_to_dec(binary):
    result = 0
    for digit in binary:
        result = result * 2 + int(digit)
    return result

# 十轉十六
def dec_to_hex(n):
    if n == 0:
        return "0"
    hex_text = "0123456789ABCDEF"
    result = ""
    while n > 0:
        result = hex_text[n % 16] + result
        n = n // 16
    return result

# 驗證輸入是否合法

def is_binary(s):
    if s == "":
        return False
    for ch in s:
        if ch not in "01":
            return False
    return True

def is_decimal(s):
    return s.isdigit()

def is_hexadecimal(s):
    if s == "":
        return False
    valid = "0123456789ABCDEF"
    for ch in s:
        if ch not in valid:
            return False
    return True

# 介面功能
def convert():
    number = entry.get().strip().upper()
    base = base_var.get()

    if base == "2":
        if not is_binary(number):
            result_label.config(text="錯誤：請輸入2 進位數字")
            return
        dec_value = bin_to_dec(number)

    elif base == "10":
        if not is_decimal(number):
            result_label.config(text="錯誤：請輸入10 進位數字")
            return
        dec_value = int(number)

    elif base == "16":
        if not is_hexadecimal(number):
            result_label.config(text="錯誤：請輸入16 進位數字")
            return
        dec_value = hex_to_dec(number)

    else:
        result_label.config(text="錯誤：請選擇輸入進位")
        return

    binary_result = dec_to_bin(dec_value)
    decimal_result = str(dec_value)
    hex_result = dec_to_hex(dec_value)

    result_label.config(
        text="2進位： " + binary_result + "\n"
           + "10進位： " + decimal_result + "\n"
           + "16進位： " + hex_result
    )
    

# 內容元件設定
input_label = tk.Label(window, text="請輸入數字：")
input_label.pack()

entry = tk.Entry(window, width=30)
entry.pack(pady=5)

base_var = tk.StringVar()
base_var.set("10")

radio_frame = tk.Frame(window)
radio_frame.pack(pady=10)

tk.Label(radio_frame, text="輸入的進位：").pack(side="left")
tk.Radiobutton(radio_frame, text="2進位", variable=base_var, value="2").pack(side="left")
tk.Radiobutton(radio_frame, text="10進位", variable=base_var, value="10").pack(side="left")
tk.Radiobutton(radio_frame, text="16進位", variable=base_var, value="16").pack(side="left")

convert_button = tk.Button(window, text="轉換", command=convert)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

window.mainloop()
