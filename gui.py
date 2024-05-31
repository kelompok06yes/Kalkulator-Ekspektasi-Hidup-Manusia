import kalkulasi as op
import history as hs
import tkinter as tk
from tkinter import *
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from PIL import Image, ImageTk, ImageGrab
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def menu_utama():
    global window
    window = ctk.CTk()
    window.title("Kalkulator Ekspektasi Hidup Manusia")
    window.configure(bg="White", x=0, y=0)
    window.state("zoomed")
    window.resizable(True,True)

    bg_img = Image.open('Kalkulator-Ekspektasi-Hidup-Manusia/bg_menu_utama.png')
    resized_bg_img = bg_img.resize((2560, 1440))
    bg_img_tk = ImageTk.PhotoImage(resized_bg_img)

    canvas = ctk.CTkCanvas(window, width=2560, height=1440)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_img_tk)

    ctk.CTkButton(
        window, 
        width=355, 
        height=40, 
        text="Kalkulasi", 
        font=("hywenhei-85w", 15, "bold"),  
        bg_color="#FF914D", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=3, 
        text_color="#644633", 
        corner_radius=10, 
        hover_color="#F6E4BC",
        command= kalkulasi
    ).place(x=675, y=690)
    ctk.CTkButton(
        window, 
        width=355, 
        height=40, 
        text="History", 
        font=("hywenhei-85w", 15, "bold"),   
        bg_color="#FF914D", 
        fg_color="#D16927", 
        border_color="#D16927", 
        border_width=3, 
        text_color="#FFF4DC",
        corner_radius=10, 
        hover_color="#BB5F25",
        command= history
    ).place(x=675, y=740)
    
    window.mainloop()

