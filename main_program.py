import kalkulasi as op
import inputs as inp
import history as hs

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Kalkulasi")
        print("2. History")
        print("0. Keluar")

        choice = input("Pilih menu : ")

        if choice == "1":
            nama = inp.nama()
            umur = inp.umur()
            status = inp.pil_pendidikan()
            tinggi_badan = inp.tinggi_badan()
            berat_badan = inp.berat_badan()
            gender = inp.pil_gender()
            pola_makan = inp.pil_pola_makan()
            perokok = inp.pil_perokok()
            alkohol = inp.pil_alkohol()
            obat_terlarang = inp.pil_obat_terlarang()

            def angka_harapan_hidup():
                bmi = op.index_bmi(tinggi_badan, berat_badan)
                ahh, ket = op.kategori_bmi(gender[0], bmi)
                ahh = op.kategori_pola_makan(pola_makan[0], ahh)
                ahh = op.kategori_perokok(perokok[0], ahh)
                ahh = op.kategori_pengonsumsi_alkohol(alkohol[0], ahh)
                ahh = op.kategori_pengguna_obat_terlarang(obat_terlarang[0], ahh)
                return bmi, ahh, ket

            bmi, ahh, ket = angka_harapan_hidup()
            sisa_umur = ahh - umur
            hs.create_excel_history(
                nama,
                umur,
                gender[1],
                status[1], 
                pola_makan[1], 
                perokok[1], 
                alkohol[1], 
                obat_terlarang[1],
                bmi, 
                ahh,
                sisa_umur,
            )

            print(f"Nama\t\t\t:{nama}")
            print(f"Umur\t\t\t:{umur}")
            print(f"Gender\t\t\t:{gender[1]}")
            print(f"Status\t\t\t:{status[1]}")
            print(f"BMI\t\t\t:{bmi:.2f}")
            print(f"Kategori\t\t:{ket}")
            print(f"Angka Harapan Hidup\t:{ahh}")
            print(f"Sisa Umur\t\t:{sisa_umur}")
            

        elif choice == "2":
            hs.display_history(input('Masukan nama yang dicari :'))

        elif choice == "0":
            print("Terima kasih!")
            break

        else:
            print("Pilihan menu salah. Silakan coba lagi.")

main_menu()