### Muhammad Abyan Nauli Harahap
### CAPSTONE 1 - Data Pasien RS

### List pasien dengan data awal
patients = [
    {'ID': 'P1', 'Nama': 'Andre', 'Usia': 26, 'Jenis kelamin': 'Laki-Laki', 'Gol. darah': 'A', 'Diagnosis': 'Flu', 'Ruangan': 101 },
    {'ID': 'P2', 'Nama': 'Budi', 'Usia': 31, 'Jenis kelamin': 'Laki-Laki', 'Gol. darah': 'B', 'Diagnosis': 'Demam Berdarah', 'Ruangan': 101},
    {'ID': 'P3', 'Nama': 'Cici', 'Usia': 40, 'Jenis kelamin': 'Perempuan', 'Gol. darah': 'AB', 'Diagnosis': 'Batuk Berdahak','Ruangan': 102},
] 

### CREATE pasien baru
def add_patient():
    while True:
        while True:
            patient_id = input('Masukkan ID pasien: ').strip()

            # Cek apakah ID sudah ada
            id_lama = False ## asumsi id tidak ada
            for patient in patients:
                if patient["ID"] == patient_id:
                    id_lama = True ## diubah menjadi True
                    break
            if id_lama:
                print('ID sudah digunakan! Masukkan ID lain.')
            else:
                break

        nama = input('Masukkan Nama Pasien: ').strip()
        usia = input('Masukkan Usia Pasien: ').strip()
        jenis_kelamin = input('Masukkan Jenis Kelamin Pasien: ').strip()
        gol_dar = input('Masukkan Golongan Darah Pasien: ').strip()
        diagnosis = input('Masukkan Diagnosis Pasien: ').strip()
        ruangan = input('Masukkan Ruangan Pasien: ').strip()
        
        ## show new patient details
        print('\n Konfirmasi data pasien:')
        print(f'ID: {patient_id}')
        print(f'Nama: {nama}')
        print(f'Usia: {usia}')
        print(f'Jenis kelamin: {jenis_kelamin}')
        print(f'Gol. darah: {gol_dar}')
        print(f'Diagnosis: {diagnosis}')
        print(f'Ruangan: {ruangan}')

        konfirmasi_tambah = input('Apa yakin data pasien sudah benar? (y/n): ')

        if konfirmasi_tambah == 'y':
            patient = {
                'ID': patient_id,
                'Nama': nama,
                'Usia': usia,
                'Jenis kelamin': jenis_kelamin,
                'Gol. darah': gol_dar,
                'Diagnosis': diagnosis,
                'Ruangan': ruangan,
            }
            patients.append(patient)  # Tambahkan pasien ke dalam list
            print("Pasien berhasil ditambahkan!\n")
        else:
            print('Tambah pasien dibatalkan.')

        ## tambah data pasien lain
        another_add = input('Ingin tambah data pasien lain? (y/n): ')
        if another_add == 'n':
            print('Kembali ke menu utama\n')
            break

### READ data semua pasien
def show_patient():
    while True:
        print('\n === Lihat Data Pasien ===')
        print('1. Lihat semua pasien')
        print('2. Lihat ID pasien')
        print('3. Kembali ke Menu Utama')

        show_menu = input('Pilih opsi menu [1-3]: ')

        if show_menu == '1':
            if not patients:  # Perbaikan dari 'if not patients():'
                print('Data pasien tidak ditemukan.\n')
            else:
                print("\n=== Data Pasien ===")
                for patient in patients:
                    print(f'''ID: {patient['ID']}, Nama: {patient['Nama']}, Usia: {patient['Usia']}, 
                    Jenis kelamin: {patient['Jenis kelamin']}, Gol. darah: {patient['Gol. darah']}, 
                    Diagnosis: {patient['Diagnosis']}, Ruangan: {patient['Ruangan']}''')
                print()

        elif show_menu == '2':
            patient_id = input('Masukkan ID pasien: ').strip()
            found = False #asumsi pasien tidak dalam list
            
            for patient in patients:
                if patient['ID'] == patient_id:
                    print('\n === Data Pasien ===')
                    print(f'''ID: {patient['ID']}, Nama: {patient['Nama']}, Usia: {patient['Usia']}, 
                    Jenis kelamin: {patient['Jenis kelamin']}, Gol. darah: {patient['Gol. darah']}, 
                    Diagnosis: {patient['Diagnosis']}, Ruangan: {patient['Ruangan']}''')
                    found = True # found diset menjadi True
                    break # keluar loop
            
            if not found:
                print('ID pasien tidak ditemukan')

        elif show_menu == '3':
            break

        else:
            print('Pilihan tidak valid, coba lagi.')

        another_show = input('Apa ingin melihat data pasien yang lain? (y/n): ').strip().lower()
        if another_show == 'n':
            print('Kembali ke menu utama')
            break
        elif another_show == 'y':
            continue