def kalkulasi():
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def validasi(nama, usia, gender, pendidikan, berat, tinggi, pola, perokok, alkohol, obat):
        errors = []
        if not usia.isdigit() or not (0 <= int(usia) < 40):
            errors.append("Usia harus angka dan kurang dari 40.")
        
        if not is_number(berat):
            errors.append("Berat badan harus angka.")
        
        if not is_number(tinggi):
            errors.append("Tinggi badan harus angka.")
        
        if gender == "Pilih opsi":
            errors.append("Gender harus dipilih.")
        
        if pendidikan == "Pilih opsi":
            errors.append("Pendidikan harus dipilih.")
        
        if pola == "Pilih opsi":
            errors.append("Pola makan harus dipilih.")
        
        if perokok == "Pilih opsi":
            errors.append("Status perokok harus dipilih.")
        
        if alkohol == "Pilih opsi":
            errors.append("Konsumsi alkohol harus dipilih.")
        
        if obat == "Pilih opsi":
            errors.append("Penggunaan obat terlarang harus dipilih.")
        
        errors = "\n\n".join(errors)
        if errors:
            CTkMessagebox(
                title="Kesalahan Input !!!", 
                title_color="#F6E4BC",
                width= 1000,
                height= 20,
                fg_color="#FFF4DC",
                bg_color="#D16927",
                border_color="#8F4D09",
                border_width=3,
                corner_radius=10,
                font=("hywenhei-85w", 13, "normal"),
                text_color="#8F4D09",
                message=errors,
                icon="warning", 
                option_1="OK",
                options=errors,
                button_color="#F6E4BC",
                button_height=30,
                button_width=100,
                button_hover_color="#FFF4DC",
                button_text_color="#644633",
                cancel_button_color="#D16927",
            )
            return
        
        processing_data(nama, usia, gender, pendidikan, berat, tinggi, pola, perokok, alkohol, obat)

    global window_kalkulasi
    window_kalkulasi = ctk.CTkToplevel()
    window_kalkulasi.title("Kalkulasi")
    window_kalkulasi.configure(bg="white")
    window_kalkulasi.wm_state("zoomed")
    window_kalkulasi.resizable(True, True)
    window_kalkulasi.geometry("2560x1440")
    window_kalkulasi.attributes('-topmost', True)

    bg_img = Image.open('Kalkulator-Ekspektasi-Hidup-Manusia/bg_kalkulasi.png')
    resized_bg_img = bg_img.resize((2560, 2048))
    bg_img_tk = ImageTk.PhotoImage(resized_bg_img)

    canvas_frame = ctk.CTkFrame(window_kalkulasi)
    canvas_frame.pack(fill="both", expand=True)

    canvas = ctk.CTkCanvas(canvas_frame, width=2560, height=1440, scrollregion=(0, 0, 2560, 2048))
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_img_tk)

    scrollbar_y = ctk.CTkScrollbar(canvas_frame, command=canvas.yview, button_color='#FFF4DC', button_hover_color='#F6E4BC', fg_color='#D16927')
    scrollbar_y.pack( side="right", fill="y")
    canvas.configure(bg="grey", width=20, yscrollcommand=scrollbar_y.set)
    canvas.bind("<MouseWheel>", lambda event: on_mouse_wheel(event, canvas))
    
    input_nama = ctk.CTkEntry(
        window_kalkulasi, 
        placeholder_text="Masukkan nama Anda",
        placeholder_text_color="#EDBEA0",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45
    )
    canvas.create_window(785, 625, anchor="nw", window=input_nama)
    
    input_usia = ctk.CTkEntry(
        window_kalkulasi, 
        placeholder_text="Masukkan umur Anda",
        placeholder_text_color="#EDBEA0",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45
    )
    canvas.create_window(1339, 625, anchor="nw", window=input_usia)

    pil_gender = ctk.CTkComboBox(
        window_kalkulasi,
        values=["Laki-Laki", "Perempuan"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 17, "bold"),
        dropdown_text_color="black",
        button_color='#D16927',
        button_hover_color="#BB5F25",
        state="readonly",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45,
    )
    pil_gender.set("Pilih opsi")
    canvas.create_window(785, 791, anchor="nw", window=pil_gender)

    pil_pendidikan = ctk.CTkComboBox(
        window_kalkulasi,
        values=["Pelajar/Mahasiswa", "Lulusan Universitas"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 17, "bold"),
        dropdown_text_color="black",
        button_color='#D16927',
        button_hover_color="#BB5F25",
        state="readonly",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45,
    )
    pil_pendidikan.set("Pilih opsi")
    canvas.create_window(1339, 791, anchor="nw", window=pil_pendidikan)

    input_berat_badan = ctk.CTkEntry(
        window_kalkulasi, 
        placeholder_text="Berat badan dalam Kg",
        placeholder_text_color="#EDBEA0",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45
    )
    canvas.create_window(785, 1038, anchor="nw", window=input_berat_badan)

    input_tinggi_badan = ctk.CTkEntry(
        window_kalkulasi, 
        placeholder_text="Tinggi badan dalam Cm",
        placeholder_text_color="#EDBEA0",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45
    )
    canvas.create_window(1339, 1038, anchor="nw", window=input_tinggi_badan)

    pil_pola_makan = ctk.CTkComboBox(
        window_kalkulasi,
        values=["Sehat", "Tidak Sehat"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 17, "bold"),
        dropdown_text_color="black",
        button_color='#D16927',
        button_hover_color="#BB5F25",
        state="readonly",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45,
    )
    pil_pola_makan.set("Pilih opsi")
    canvas.create_window(785, 1285, anchor="nw", window=pil_pola_makan)

    pil_perokok = ctk.CTkComboBox(
        window_kalkulasi,
        values=["Tidak", "Ya"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 17, "bold"),
        dropdown_text_color="black",
        button_color='#D16927',
        button_hover_color="#BB5F25",
        state="readonly",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45,
    )
    pil_perokok.set("Pilih opsi")
    canvas.create_window(1339, 1285, anchor="nw", window=pil_perokok)

    pil_alkohol = ctk.CTkComboBox(
        window_kalkulasi,
        values=["Tidak Pernah", "Ringan", "Sedang", "Berat"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 17, "bold"),
        dropdown_text_color="black",
        button_color='#D16927',
        button_hover_color="#BB5F25",
        state="readonly",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45,
    )
    pil_alkohol.set("Pilih opsi")
    canvas.create_window(785, 1452, anchor="nw", window=pil_alkohol)

    pil_obat_terlarang = ctk.CTkComboBox(
        window_kalkulasi,
        values=["Tidak Pernah", "Ringan", "Berat"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 17, "bold"),
        dropdown_text_color="black",
        button_color='#D16927',
        button_hover_color="#BB5F25",
        state="readonly",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 290,
        height= 45,
    )
    pil_obat_terlarang.set("Pilih opsi")
    canvas.create_window(1339, 1452, anchor="nw", window=pil_obat_terlarang)

    button_kalkulasi = ctk.CTkButton(
        window_kalkulasi, 
        width=200, 
        height=45, 
        text="Hitung", 
        font=("hywenhei-85w", 17, "bold"), 
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=3, 
        text_color="#D16927",
        corner_radius=10, 
        hover_color="#F6E4BC",
        command=lambda: validasi(
            input_nama.get(),
            input_usia.get(),
            pil_gender.get(),
            pil_pendidikan.get(),
            input_berat_badan.get(),
            input_tinggi_badan.get(),
            pil_pola_makan.get(),
            pil_perokok.get(),
            pil_alkohol.get(),
            pil_obat_terlarang.get()
        )
    )
    canvas.create_window(1400, 1630, anchor="nw", window=button_kalkulasi)

    button_kembali = ctk.CTkButton(
        window_kalkulasi, 
        width=200, 
        height=45, 
        text="Back", 
        font=("hywenhei-85w", 17, "bold"), 
        bg_color="#FFF4DC", 
        fg_color="#D16927", 
        border_color="#D16927", 
        border_width=3, 
        text_color="#FFF4DC",
        corner_radius=10, 
        hover_color="#BB5F25",
        command=window_kalkulasi.destroy
    )
    canvas.create_window(860, 1630, anchor="nw", window=button_kembali)

    window_kalkulasi.mainloop()

