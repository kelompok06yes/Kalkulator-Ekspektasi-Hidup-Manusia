def nama () :
    nama = str(input('Nama :'))
    return nama

def umur () :
    umur = int(input('Umur :'))
    return umur

def pil_pendidikan () :
    print ('1. Pelajar/Mahasiswa')
    print ('2. Lulusan Universitas')
    pendidikan = int(input('Pendidikan :'))
    if pendidikan == 1 :
        status = 'Pelajar/Mahasiswa'
    elif pendidikan == 2 :
        status = 'Lulusan Universitas'
    return pendidikan, status

def tinggi_badan () :
    tinggi_badan = int(input('Tinggi :'))
    return tinggi_badan

def berat_badan () :
    berat_badan = int(input('Berat :'))
    return berat_badan

def pil_gender () :
    print ('1. Laki-laki')
    print ('2. Perempuan')
    gender = int(input('Gender :'))
    if gender == 1 :
        status = 'Laki-laki'
    elif gender == 2 :
        status = 'Perempuan'
    return gender, status

def pil_pola_makan () :
    print ('1. Sehat')
    print ('2. Tidak Sehat')
    pola_makan = int(input('Pola makan :'))
    if pola_makan == 1 :
        status = 'Sehat'
    elif pola_makan == 2 :
        status = 'Tidak Sehat'
    return pola_makan, status

def pil_perokok () :
    print ('1. Ya')
    print ('2. Tidak')
    perokok = int(input('Perokok :'))
    if perokok == 1 :
        status = 'Ya'
    elif perokok == 2 :
        status = 'Tidak'
    return perokok, status

def pil_alkohol () :
    print ('1. Ringan')
    print ('2. Sedang')
    print ('3. Berat')
    print ('4. Tidak Pernah')
    alkohol = int(input('Alkohol :'))
    if alkohol == 1 :
        status = 'Ringan'
    elif alkohol == 2 :
        status = 'Sedang'
    elif alkohol == 3 :
        status = 'Berat'
    elif alkohol == 4 :
        status = 'Tidak Pernah'
    return alkohol, status

def pil_obat_terlarang () :
    print ('1. Ringan')
    print ('2. Berat')
    print ('3. Tidak Pernah')
    obat_terlarang = int(input('Obat terlarang :'))
    if obat_terlarang == 1 :
        status = 'Ringan'
    elif obat_terlarang == 2 :
        status = 'Berat'
    elif obat_terlarang == 3 :
        status = 'Tidak Pernah'
    return obat_terlarang, status
