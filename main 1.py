nama = 'nadzif muaffi'
program = 'Tegangan Listrik'

print(f'program {program} oleh {nama}')

def hitung_tegangan(kuat_arus, hambatan):
    tegangan = kuat_arus * hambatan
    print(f'tegangan = {tegangan} V')

tegangan = hitung_tegangan(5, 1000)
tegangan = hitung_tegangan(12, 100)