def processing_data(nama, usia, gender, pendidikan, berat, tinggi, pola, perokok, alkohol, obat):
    window_kalkulasi.attributes('-topmost', False)
    usia = int(usia)
    berat = float(berat)
    tinggi = float(tinggi)
    data = [
        nama,
        usia,
        gender,
        pendidikan,
        berat,
        tinggi,
        pola,
        perokok,
        alkohol,
        obat
    ]

    def angka_harapan_hidup():
        bmi = op.index_bmi(data[5], data[4])
        ahh, ket = op.kategori_bmi(data[2], bmi)
        ahh = op.kategori_pola_makan(data[6], ahh)
        ahh = op.kategori_perokok(data[7], ahh)
        ahh = op.kategori_pengonsumsi_alkohol(data[8], ahh)
        ahh = op.kategori_pengguna_obat_terlarang(data[9], ahh)
        return bmi, ahh, ket

    bmi, ahh, ket = angka_harapan_hidup()
    sisa_umur = ahh - data[1]

    hs.create_excel_history(
                data[0],
                data[1],
                data[2],
                data[3], 
                data[6], 
                data[7], 
                data[8], 
                data[9],
                bmi, 
                ahh,
                sisa_umur,
            )
    
    laporan (hs.display_history())
    
def on_mouse_wheel(event, canvas):
    scroll_speed = int(-1*(event.delta/120))
    canvas.after_idle(canvas.yview_scroll, scroll_speed, "units")

