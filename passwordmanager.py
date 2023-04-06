import tkinter as tk
from tkinter import messagebox
from random import choice
import string
import os

# Ana Pencere
root = tk.Tk()
root.title("Password Manager")

# Şifre Oluşturma Fonksiyonu
def generate_password():
    password_length = int(length_entry.get())
    if password_length < 6:
        messagebox.showerror("Hata", "Şifre uzunluğu en az 6 karakter olmalıdır!")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Şifre Kaydetme Fonksiyonu
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not website or not username or not password:
        messagebox.showerror("Hata", "Boş alan bırakmayınız!")
        return

    file_path = r"C:\Password\passwords.txt"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "a") as file:
        file.write(f"Website: {website}\n")
        file.write(f"Kullanıcı Adı: {username}\n")
        file.write(f"Şifre: {password}\n\n")
        messagebox.showinfo("Başarılı", "Şifre kaydedildi!")

# GUI Elemanları
website_label = tk.Label(root, text="Website:")
website_label.grid(row=0, column=0, padx=10, pady=10)
website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1, padx=10, pady=10)

username_label = tk.Label(root, text="Kullanıcı Adı:")
username_label.grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1, padx=10, pady=10)

password_label = tk.Label(root, text="Şifre:")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root)
password_entry.grid(row=2, column=1, padx=10, pady=10)

length_label = tk.Label(root, text="Şifre Uzunluğu:")
length_label.grid(row=3, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=3, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Şifre Oluştur", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

save_button = tk.Button(root, text="Şifreyi Kaydet", command=save_password)
save_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
