from tabulate import tabulate

Data = {
    'D.1710.JDS' : {'Nama' : 'Yamaha Nmax', 'Harga' : 24000000, 'DP' : '10% Dari harga motor', 'Bunga' : '5%/bulan', 'Tenor' : '24 bulan', 'warna' : 'Hitam'},
    'D.1223.AAZ' : {'Nama' : 'Honda Vario', 'Harga' : 17000000, 'DP' : '10% Dari harga motor', 'Bunga' : '5%/bulan', 'Tenor' : '24 bulan', 'warna' : 'Putih'},
    'D.3116.ZXE' : {'Nama' : 'Suzuki satria', 'Harga' : 14000000, 'DP' : '10% Dari harga motor', 'Bunga' : '5%/bulan', 'Tenor' : '24 bulan', 'warna' : 'Merah'},
    'D.5508.UIJ' : {'Nama' : 'Kawasaki Ninja', 'Harga' : 36000000, 'DP' : '10% Dari harga motor', 'Bunga' : '5%/bulan', 'Tenor' : '24 bulan', 'warna' : 'Hijau'},
    'D.0023.TRM' : {'Nama' : 'Yamaha Mio', 'Harga' : 14000000, 'DP' : '10% Dari harga motor', 'Bunga' : '5%/bulan', 'Tenor' : '24 bulan', 'warna' : 'Biru'},
    'D.5081.TXH' : {'Nama' : 'Honda Beat', 'Harga' : 17000000, 'DP' : '10% Dari harga motor', 'Bunga' : '5%/bulan', 'Tenor' : '24 bulan', 'warna' : 'Silver'}

}

def display_motorcycles(brand=None):
    headers = ["Kode", "Nama", "Harga", "DP", "Bunga", "Tenor", "Warna"]
    rows = []


    print(f"\nDaftar Motor {brand}:")
    for key, value in Data.items():
        if brand is None or brand in value['Nama']:
            print(f"{key.capitalize()}: {value['Nama']}")
            rows.append([key, value['Nama'], value['Harga'], value['DP'], value['Bunga'], value['Tenor'], value['warna']])

    print(tabulate(rows, headers=headers, tablefmt='pretty'))

def MenambahData_motor():
    while True:
        tabel_choice = input('Apakah anda ingin Memasukkan data (ya/tidak) ').strip()

        if tabel_choice == 'ya':
            kode_motor = input("Masukkan kode motor baru (contoh: D.0117.JDS): ").strip()
            if kode_motor in Data:
                print("Kode motor sudah ada. Silakan gunakan kode yang berbeda.")
                continue
            display_motorcycles(brand=None)
            lanjut_choice = input('lanjutkan tambah data motor? (ya/tidak)')
            if lanjut_choice == 'ya': 

                nama = input("Masukkan nama motor(Contoh: Suzuki satria): ").strip()
                harga = input("Masukkan harga motor: ").strip()
                dp = input("Masukkan DP(Minimal 10% Dari harga motor): ").strip()
                bunga = input("Masukkan bunga: ").strip()
                tenor = input("Masukkan tenor: ").strip()
                warna = input("Masukkan warna: ").strip()

                # Menambahkan data motor baru
                Data[kode_motor] = {
                    'Nama': nama,
                    'Harga': int(harga) if harga.isdigit() else 0,
                    'DP': dp,
                    'Bunga': bunga,
                    'Tenor': tenor,
                    'warna': warna
                }

                save_choice = input("Apakah Anda ingin menyimpan data motor ini? (y/n): ").strip().lower()
                if save_choice == 'y':
                    print("Data motor berhasil disimpan.")
                    display_motorcycles(brand=None)
                    another_choice = input("Kembali ke menu? (1: Ya): ").strip()
                    if another_choice != '1':
                        return
            
                else:
                    print("Data motor tidak disimpan.")

            else:
                print("kembali ke menu.")
                return

        elif tabel_choice == 'tidak':
                exit_choice = input("Apakah Anda ingin kembali ke program? (ya/tidak): ").strip().lower()
                if exit_choice == 'ya':
                    continue
                else:
                    print()
                    break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
         
        
