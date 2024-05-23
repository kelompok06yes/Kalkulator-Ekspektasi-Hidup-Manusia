import time
import customtkinter as ctk
from PIL import Image, ImageTk

def menu_utama():
    global window
    window = ctk.CTk()
    window.title("Kalkulator Ekspektasi Hidup Manusia")
    window.configure(bg="White", x=0, y=0)
    window.state("zoomed")
    window.resizable(True,True)

    bg_img = Image.open('Kalkulator-Ekspektasi-Hidup-Manusia/bg.png')
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
        font=("Arial", 15, "bold"), 
        bg_color="#FF914D", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=3, 
        text_color="black", 
        corner_radius=10, 
        hover_color="#F6E4BC",
        command= kalkulasi
    ).place(x=675, y=690)
    ctk.CTkButton(
        window, 
        width=355, 
        height=40, 
        text="History", 
        font=("Arial", 15, "bold"), 
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
    global window
    window = ctk.CTkToplevel()
    window.title("Kalkulasi")
    window.configure(bg="white")
    window.wm_state("zoomed")
    window.resizable(True, True)
    window.geometry("2560x1440")
    window.attributes('-topmost', True)
    # window.after_idle(window.attributes, '-topmost', False)

    bg_img = Image.open('Kalkulator-Ekspektasi-Hidup-Manusia/bg_kalkulasi.png')
    resized_bg_img = bg_img.resize((2560, 2048))
    bg_img_tk = ImageTk.PhotoImage(resized_bg_img)

    canvas_frame = ctk.CTkFrame(window)
    canvas_frame.pack(fill="both", expand=True)

    canvas = ctk.CTkCanvas(canvas_frame, width=2560, height=1440, scrollregion=(0, 0, 2560, 2048))
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_img_tk)

    scrollbar_y = ctk.CTkScrollbar(canvas_frame, command=canvas.yview)
    scrollbar_y.pack( side="right", fill="y")
    canvas.configure(bg="grey", width=20, yscrollcommand=scrollbar_y.set)

    canvas.bind("<MouseWheel>", lambda event: on_mouse_wheel(event, canvas))
    
    input_nama = ctk.CTkEntry(
        window, 
        placeholder_text="Masukkan nama Anda",
        placeholder_text_color="#EDBEA0",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50
    )
    canvas.create_window(706, 650, anchor="nw", window=input_nama)
    
    input_usia = ctk.CTkEntry(
        window, 
        placeholder_text="Masukkan umur Anda",
        placeholder_text_color="#EDBEA0",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50
    )
    canvas.create_window(1355, 650, anchor="nw", window=input_usia)

    pil_gender = ctk.CTkComboBox(
        window,
        values=["Laki-Laki", "Perempuan"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 20, "bold"),
        dropdown_text_color="black",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50,
    )
    pil_gender.set("Pilih Gender Anda")
    canvas.create_window(706, 848, anchor="nw", window=pil_gender)

    pil_pendidikan = ctk.CTkComboBox(
        window,
        values=["Pelajar/Mahasiswa", "Lulusan Universitas"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 20, "bold"),
        dropdown_text_color="black",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50,
    )
    pil_pendidikan.set("Pilih Pendidikan Anda")
    canvas.create_window(1355, 848, anchor="nw", window=pil_pendidikan)

    input_berat_badan = ctk.CTkEntry(
        window, 
        placeholder_text="Masukkan berat badan Anda",
        placeholder_text_color="#EDBEA0",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50
    )
    canvas.create_window(706, 1139, anchor="nw", window=input_berat_badan)

    input_tinggi_badan = ctk.CTkEntry(
        window, 
        placeholder_text="Masukkan tinggi badan Anda",
        placeholder_text_color="#EDBEA0",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50
    )
    canvas.create_window(1355, 1139, anchor="nw", window=input_tinggi_badan)

    pil_pola_makan = ctk.CTkComboBox(
        window,
        values=["Sehat", "Tidak Sehat"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 20, "bold"),
        dropdown_text_color="black",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50,
    )
    pil_pola_makan.set("Pilih Pola Makan")
    canvas.create_window(706, 1428, anchor="nw", window=pil_pola_makan)

    pil_perokok = ctk.CTkComboBox(
        window,
        values=["Tidak", "Ya"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 20, "bold"),
        dropdown_text_color="black",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50,
    )
    pil_perokok.set("Pilih Opsi")
    canvas.create_window(1355, 1428, anchor="nw", window=pil_perokok)

    pil_alkohol = ctk.CTkComboBox(
        window,
        values=["Tidak Pernah", "Ringan", "Sedang", "Berat"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 20, "bold"),
        dropdown_text_color="black",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50,
    )
    pil_alkohol.set("Pilih seberapa sering")
    canvas.create_window(706, 1626, anchor="nw", window=pil_alkohol)

    pil_obat_terlarang = ctk.CTkComboBox(
        window,
        values=["Tidak Pernah", "Ringan", "Berat"],
        dropdown_fg_color="#FFF4DC",
        dropdown_hover_color="#D16927",
        dropdown_font=("Arial", 20, "bold"),
        dropdown_text_color="black",
        bg_color="#FFF4DC", 
        fg_color="#FFF4DC", 
        border_color="#D16927", 
        border_width=2, 
        font=("Arial", 20, "bold"), 
        text_color="black",
        corner_radius=5,
        width= 338,
        height= 50,
    )
    pil_obat_terlarang.set("Pilih Opsi")
    canvas.create_window(1355, 1626, anchor="nw", window=pil_obat_terlarang)
    # apply_button = ctk.CTkButton(window, text="Apply", command=lambda: process_input(input_nama.get(), info_entry.get()))
    # canvas.create_window(20, 160, anchor="nw", window=apply_button)

    window.mainloop()

def process_input(name, info):
    # You can call other functions or perform any necessary actions here
    print(f"Name: {name}")
    print(f"Other Information: {info}")

def on_mouse_wheel(event, canvas):
    scroll_speed = int(-1*(event.delta/120))
    canvas.after_idle(canvas.yview_scroll, scroll_speed, "units")

def history():
    window.destroy()
    window = ctk.CTk()
    window.title("History")
    window.geometry("2560x1440")
    window.configure(bg="white")
    window.resizable(True, True)
    window.mainloop()