def laporan(data):
    global window_laporan
    window_laporan = ctk.CTkToplevel()
    window_laporan.title("Laporan")
    window_laporan.configure(bg="white")
    window_laporan.wm_state("zoomed")
    window_laporan.resizable(True, True)
    window_laporan.geometry("2560x1440")
    window_laporan.attributes('-topmost', True)

    bg_img = Image.open('Kalkulator-Ekspektasi-Hidup-Manusia/bg_laporan.png')
    resized_bg_img = bg_img.resize((2560, 1440))
    bg_img_tk = ImageTk.PhotoImage(resized_bg_img)

    canvas = ctk.CTkCanvas(window_laporan, width=2560, height=1440)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_img_tk)

    nama = data[0]
    ahh = data[1]
    sisa_umur = data[2]
    label_nama = ctk.CTkLabel(
        window_laporan, 
        width=1,
        height=1,
        bg_color="#FFF4DC",
        fg_color="#FFF4DC",
        text=f"{nama}", 
        text_color="#644633",
        font=("hywenhei-85w", 45, "normal"), 
        
    )
    canvas.create_window(1280, 433, anchor="center", window=label_nama)

    label_ahh = ctk.CTkLabel(
        window_laporan, 
        width=1,
        height=1,
        bg_color="#FFF4DC",
        fg_color="#FFF4DC",
        text=f"{ahh}", 
        text_color="#644633",
        font=("hywenhei-85w", 110, "normal"), 
        
    )
    canvas.create_window(1280, 647, anchor="center", window=label_ahh)

    label_sisa_umur = ctk.CTkLabel(
        window_laporan, 
        width=1,
        height=1,
        bg_color="#FFF4DC",
        fg_color="#FFF4DC",
        text=f"{sisa_umur}", 
        text_color="#644633",
        font=("hywenhei-85w", 30, "bold"), 
        
    )
    canvas.create_window(1742, 780, anchor="center", window=label_sisa_umur)

    button_save = ctk.CTkButton(
        window_laporan, 
        width=200, 
        height=45, 
        text="Save", 
        font=("Arial", 17, "bold"), 
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=3, 
        text_color="#D16927",
        corner_radius=10, 
        hover_color="#F6E4BC",
        command=lambda: save_as_pdf(window_laporan, nama)
    )
    canvas.create_window(1330, 1150, anchor="nw", window=button_save)

    button_kembali = ctk.CTkButton(
        window_laporan,  
        width=200, 
        height=45, 
        text="Back", 
        font=("Arial", 17, "bold"), 
        bg_color="#FFF4DC", 
        fg_color="#D16927", 
        border_color="#8F4D09", 
        border_width=3, 
        text_color="#FFF4DC",
        corner_radius=10, 
        hover_color="#BB5F25",
        command=window_laporan.destroy
    )
    canvas.create_window(930, 1150, anchor="nw", window=button_kembali)
    window_laporan.mainloop()