def ubahData_motor():
    while True:
        tabel_choice = input('Apakah anda ingin Mengubah data (ya/tidak) ').strip()

        if tabel_choice == 'ya':             
                kode_motor = input("Masukkan kode motor yang ingin diubah (contoh: D.1710.JDS):")
                if kode_motor not in Data:
                    print("Kode motor Tidak ada. Silakan gunakan kode motor yang ada.")
                    continue
                display_motorcycles(brand=None)
                lanjut_choice = input('lanjutkan ubah data motor? (ya/tidak)')
                if lanjut_choice == 'ya':   

                # Display current data
                    current_data = Data[kode_motor]
                    headers = ["Kode", "Nama", "Harga", "DP", "Bunga", "Tenor", "Warna"]
                    rows = [[kode_motor, current_data['Nama'], current_data['Harga'], current_data['DP'], 
                    current_data['Bunga'], current_data['Tenor'], current_data['warna']]]
            
                    print("Data saat ini:")
                    print(tabulate(rows, headers=headers, tablefmt='pretty'))

                # Input new values
                    nama = input(f"Masukkan nama baru (tekan Enter untuk tidak mengubah, saat ini: {current_data['Nama']}): ").strip()
                    harga = input(f"Masukkan harga baru (tekan Enter untuk tidak mengubah, saat ini: {current_data['Harga']}): ").strip()
                    dp = input(f"Masukkan DP baru (tekan Enter untuk tidak mengubah, saat ini: {current_data['DP']}): ").strip()
                    bunga = input(f"Masukkan bunga baru (tekan Enter untuk tidak mengubah, saat ini: {current_data['Bunga']}): ").strip()
                    tenor = input(f"Masukkan tenor baru (tekan Enter untuk tidak mengubah, saat ini: {current_data['Tenor']}): ").strip()
                    warna = input(f"Masukkan warna baru (tekan Enter untuk tidak mengubah, saat ini: {current_data['warna']}): ").strip()

                # Update values only if new data is provided
                    if nama:
                        current_data['Nama'] = nama
                    if harga.isdigit():
                        current_data['Harga'] = int(harga)
                    if dp:
                        current_data['DP'] = dp
                    if bunga:
                        current_data['Bunga'] = bunga
                    if tenor:
                        current_data['Tenor'] = tenor
                    if warna:
                        current_data['warna'] = warna

                    change_choice = input("Ubah data motor? (y/n): ").strip().lower()
                    if change_choice == 'y':
                        print("Data motor berhasil diubah.")
                        display_motorcycles(brand=None)
                    rows = [[kode_motor, current_data['Nama'], current_data['Harga'], current_data['DP'], 
                            current_data['Bunga'], current_data['Tenor'], current_data['warna']]]
                    print("Data baru:")
                    print(tabulate(rows, headers=headers, tablefmt='pretty'))
                    return
                    
                else:
                    print("kembali ke menu.")
                    return

        elif tabel_choice == 'tidak':
                exit_choice = input("Apakah Anda ingin kembali ke program? (ya/tidak): ").strip().lower()
                if exit_choice == 'ya':
                    continue
                else:
                    print()
                    break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def hapusData_motor():
    while True:
        tabel_choice = input('Apakah Anda ingin menghapus data motor? (ya/tidak) ').strip().lower()

        if tabel_choice == 'ya':
                kode_motor = input("Masukkan kode motor yang ingin dihapus (contoh: D.1710.JDS): ").strip()
                if kode_motor not in Data:
                    print("Kode motor tidak ada. Silakan gunakan kode motor yang ada.")
                    continue
                display_motorcycles()
                lanjut_choice = input('Lanjutkan hapus data motor? (ya/tidak) ').strip().lower()
                if lanjut_choice == 'ya':
                    konfirmasi = input(f"Anda yakin ingin menghapus {Data[kode_motor]['Nama']}? (ya/tidak): ").strip().lower()
                    if konfirmasi == 'ya':
                        del Data[kode_motor]
                        print(f"Data motor {kode_motor} berhasil dihapus.")
                        display_motorcycles(brand=None)
                        return
                    else:
                        print("Penghapusan dibatalkan.")

        elif tabel_choice == 'tidak':
                exit_choice = input("Apakah Anda ingin kembali ke program? (ya/tidak): ").strip().lower()
                if exit_choice == 'ya':
                    continue
                else:
                    print()
                    break
        else:            
            print("Kembali ke menu dealer motor.")
            return

