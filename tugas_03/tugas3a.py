def HitungJarak():
    """
    HitungJarak
    Program menerima input berupa kecepatan (m/s) dan waktu (s), 
    kemudian menampilkan ke layar output berupa jarak yang ditempuh.

    KAMUS
    kecepatan: Kecepatan (float)
    waktu: Waktu (float)
    jarak_tempuh: Jarak tempuh (kecepatan dikali waktu) (float)
    """
    kecepatan = float(input("Masukkan kecepatan (m/s): "))
    waktu = float(input("Masukkan waktu (s): "))

    jarak_tempuh = kecepatan * waktu
    print("Jarak yang ditempuh sejauh", jarak_tempuh)


def KelilingLingkaran():
    """
    KelilingLingkaran
    Program menerima input berupa jari-jari lingkaran, 
    kemudian menampilkan ke layar output berupa keliling lingkaran.

    KAMUS
    jari_jari: Jari-jari lingkaran (float)
    keliling_lingkaran: Keliling lingkaran (float)
    """
    jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))

    keliling_lingkaran = 2 * 3.14 * jari_jari
    print(keliling_lingkaran)


def LuasSegitiga():
    """
    LuasSegitiga
    Program akan menghitung luas segitiga setelah diberikan input alas dan tinggi segitiga

    KAMUS
    alas: ALas segitiga (float)
    tinggi: Tinggi segitiga (float)
    luas_segitiga: Luas segitiga (float)
    """
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan panjang tinggi segitiga: "))

    luas_segitiga = alas * tinggi / 2
    print(luas_segitiga)


def TinggiRataRata():
    """
    TinggiRataRata
    Program akan menghitung rata-rata dari 5 data yang diinputkan

    KAMUS
    total_tinggi: Total tinggi dari kelima data yang dimasukkan (float)
    tinggi_rata_rata: Rata-rata tinggi dari kelima data (float)
    """
    total_tinggi = .0
    for i in range(1, 6):
        total_tinggi += float(input(f"Masukkan tinggi ke-{i}: "))

    tinggi_rata_rata = total_tinggi / 5
    print("Tinggi rata-rata adalah: ", tinggi_rata_rata)


def TokoKelereng():
    """
    TokoKelereng
    Program akan menghitung berapa harga total yang harus dibayar dari pembelian kelereng.
    Terdapat 3 warna kelereng yang dapat dibeli (merah: 10 sen, hijau: 15 sen, hitam: 20 sen)

    KAMUS
    merah_dibeli: Jumlah kelereng merah yang ingin dibeli (int)
    hijau_dibeli: Jumlah kelereng hijau yang ingin dibeli (int)
    hitam_dibeli: Jumlah kelereng hitam yang ingin dibeli (int)
    total_harga: Total harga dari seluruh kelereng (int)
    """
    merah_dibeli = int(input("Berapa kelereng merah yang ingin dibeli? "))
    hijau_dibeli = int(input("Berapa kelereng hijau yang ingin dibeli? "))
    hitam_dibeli = int(input("Berapa kelereng hitam yang ingin dibeli? "))

    total_harga = 10 * merah_dibeli + 15 * hijau_dibeli + 20 * hitam_dibeli
    print(f"Total harga yang harus dibayarkan sebesar: {total_harga} sen")


if __name__ == "__main__":
    pilihan_program = """
    1. HitungJarak
    2. KelilingLingkaran
    3. LuasSegitiga
    4. TinggiRataRata
    5. TokoKelereng

    Pilih program yang ingin digunakan (masukkan angka saja): """
    pilihan = int(input(pilihan_program))

    match pilihan:
        case 1:
            HitungJarak()
        case 2:
            KelilingLingkaran()
        case 3:
            LuasSegitiga()
        case 4:
            TinggiRataRata()
        case 5:
            TokoKelereng()
        case _:
            print("Maaf masukkan yang diberikan tidak sesuai")