def history():
    def on_item_click(event):
        selected_item = tabel.focus()
        selected_values = tabel.item(selected_item, 'values')
        selected_name = selected_values[0]  
        window_history.attributes('-topmost', False)
        laporan(hs.display_history(selected_name))

    def add_data_to_table(data):
        tabel.delete(*tabel.get_children())
        for index, row in enumerate(data):
            tag = 'evenrow' if index % 2 == 0 else 'oddrow'
            tabel.insert(parent='', index=0, iid=index, values=row, tags=(tag,))

    def search_data():
        search_term = input_nama.get().lower()
        gender_term = pil_gender.get()
        education_term = pil_pendidikan.get()
        filtered_data = [row for row in hs.read_nama() if
                         (search_term in row[0].lower()) and
                         (gender_term == "Cari Berdasar Gender" or row[1] == gender_term) and
                         (education_term == "Cari Berdasar Status" or row[2] == education_term)]
        add_data_to_table(filtered_data)

    def delete_selected():
        selected_items = tabel.selection()
        for selected_item in selected_items:
            selected_values = tabel.item(selected_item, 'values')
            selected_name = selected_values[0]
            tabel.delete(selected_item)
            hs.delete_data(selected_name)

    global window_history 
    window_history = ctk.CTkToplevel()
    window_history.title("History")
    window_history.configure(bg="white")
    window_history.wm_state("zoomed")
    window_history.resizable(True, True)
    window_history.geometry("2560x1440")
    window_history.attributes('-topmost', True)

    bg_img = Image.open('Kalkulator-Ekspektasi-Hidup-Manusia/bg_history.png')
    resized_bg_img = bg_img.resize((2560, 1440))
    bg_img_tk = ImageTk.PhotoImage(resized_bg_img)

    canvas = ctk.CTkCanvas(window_history, width=2560, height=1440)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_img_tk)

    main_frame = ctk.CTkFrame(
        window_history, 
        width=1000,  
        height=400,
        fg_color="#D16927",
        bg_color="#FFF4DC",
        border_color="#8F4D09",
        border_width=3,
        corner_radius=10
    )
    canvas.create_window(1280, 850, anchor="center", window=main_frame)

    frame = ctk.CTkFrame(window_history)
    canvas.create_window(1700, 853, anchor="center", window=frame)

    frame1 = ctk.CTkScrollableFrame(
        frame,
        width=385,  
        height=347,
        fg_color="#D16927",
        bg_color="#D16927",
        border_color="#8F4D09",
        border_width=0,
        corner_radius=0,
        scrollbar_button_color="#8F4D09",
        scrollbar_button_hover_color="#7B4309",
        scrollbar_fg_color="#D16927"
        
    )
    frame1.pack(fill="both", expand=True)     

    data = hs.read_nama()

    style = ttk.Style(window_history)
    style.theme_use("clam")

    style.configure("Treeview", 
        padding=5,
        font=("Arial", 17, "bold"), 
        foreground='#000000', 
        background="#FFF4DC",
        fieldbackground="#FFF4DC",
        rowheight=45,  
        bordercolor="#8F4D09",  
        relief="solid",  
        bordersize=2
    )
    style.configure("Treeview.Heading", 
        font=("Arial", 16, "bold"),
        foreground="#FFF4DC", 
        background="#D16927",
        bordercolor="#8F4D09",  
        relief="solid",  
        bordersize=2
    )
    style.configure("Treeview.Row", 
        background=[('#FFF4DC','#EBDDBE')],
    )
    style.map('Treeview', 
        background = [('selected', '#8F4D09')],
    )
    style.map('Treeview.Heading', 
        background = [('active', '#BB5F25')],
    )

    tabel = ttk.Treeview(frame1, height=15, show='headings')
    tabel['columns'] = ('Nama', 'Gender', 'Status')

    tabel.column('#0', width=0, stretch=tk.NO)
    tabel.column('Nama', anchor=tk.W, width=150)
    tabel.column('Gender', anchor=tk.W, width=150)
    tabel.column('Status', anchor=tk.W, width=250)

    tabel.heading('Nama', text='Nama', anchor=tk.CENTER)
    tabel.heading('Gender', text='Gender', anchor=tk.CENTER)
    tabel.heading('Status', text='Status', anchor=tk.CENTER)

    for index, row in enumerate(data):
        tag = 'evenrow' if index % 2 == 0 else 'oddrow'
        tabel.insert(parent='', index=0, iid=index, values=row, tags=(tag,))

    tabel.tag_configure('evenrow', background='#FFF4DC')
    tabel.tag_configure('oddrow', background='#EBDDBE')

    tabel.pack()
    tabel.bind('<ButtonRelease-1>', on_item_click)
    
    input_nama = ctk.CTkEntry(
        window_history, 
        placeholder_text="Masukkan nama yang ingin dicari",
        placeholder_text_color="#EDBEA0",
        bg_color="#D16927", 
        fg_color="#FFF4DC", 
        border_color="#8F4D09", 
        border_width=3, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=10,
        width= 500,
        height= 45
    )
    canvas.create_window(950, 625, anchor="center", window=input_nama)  

    label_advance = ctk.CTkButton(
        window_history, 
        width=500,
        height=30,
        bg_color="#D16927",
        fg_color="#F6E4BC",
        corner_radius=10,
        text='Pencarian Lanjut', 
        text_color="#644633",
        font=("hywenhei-85w", 20, "bold"), 
        border_color="#8F4D09", 
        border_width=3, 
        state='readonly',
    )
    canvas.create_window(575, 705, anchor="nw", window=label_advance)

    pil_gender = ctk.CTkComboBox(
        window_history,
        values=["Laki-Laki", "Perempuan"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 17, "bold"),
        dropdown_text_color="black",
        button_color='#8F4D09',
        button_hover_color="#BB5F25",
        state="readonly",
        bg_color="#D16927", 
        fg_color="#FFF4DC", 
        border_color="#8F4D09", 
        border_width=3, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=10,
        width= 500,
        height= 45,
    )
    pil_gender.set("Cari Berdasar Gender")
    canvas.create_window(575, 780, anchor="nw", window=pil_gender)

    pil_pendidikan = ctk.CTkComboBox(
        window_history,
        values=["Pelajar/Mahasiswa", "Lulusan Universitas"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 17, "bold"),
        dropdown_text_color="black",
        button_color='#8F4D09',
        button_hover_color="#BB5F25",
        state="readonly",
        bg_color="#D16927", 
        fg_color="#FFF4DC", 
        border_color="#8F4D09", 
        border_width=3, 
        font=("Arial", 17, "bold"), 
        text_color="black",
        corner_radius=10,
        width= 500,
        height= 45,
    )
    pil_pendidikan.set("Cari Berdasar Status")
    canvas.create_window(575, 870, anchor="nw", window=pil_pendidikan)

    button_cari = ctk.CTkButton(
        window_history, 
        width=500, 
        height=45, 
        text="Cari", 
        font=("hywenhei-85w", 17, "bold"),
        bg_color="#D16927", 
        fg_color="#F6E4BC", 
        border_color="#8F4D09", 
        border_width=3, 
        text_color="#644633",
        corner_radius=10, 
        hover_color="#FFF4DC",
        command=search_data
        )
    canvas.create_window(575, 980, anchor="nw", window=button_cari)

    button_delete = ctk.CTkButton(
        window_history, 
        width=500, 
        height=45, 
        text="Hapus History", 
        font=("hywenhei-85w", 17, "bold"),
        bg_color="#D16927", 
        fg_color="#990A0A", 
        border_color="#8F4D09", 
        border_width=3, 
        text_color="#FFF4DC",
        corner_radius=10, 
        hover_color="#AD0A0A",
        command=delete_selected
        )
    canvas.create_window(575, 1050, anchor="nw", window=button_delete)

    button_kembali = ctk.CTkButton(
        window_history,  
        width=200, 
        height=45, 
        text="Back", 
        font=("hywenhei-85w", 17, "bold"),
        bg_color="#FFF4DC", 
        fg_color="#D16927", 
        border_color="#8F4D09", 
        border_width=3, 
        text_color="#FFF4DC",
        corner_radius=10, 
        hover_color="#BB5F25",
        command=window_history.destroy
    )
    canvas.create_window(528, 1160, anchor="nw", window=button_kembali)

    kolom_nama = ctk.CTkButton(
        window_history, 
        width=106,
        height=30,
        bg_color="#D16927",
        fg_color="#F6E4BC",
        corner_radius=10,
        text='Nama', 
        text_color="#644633",
        font=("hywenhei-85w", 13, "bold"), 
        border_color="#8F4D09", 
        border_width=3, 
        state='readonly',
    )
    canvas.create_window(1405, 590, anchor="nw", window=kolom_nama)

    kolom_gender = ctk.CTkButton(
        window_history, 
        width=100,
        height=30,
        bg_color="#D16927",
        fg_color="#F6E4BC",
        corner_radius=10,
        text='Gender', 
        text_color="#644633",
        font=("hywenhei-85w", 13, "bold"), 
        border_color="#8F4D09", 
        border_width=3, 
        state='readonly',
    )
    canvas.create_window(1563, 590, anchor="nw", window=kolom_gender)

    kolom_status = ctk.CTkButton(
        window_history, 
        width=172,
        height=30,
        bg_color="#D16927",
        fg_color="#F6E4BC",
        corner_radius=10,
        text='Status', 
        text_color="#644633",
        font=("hywenhei-85w", 13, "bold"), 
        border_color="#8F4D09", 
        border_width=3, 
        state='readonly',
    )
    canvas.create_window(1713, 590, anchor="nw", window=kolom_status)

    window_history.mainloop()