### UPDATE data pasien
def update_patient():
    while True:
        patient_id = input('Masukkan ID pasien yang ingin di-update: ')

        for patient in patients:
            if patient['ID'] == patient_id:
                print(f'''Data pasien ditemukan
                == {patient['ID']}: {patient['Nama']} ==''')
                                
                while True:
                    print('Pilih data yang ingin di-update.')
                    print('1. Nama')
                    print('2. Usia')
                    print('3. Jenis kelamin')
                    print('4. Gol. darah')
                    print('5. Diagnosis')
                    print('6. Ruangan')
                    print('7. Kembali ke menu utama')

                    update_menu = input('Masukkan pilihan [1-7]: ')

                    if update_menu in ['1','2','3','4','5','6']:
                        if update_menu == '1':
                            value_update = input('Masukkan nama baru: ')
                            column_update = 'Nama'            
                        elif update_menu == '2':
                            value_update = input('Masukkan usia baru: ')
                            column_update = 'Usia'                    
                        elif update_menu == '3':
                            value_update = input('Masukkan jenis kelamin baru: ')
                            column_update = 'Jenis kelamin'
                        elif update_menu == '4':
                            value_update = input('Masukkan golongan darah baru: ')
                            column_update = 'Gol. darah'
                        elif update_menu == '5':
                            value_update = input('Masukkan diagnosis baru: ')
                            column_update = 'Diagnosis'
                        elif update_menu == '6':
                            value_update = input('Masukkan ruangan baru: ')
                            column_update = 'Ruangan'
                        
                        confirm_update = input(f'Konfirmasi update "{column_update}" menjadi "{value_update}"? (y/n): ').strip().lower()
                        if confirm_update == 'y':
                            print(f'Update {column_update} data sudah berhasil!')
                            patient[column_update] = value_update
                        else:
                            print('Update dibatalkan.')

                        # update detail lain pasien sama
                        another_detail = input('Apa ingin mengupdate data lain? (y/n): ')
                        if another_detail == 'n':
                            break
                        elif another_detail == 'y':
                            continue
                    
                    elif update_menu == '7':
                        print('Update dibatalkan. Kembali ke menu utama.')
                        return
            
                    print('Data pasien telah diperbarui\n')
                    return
                
                # update pasien lain
                another_update = input('Ingin update pasien lain? (y/n): ')
                if another_update == 'y':
                    continue ## balik milih pasien
                else:
                    print('Kembali ke menu utama')
                    return ## back to main menu                

        print("Pasien dengan ID tersebut tidak ditemukan.\n")

### DELETE data pasien
def delete_patient():
    while True:
        patient_id = input('Masukkan ID pasien untuk menghapus pasien: ').strip()

        found = False ## tracking patient

        for patient in patients:
            if patient['ID'] == patient_id:
                found = True ## ada patient == True
                konfirmasi_delete = input('Konfirmasi delete data pasien? (y/n): ')
                
                if konfirmasi_delete == 'y':
                    patients.remove(patient)       
                    print('Data pasien berhasil dihapus!\n')
                else:
                    print('Hapus data pasien dibatalkan.')
                
                break ## exit loop

        if not found:
            print('ID Pasien tidak ditemukan. Coba lagi\n')
            continue

        another_delete = input('Apa ingin menghapus data pasien lain? (y/n): ')
            
        if another_delete == 'n':
            print('Kembali ke menu utama.')
            return
        elif another_delete == 'y':
            continue

### MENU INTERAKTIF DENGAN LOOP
def main_menu():
    while True:
        menu = input('''
            Selamat datang di Rumah Sakit 

            List Menu:
            1. Lihat Data Pasien
            2. Tambah Data Pasien
            3. Update Data Pasien
            4. Hapus Data Pasien
            5. Exit

            Silakan pilih menu [1-5]: ''')

        if menu == '1':
            show_patient()
        elif menu == '2':
            add_patient()
        elif menu == '3':
            update_patient()
        elif menu == '4':
            delete_patient()
        elif menu == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

### memunculkan menu utama
main_menu()