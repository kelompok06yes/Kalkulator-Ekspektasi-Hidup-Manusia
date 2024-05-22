def index_bmi (tinggi_badan, berat_badan) :
    tinggi = tinggi_badan/ 100 
    bmi = berat_badan / (tinggi ** 2)
    return bmi

def kategori_bmi (gender, bmi) :
    if gender == 1 :
        ahh = 73
        if bmi < 17 :
            ahh -= 4
            ket = 'Kurus'
        elif bmi >= 17 and bmi <= 24.9 :
            ahh -= 0
            ket = 'Normal'
        elif bmi >= 25 and bmi <= 29.9 :
            ahh -= -4
            ket = 'Kegemukan'
        elif bmi >= 30 :
            ahh -= -8
            ket = 'Obesitas'
        return ahh, ket
    elif gender == 2 :
        ahh = 78
        if bmi < 17 :
            ahh -= 4
            ket = 'Kurus'
        elif bmi >= 17 and bmi <= 24.9 :
            ahh -= 0
            ket = 'Normal'
        elif bmi >= 25 and bmi <= 29.9 :
            ahh -= -4
            ket = 'Kegemukan'
        elif bmi >= 30 :
            ahh -= -8
            ket = 'Obesitas'
        return ahh, ket
    else :
        return 'Error'
    
def kategori_pola_makan (pola_makan, ahh) :
    if pola_makan == 1 :
        ahh = ahh + 14
    else :
        ahh = ahh
    return ahh

def kategori_perokok (perokok, ahh) :
    if perokok == 1 :
        ahh = ahh - 7
    else :
        ahh = ahh
    return ahh

def kategori_pengonsumsi_alkohol (alkohol, ahh) :
    if alkohol == 1 :
        ahh = ahh - 2
    elif alkohol == 2 :
        ahh = ahh - 4
    elif alkohol == 3 :
        ahh = ahh - 6
    elif alkohol == 4 :
        ahh = ahh
    return ahh

def kategori_pengguna_obat_terlarang (obat_terlarang, ahh) :
    if obat_terlarang == 1 :
        ahh = ahh - 5
    elif obat_terlarang == 2 :
        ahh = ahh - 20
    elif obat_terlarang == 3 :
        ahh = ahh 
    return ahh