def save_as_pdf(window, nama):
    window.update_idletasks()
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    width = window.winfo_width()
    height = window.winfo_height()

    image = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    temp_image_path = "Kalkulator-Ekspektasi-Hidup-Manusia/Laporan/temp_laporan.png"
    image.save(temp_image_path)

    pdf_path = f"Kalkulator-Ekspektasi-Hidup-Manusia/Laporan/Laporan {nama}.pdf"
    c = canvas.Canvas(pdf_path, pagesize=(width, height))

    c.drawImage(temp_image_path, 0, 0, width=width, height=height)
    c.save()

    import os
    os.remove(temp_image_path)
    CTkMessagebox(
        master=window_laporan,
        title="Laporan Anda Berhasil Disimpan", 
        title_color="#F6E4BC",
        width= 600,
        height= 20,
        fg_color="#FFF4DC",
        bg_color="#D16927",
        border_color="#8F4D09",
        border_width=3,
        corner_radius=10,
        font=("hywenhei-85w", 13, "normal"),
        text_color="#8F4D09",
        message=f"Laporan disimpan sebagai {nama}.pdf",
        icon="check", 
        option_1="OK",
        button_color="#F6E4BC",
        button_height=30,
        button_width=100,
        button_hover_color="#FFF4DC",
        button_text_color="#644633",
        cancel_button_color="#D16927",
    )
