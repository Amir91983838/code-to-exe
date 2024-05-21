import tkinter as tk
from tkinter import filedialog, ttk
import PyInstaller.__main__
import os
from threading import Thread


def convert_to_exe():
    file_path = filedialog.askopenfilename(title="انتخاب فایل پایتون", filetypes=[("Python Files", "*.py")])
    if file_path:
        loading_label.config(text="لطفا منتظر بمانید...", foreground="blue")
        progress_bar.start()
        t = Thread(target=convert_and_show_message, args=(file_path,))
        t.start()


def convert_and_show_message(file_path):
    directory = os.path.dirname(file_path)
    file_name = os.path.basename(file_path).split('.')[0]
    exe_file_path = os.path.join(directory, file_name + ".exe")

    PyInstaller.__main__.run([
        file_path,
        '--onefile',
        '--windowed',
        '--distpath',
        directory,
        '--name',
        file_name
    ])
    progress_bar.stop()
    loading_label.config(text="فایل به exe تبدیل شد!", foreground="green")


def main():
    root = tk.Tk()
    root.title("تبدیل به فایل exe")
    root.geometry("400x250")  # تعیین اندازه پنجره

    label = tk.Label(root, text="برنامه‌ی خود را به فایل exe تبدیل کنید", font=("Helvetica", 14))
    label.pack(pady=20)

    convert_button = tk.Button(root, text="انتخاب فایل", font=("Helvetica", 12), command=convert_to_exe)
    convert_button.pack()

    global loading_label
    loading_label = tk.Label(root, text="", font=("Helvetica", 12))
    loading_label.pack(pady=10)

    global progress_bar
    progress_bar = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=200)
    progress_bar.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
