from logging import root
from tkinter import N, filedialog
from tkinter.ttk import LabelFrame
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *

root = Tk()
root.geometry("250x240")
root.resizable(False, False)
root.title("Sistem Prediksi Prestasi Ujian Siswa")
page_check = 0

def halamanAwal():
    global lblframe01, page_check
    if page_check == 0:
        pass
    elif page_check == 2:
        lblframe02.grid_forget()
    elif page_check == 3:
        lblframe03.grid_forget()
    elif page_check == 4 :
        lblframe04.grid_forget()
    elif page_check == 5 :
        lblframe05.grid_forget()
    page_check = 1
    lblframe01 = LabelFrame(root)
    lblframe01.grid()
    lbl = Label(lblframe01, text="PILIH MENU DIBAWAH INI!", padx=50, pady=20)
    lbl.grid(row=0, column=0)

    btn = Button(lblframe01, text="Math Score", command=halamanMath, padx=50, pady=10)
    btn.grid(row=1)

    btn2 = Button(lblframe01, text="Reading Score", command=halamanReading, padx=50, pady=10)
    btn2.grid(row=2)

    btn3 = Button(lblframe01, text="Writing Score", command=halamanWriting, padx=50, pady=10)
    btn3.grid(row=3)

    btn4 = Button(lblframe01, text="Total Score", command=halamanTotal, padx=50, pady=10)
    btn4.grid(row=4)

def halamanMath():
    lblframe01.grid_forget()
    global lblframe02, page_check
    page_check = 2
    lblframe02 = LabelFrame(root)

    file_path = filedialog.askopenfilename()
    data = pd.read_excel(file_path)
    data = data.set_index("parental level of education")
    data = data.reset_index()
    print(data)

    sns.lineplot(data=data, x="parental level of education", y="math score total")
    plt.show()
    halamanAwal()


def halamanReading():
    lblframe01.grid_forget()
    global lblframe03, page_check
    page_check = 3
    lblframe03 = LabelFrame(root)

    file_path = filedialog.askopenfilename()
    data = pd.read_excel(file_path)
    data = data.set_index("parental level of education")
    data = data.reset_index()
    print(data)

    sns.lineplot(data=data, x="parental level of education", y="reading score total")
    plt.show()
    halamanAwal()

def halamanWriting():
    lblframe01.grid_forget()
    global lblframe04, page_check
    page_check = 4
    lblframe04 = LabelFrame(root)

    file_path = filedialog.askopenfilename()
    data = pd.read_excel(file_path)
    data = data.set_index("parental level of education")
    data = data.reset_index()
    print(data)

    sns.lineplot(data=data, x="parental level of education", y="writing score total")
    plt.show()
    halamanAwal()

def halamanTotal():
    lblframe01.grid_forget()
    global lblframe05, page_check
    page_check = 5
    lblframe05 = LabelFrame(root)

    file_path = filedialog.askopenfilename()
    data = pd.read_excel(file_path)
    data = data.set_index("parental level of education")
    data = data.reset_index()
    print(data)

    sns.barplot(data=data, x="parental level of education", y="total score")
    plt.show()
    halamanAwal()

halamanAwal()
root.mainloop()