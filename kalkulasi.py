def index_bmi (tinggi_badan, berat_badan) :
    tinggi = tinggi_badan/ 100 
    bmi = berat_badan / (tinggi ** 2)
    return bmi

def kategori_bmi (gender, bmi) :
    if gender == 'Laki-Laki' :
        ahh = 73
        if bmi < 17 :
            ahh -= 4
            ket = 'Kurus'
        elif bmi >= 17 and bmi <= 24.9 :
            ahh -= 0
            ket = 'Normal'
        elif bmi >= 25 :
            ahh -= -4
            ket = 'Kegemukan'
        return ahh, ket
    elif gender == 'Perempuan' :
        ahh = 78
        if bmi < 17 :
            ahh -= 4
            ket = 'Kurus'
        elif bmi >= 17 and bmi <= 24.9 :
            ahh -= 0
            ket = 'Normal'
        elif bmi >= 25 :
            ahh -= -4
            ket = 'Kegemukan'
        return ahh, ket
    else :
        return 'Error'
    
def kategori_pola_makan (pola_makan, ahh) :
    if pola_makan == 'Sehat' :
        ahh = ahh + 10
    else :
        ahh = ahh
    return ahh

def kategori_perokok (perokok, ahh) :
    if perokok == 'Ya' :
        ahh = ahh - 10
    else :
        ahh = ahh
    return ahh

def kategori_pengonsumsi_alkohol (alkohol, ahh) :
    if alkohol == 'Ringan' :
        ahh = ahh - 2
    elif alkohol == 'Sedang' :
        ahh = ahh - 6
    elif alkohol == 'Berat' :
        ahh = ahh - 8
    elif alkohol == 'Tidak Pernah' :
        ahh = ahh
    return ahh

def kategori_pengguna_obat_terlarang (obat_terlarang, ahh) :
    if obat_terlarang == 'Ringan' :
        ahh = ahh - 5
    elif obat_terlarang == 'Berat' :
        ahh = ahh - 10
    elif obat_terlarang == 'Tidak Pernah' :
        ahh = ahh 
    return ahh
