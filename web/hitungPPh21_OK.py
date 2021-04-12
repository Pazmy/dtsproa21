def hitung(nama, status, jumlah_tanggungan, gaji):
    nama = nama
    Status = status
    Jumlah_Tanggungan = int(jumlah_tanggungan)
    Gaji = int(gaji)

    print("Keterangan Tambahan (Asumsi) sbb:\n- Iuran Pensiun dibayar sendiri sebesar 1% dari Gaji \n- Iuran Jaminan Hari Tua dibayar sendiri 2% dari gaji, dibayar perusahaan 3,7% dari Gaji\n- Premi Jaminan Kecelakaan Kerja dibayar pemberi kerja sebesar 1% dari Gaji\n- Premi Jaminan Kematian dibayar pemberi kerja sebesar 0,3% dari gaji")

    Iuran_pensiun_dbs = 1/100 * Gaji
    Iuran_JHT_dtp = 3.7/100 * Gaji
    Iuran_JHT_dbs = 2/100 * Gaji
    Premi_Jaminan_Kematian = 0.3/100 * Gaji
    Premi_JKK = 1/100 * Gaji
    Biaya_Jabatan = 5/100 * Gaji
    Ph_Bruto = Gaji + Premi_JKK + Premi_Jaminan_Kematian
    Ph_Netto_Sebulan = Ph_Bruto - (Biaya_Jabatan +  Iuran_pensiun_dbs + Iuran_JHT_dbs)
    Ph_Netto_Setahun = Ph_Netto_Sebulan * 12

    print()
    print("NAMA : ", nama)
    print()
    print("Gaji : ", Gaji)
    print("Premi Jaminan Kecelakaan Kerja : ", int(Premi_JKK))
    print("Premi Jaminan Kematian : ", int(Premi_Jaminan_Kematian))
    print("PENGHASILAN BRUTO : ", int(Ph_Bruto))
    print()
    print("Biaya Jabatan : ", int(Biaya_Jabatan))
    print("Iuran Pensiun : ", int(Iuran_pensiun_dbs))
    print("Iuran Jaminan Hari Tua : ", int(Iuran_JHT_dbs))
    print("PENGURANGAN : ", int(Biaya_Jabatan + Iuran_pensiun_dbs + Iuran_JHT_dbs))
    print()
    print("PENGHASILAN NETTO SEBULAN = ", int(Ph_Netto_Sebulan))
    print()
    print("PENGHASILAN NETTO SETAHUN = ", int(Ph_Netto_Setahun))
    print()

    S_PTKP = Status + str(Jumlah_Tanggungan)
    S_PTKP = S_PTKP.upper()
    #print("Status PTKP = ", S_PTKP)
    PTKP = 0

    if S_PTKP == "TK0":
        PTKP = 54000000
    elif S_PTKP == "TK1":
        PTKP = 58500000
    elif S_PTKP == "TK2":
        PTKP = 63000000
    elif S_PTKP == "TK3":
        PTKP = 67500000
    elif S_PTKP == "K0":
        PTKP = 58500000
    elif S_PTKP == "K1":
        PTKP = 63000000
    elif S_PTKP == "K2":
        PTKP = 67500000
    elif S_PTKP == "K3":
        PTKP = 72000000
    else:
        PTKP = "Cek kembali pengisian status; jml tanggungan maks 3"

    print("PTKP SETAHUN = ", PTKP)

    Ph_Kena_Pajak_Setahun = int(round(Ph_Netto_Setahun-PTKP, -3))
    if Ph_Kena_Pajak_Setahun<=0:
        Ph_Kena_Pajak_Setahun=0

    print("Penghasilan Kena Pajak Setahun = ", Ph_Kena_Pajak_Setahun)

    PPh21_Setahun = 0

    if Ph_Kena_Pajak_Setahun <= 50000000:
        PPh21_Setahun = 5/100 * Ph_Kena_Pajak_Setahun
    elif Ph_Kena_Pajak_Setahun > 50000000 and Ph_Kena_Pajak_Setahun <= 250000000:
        PPh21_Setahun = 2500000 + (Ph_Kena_Pajak_Setahun - 50000000) * 15/100
    elif Ph_Kena_Pajak_Setahun > 250000000 and Ph_Kena_Pajak_Setahun <= 500000000:
        PPh21_Setahun = 32500000 + (Ph_Kena_Pajak_Setahun - 250000000) * 25/100
    else:
        PPh21_Setahun = 950000000 + (Ph_Kena_Pajak_Setahun - 500000000) * 30/100

    print("PPh 21 Terutang Setahun : ", int(PPh21_Setahun))

    PPh21_Sebulan = int(1/12 * PPh21_Setahun)

    print("PPh 21 Terutang Sebulan : ", PPh21_Sebulan)

    return {
        "Nama": nama,
        "Gaji": Gaji,
        "Premi jaminan kecelakaan kerja": Premi_JKK,
        "premi jaminan kematian": Premi_Jaminan_Kematian,
        "Penghasilan bruto": Ph_Bruto,
        "Biaya jabatan": Biaya_Jabatan,
        "Iuran pensiun": Iuran_pensiun_dbs,
        "Iuran jaminan hari tua": Iuran_JHT_dbs,
        "Pengurangan": Biaya_Jabatan + Iuran_pensiun_dbs + Iuran_JHT_dbs,
        "Penghasilan netto sebulan": Ph_Netto_Sebulan,
        "Penghasilan netto setahun": Ph_Netto_Setahun,
        "PTKP setahun": PTKP,
        "Penghasilan kena pajak setahun": Ph_Kena_Pajak_Setahun,
        "PPh21 terutang setahun": PPh21_Setahun,
        "PPh21 terutang sebulan": PPh21_Sebulan,
    }
