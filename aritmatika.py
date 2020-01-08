for i in range(10) :
    print ('ini adalah operasi aritmatika 2 bilangan')
    enter = input('Tekan Enter untuk melanjutkan')
    nama = input('Masukkan nama anda agar sistem akrab dengan anda: ')
    print ('Hai ',nama,',',' Apa kabar hari ini?',sep='')
    print ('Saya doakan ', nama,' selalu dalam keadaan baik-baik saja', sep='')
    print ('Pilihlah jenis perhitungan yang anda inginkan')
    print ('1. Penambahan')
    print ('2. Pengurangan')
    print ('3. Perkalian')
    print ('4. Pembagian')
    opt = eval(input('Ketik 1 untuk operasi penambahan, ketik 2 untuk operasi pengurangan, ketik 3 untuk operasi perkalian atau ketik 4 untuk operasi pembagian: '))

    if opt == 1:
        print ('Ini adalah operasi penambahan')
        pertama = eval(input('Masukkan angka pertama: '))
        kedua = eval(input('Masukkan angka kedua: '))
        hasiltambah = pertama+kedua
        print ('Maka hasil penambahan ',pertama,'+',kedua,' adalah = ',hasiltambah, sep='')
    if opt == 2:
        print ('Ini adalah operasi pengurangan')
        pertama = eval(input('Masukkan angka pertama: '))
        kedua = eval(input('Masukkan angka kedua: '))
        hasilkurang = pertama-kedua
        print ('Maka hasil pengurangan ',pertama,'-',kedua,' adalah = ',hasilkurang, sep='')
    if opt == 3:
        print ('Ini adalah operasi perkalian')
        pertama = eval(input('Masukkan angka pertama: '))
        kedua = eval(input('Masukkan angka kedua: '))
        hasilkali = pertama*kedua
        print ('Maka hasil perkalian ',pertama,'x',kedua,' adalah = ',hasilkali, sep='')
    if opt == 4:
        print ('Ini adalah operasi pembagian')
        pertama = eval(input('Masukkan angka pertama: '))
        kedua = eval(input('Masukkan angka kedua: '))
        hasilbagi = pertama/kedua
        print ('Maka hasil pembagian ',pertama,':',kedua,' adalah = ',hasilbagi, sep='')
print('Perhitungan selesai.')