def calculate_monthly_payment(harga, dp, tenor, bunga):
    total_pembiayaan = harga - dp
    monthly_payment = (total_pembiayaan / tenor) + (total_pembiayaan * bunga)
    return monthly_payment


def buy_motor():
    while True:
        motor_to_buy = input("Apakah Anda ingin memulai kredit motor? (ya/tidak): ").strip().lower()
        if motor_to_buy == 'ya':
            display_motorcycles()
            kode_motor = input("Masukkan kode motor yang ingin Anda mulai kredit (contoh: D.1710.JDS): ").strip()
            if kode_motor not in Data:
                print("Kode motor tidak ada. Silakan gunakan kode motor yang ada.")
                continue

            motor_info = Data[kode_motor]
            harga = motor_info['Harga']
            tenor = int(motor_info['Tenor'].split()[0])
            bunga = float(motor_info['Bunga'].replace('%/bulan', '').replace(' ', '')) / 100  # Ubah persentase menjadi desimal

            lanjut_choice = input('Lanjutkan pembayaran DP motor? (ya/tidak): ').strip().lower()
            if lanjut_choice == 'ya':
                dp = float(input(f"Masukkan DP (minimal Rp {harga * 0.10:.2f}): "))
                if dp >= harga * 0.10:
                    monthly_payment = calculate_monthly_payment(harga, dp, tenor, bunga)
                    print(f"\nAnda memilih: {motor_info['Nama']}")
                    print(f"Pembayaran per bulan: Rp {monthly_payment:.2f}")
                    print(f"\ndengan Tenor: {motor_info['Tenor']}")
                    lanjut = input("Apakah Anda ingin melanjutkan? (y/n): ").strip().lower()
                    if lanjut == 'y':
                        print("Terima kasih sudah melakukan kredit motor di tempat kami.")
                        print("Motor Anda sedang di proses")
                        return
                    else:
                        print("Pengajuan kredit dibatalkan.")
                else:
                    print(f"DP tidak boleh kurang dari 10% dari harga motor. Silakan coba lagi.")
            else:
                print("Kembali ke menu utama.")
                return

        elif motor_to_buy == 'tidak':
            print("Terima kasih. Kembali ke menu utama.")
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#         # HOME PAGE
def main_menu():
        print(f'''
        =======DEALER MOTOR=======      
        1. DATA MOTOR-MOTOR
        2. MENAMBAHKAN DATA MOTOR
        3. MENGUBAH DATA MOTOR
        4. MENGHAPUS DATA MOTOR
        5. KREDIT MOTOR
        6. EXIT
        ''')
        input_home = input('Silahkan Pilih [1-6] : ').strip()
        return input_home


while True:
    input_home=main_menu()


    if input_home == '1':
        display_motorcycles()
        print('1. Yamaha\n2. Honda\n3. Suzuki/Kawasaki')
        brand_choice = input('Silahkan Pilih [1-3]: ').strip()

        if brand_choice == '1':
            display_motorcycles('Yamaha')
        elif brand_choice == '2':
            display_motorcycles('Honda')
        elif brand_choice == '3':
            display_motorcycles('Suzuki')  # Suzuki and Kawasaki are combined 
            display_motorcycles('Kawasaki')
        else:
            print("Pilihan tidak valid.")

        selected_code = input("Silahkan masukkan kode motor yang mau dipilih: ").strip()
        display_motorcycles(selected_code)

        continue_choice = input("Ingin melanjutkan ke menu? (y/n): ").strip().lower()
        if continue_choice != 'y':
            break

            # menambah data motor
    elif input_home == '2':
        MenambahData_motor()

            #mengubah data motor
    elif input_home == '3':
            #tampilan 3
        ubahData_motor()

            #menghapus data motor
    elif input_home == '4':
            #tampilan 4
        hapusData_motor()

            #kredit motor
    elif input_home == '5':
            #tampilan 5
        buy_motor()
#             # EXIT program
    else:
        input_home == '6'
        print()
        break


main_menu()