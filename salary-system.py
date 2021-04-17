toplam_kisi_sayisi = 0
brut_maas = 0
es_icin_aile_odenegi = 0
altidan_buyuk = 0
cocuk_icin_odenecek_toplam_tutar = 0
aylik_brut_toplam = 0
engel_muafi_yok = 0
engel_orani = 0
toplam_odenen_net_ucret = 0
toplam_odenen_brut_ucret = 0
toplam_gelir_vergisi = 0
toplam_ikiyuzluk_banknot = 0
toplam_yuzluk_banknot = 0
toplam_ellilik_banknot = 0
toplam_yirmilik_banknot = 0
toplam_onluk_banknot = 0
toplam_beslik_banknot = 0
toplam_birlik = 0
toplam_ellilik = 0
toplam_yirmibes = 0
toplam_onkurus = 0
toplam_beskurus = 0
toplam_birkurus = 0
bin_bes_yuz_alti_ucret_alan = 0
yuzde_onbes_gelir_vergisi_kisi = 0
yuzde_yirmi_gelir_vergisi_kisi = 0
yuzde_yirmiyedi_gelir_vergisi_kisi = 0
yuzde_otuzbes_gelir_vergisi_kisi = 0
max_net_ucret = 0
max_net_tc = ''
max_net_ad_soyad = ''
max_net_gelir_vergisi = 0
max_net_ucret_brut_ucreti = 0
max_brut_ucret = 0
max_brut_tc = ''
max_brut_ad_soyad = ""
max_brut_gelir_vergisi = 0
max_brut_ucret_net_ucreti = 0
evli_sayisi = 0
bekar_sayisi = 0
esi_calisan = 0
toplam_cocuk_sayisi = 0
ucden_fazla_cocuk_sahibi_olan = 0
engelli_calisan_sayisi = 0
es_durumu = ''
while(True) :
    tc = int(input("Tc Kimlik Numarası = "))
    toplam_kisi_sayisi += 1
    ad_soyad = input("Ad Soyad = ")
    aylik_brut = float(input("Aylık Brüt Maas = "))
    while (True):  # Bu while döngüsü ile medeni haline girilen bilgilerin dogrulugu kontrol ediliyor ...
        medeni_hali = input("Medeni Hal = ")
        if (medeni_hali != 'e') and (medeni_hali != 'E') and (medeni_hali != 'b') and (medeni_hali != 'B'):
            print("Lütfen e/E/b/B olarak giriniz ... ")
        else:
            break
    if (medeni_hali == 'e') or (medeni_hali == 'E'):
        while (True):  # Bu while döngüsü ile es durumuna girilen bilgilerin dogrulugu kontrol ediliyor ...
            es_durumu = input("Eşiniz Çalışıyor Mu = ")
            if (es_durumu != 'e') and (es_durumu != 'E') and (es_durumu != 'h') and (es_durumu != 'H'):
                print("Lütfen e/E/h/H olarak giriniz ... ")
            else:
                break
        if (es_durumu == 'h') or (es_durumu == "H"):
            es_icin_aile_odenegi = 220
            brut_maas += 220  # Eşi çalışmadığı içi ek ödenek alınıyor ...
    if (medeni_hali == 'e') or (medeni_hali == 'E'):
        evli_sayisi += 1
    if (medeni_hali == 'b') or (medeni_hali == 'B'):
        bekar_sayisi += 1
    if (es_durumu == 'e') and (es_durumu == 'E'):
        esi_calisan += 1
    while (True):  # Bu while döngüsü ile cocuk sayisina girilen bilgilerin dogrulugu kontrol ediliyor .
        cocuk_sayisi = int(input("Bakmakla Yükümlü Oldugu Cocuk Sayisi = "))
        if (cocuk_sayisi < 0):
            print("Lütfen doğru sayı giriniz ... ")
        else:
            break
    if (cocuk_sayisi > 0):
        if (cocuk_sayisi != 0):
            toplam_cocuk_sayisi += cocuk_sayisi
            while (
            True):  # Bu while döngüsü ile altidan büyük cocuk sayısına girilen bilgilerin dogrulugu kontrol ediliyor .
                altidan_buyuk = int(input("Yaşı 6 dan Büyük Çocuk Sayisi = "))
                if (altidan_buyuk < 0):
                    print("Lütfen 0 ya da Daha Büyük Bir Sayı Giriniz ... ")
                else:
                    break
    if (cocuk_sayisi > 3):
        ucden_fazla_cocuk_sahibi_olan += 1
    altidan_kucuk = cocuk_sayisi - altidan_buyuk  # 6 yasından küçük cocukların sayısını bulabilmemiz için gerekli işlem ...
    cocuk_icin_odenecek_toplam_tutar = (altidan_buyuk * 45) + (altidan_kucuk * 25)
    aylik_brut_toplam = cocuk_icin_odenecek_toplam_tutar + es_icin_aile_odenegi + aylik_brut
    # Aylık vergi miktarını ve derecesini öğrenebilmemiz için for döngüsü kullanıyoruz .
    if (aylik_brut_toplam < 2000):
        gelir_vergisi = (aylik_brut_toplam * 15) / 100
        yuzde_onbes_gelir_vergisi_kisi += 1
    elif (aylik_brut_toplam < 5000):
        gelir_vergisi = (aylik_brut_toplam * 20) / 100
        yuzde_yirmi_gelir_vergisi_kisi += 1
    elif (aylik_brut_toplam < 10000):
        gelir_vergisi = ((aylik_brut_toplam * 27) / 100)
        yuzde_yirmiyedi_gelir_vergisi_kisi += 1
    else:
        gelir_vergisi = ((aylik_brut_toplam * 35) / 100)
        yuzde_otuzbes_gelir_vergisi_kisi += 1
    while (True):  # Bu while döngüsü ile engel durumuna girilen bilgilerin dogrulugu kontrol ediliyor .
        engel_durumu = input("Engel Durumu Var mı = ")
        if (engel_durumu != 'e') and (engel_durumu != 'E') and (engel_durumu != 'h') and (engel_durumu != 'H'):
            print("Lütfen e/E/h/H olarak giriniz ... ")
        else:
            break
    if (engel_durumu == 'e') or (engel_durumu == 'E'):
        while (True):  # Bu while döngüsü ile engel oranına girilen bilgilerin dogrulugu kontrol ediliyor ...
            engel_orani = int(input("Engel Oranı = "))
            if (engel_orani < 0) or (engel_orani > 100):
                print("1 ya da daha büyük , 100 ya da daha küçük bir sayı giriniz ... ")
            else:
                break
    # Engel durumunun kontrolüne göre engel oranını ve muaf olacak kısmı bulabilmek için koşullu işletme uygulanıyor ...
    if (engel_durumu == 'e') or (engel_durumu == 'E'):
        engelli_calisan_sayisi += 1
    if (engel_orani > 80):
        muaf_tutulan = 900
        engel_derecesi = 1
    elif (engel_orani > 60):
        muaf_tutulan = 470
        engel_derecesi = 2
    elif (engel_orani > 40):
        muaf_tutulan = 470
        engel_derecesi = 1
    else:
        muaf_tutulan = 0
    toplam_odenen_brut_ucret += aylik_brut_toplam
    aylik_brut_ucret_for_max = aylik_brut_toplam  # max değeri bulunabilmesi için ekstra değişkene atanıyor ve bekletiliyor ...
    print("Tc Kimlik Numarası = ", tc)
    print("Ad Soyad = ", ad_soyad)
    print("Aylık Brüt Ücreti = ", aylik_brut)
    print("Eş İçin Aile Yardımı Ödeneği = ", es_icin_aile_odenegi)
    print("Cocuk İçin Aile Yardımı Ödeneği = ", cocuk_icin_odenecek_toplam_tutar)
    print("Aylık Toplam Brüt Ücret = ", aylik_brut_toplam)
    print("Gelir Vergisi Kesintisi = ", gelir_vergisi)
    if (engel_orani > 40):  # Engel oranından dolayı muaflık söz konusu ise yazıdırılıyor değilse yazdırılmıyor ...
        print("Evet , yararlanıyor ve engel derecesi =  ", engel_derecesi)
    aylik_net_ücret = aylik_brut_toplam - gelir_vergisi + muaf_tutulan
    toplam_odenen_net_ucret += aylik_net_ücret
    # Aylık net ücreti belli tutarın altında olanların veri bilgilerini bu sekilde tutuyoruz ....
    if (aylik_net_ücret < 1500):
        bin_bes_yuz_alti_ucret_alan += 1
    toplam_gelir_vergisi += gelir_vergisi
    print("Aylık Net Ücret = ", aylik_net_ücret)
    aylik_net_ucret_for_max = aylik_net_ücret  # max değeri bulunabilmesi için ekstra değişkene atanıyor ve bekletiliyor ...
    kalan = aylik_net_ücret  # En az banknot verilebilmesi için farklı bir değişken atanıyor ve koşullu işletme uygulanıyor ...
    if (kalan > 200):
        iki_yuzluk = int(kalan / 200)
        print("İki Yüzlük Banknot Sayısı = ", iki_yuzluk)
        kalan = kalan % 200
        toplam_ikiyuzluk_banknot += iki_yuzluk
    if (kalan > 100):
        yuzluk = int(kalan / 100)
        print("Yüzlük Banknot Sayısı = ", yuzluk)
        kalan = kalan % 100
        toplam_yuzluk_banknot += yuzluk
    if (kalan > 50):
        ellilik = int(kalan / 50)
        print("Ellilik Banknot Sayısı = ", ellilik)
        kalan = kalan % 50
        toplam_ellilik_banknot += ellilik
    if (kalan > 20):
        yirmilik = int(kalan / 20)
        print("Yirmilik Banknot Sayısı = ", yirmilik)
        kalan = kalan % 20
        toplam_yirmilik_banknot += yirmilik
    if (kalan > 10):
        onluk = int(kalan / 10)
        print("Onluk Banknot Sayısı = ", onluk)
        kalan = kalan % 10
        toplam_onluk_banknot += onluk
    if (kalan > 5):
        beslik = int(kalan / 5)
        print("Beslik Banknot Sayısı = ", beslik)
        kalan = kalan % 5
        toplam_beslik_banknot += beslik
    if (kalan > 1):
        birlik = int(kalan / 1)
        print("Birlik Madeni Para Sayısı = ", birlik)
        kalan = kalan % 1
        toplam_birlik += birlik
    if (kalan > 0.5):
        madeni_ellilik = int(kalan / 0.5)
        print("50 Kurus Sayısı = ", madeni_ellilik)
        kalan = kalan % 0.5
        toplam_ellilik += madeni_ellilik
    if (kalan > 0.25):
        madeni_yirmibeskurus = int(kalan / 0.25)
        print("25 Kurus Sayısı = ", madeni_yirmibeskurus)
        kalan = kalan % 0.25
        toplam_yirmibes += madeni_yirmibeskurus
    if (kalan > 0.1):
        madeni_onkurus = int(kalan / 0.1)
        print("10 Kurus Sayısı = ", madeni_onkurus)
        kalan = kalan % 0.1
        toplam_onkurus += madeni_onkurus
    if (kalan > 0.05):
        madeni_beskurus = int(kalan / 0.05)
        print("5 Kurus Sayısı = ", madeni_beskurus)
        kalan = kalan % 0.05
        toplam_beskurus += madeni_beskurus
    if (kalan > 0.01):
        madeni_birkurus = int(kalan / 0.01)
        print("1 Kurus Sayısı = ", madeni_birkurus)
        toplam_birkurus += madeni_birkurus
    if (aylik_net_ucret_for_max > max_net_ucret):  # Net Ücreti En Cok Olan Kişiyi Bulma ve Atama İşlemleri
        max_net_ucret = aylik_net_ucret_for_max
        max_net_tc = tc
        max_net_ad_soyad = ad_soyad
        max_net_gelir_vergisi = gelir_vergisi
        max_net_ucret_brut_ucreti = aylik_brut_toplam
    if (aylik_brut_ucret_for_max > max_brut_ucret):  # Toplam Brüt Ücreti En Cok Olan Kişiyi Bulma ve Atama İşlemleri
        max_brut_ucret = aylik_brut_ucret_for_max
        max_brut_tc = tc
        max_brut_ad_soyad = ad_soyad
        max_brut_gelir_vergisi = gelir_vergisi
        max_brut_ucret_net_ucreti = aylik_net_ücret
    while(True) : # Baska kimse olup olmadıgı soruluyor buna göre program devam ediliyor ...
        baska_kimse = input("Baska Kayıt Var Mı = ")
        if (baska_kimse != 'e') and (baska_kimse != 'E') and (baska_kimse != 'h') and (baska_kimse != 'H'):
            print("Lütfen e/E/h/H olarak giriniz ... ")
        else :
            break
    if (baska_kimse != 'e') and (baska_kimse != 'H') :
        break
print("Toplam Ödenen Net Ücret = " , toplam_odenen_net_ucret )
print("Devlete Aktarılan Toplam Gelir Vergisi = " , toplam_gelir_vergisi)
print("Aylık Toplam Brut Ücretlerin Ortalaması = " , toplam_odenen_brut_ucret / toplam_kisi_sayisi)
print("Aylık Toplam Net Ücretlerin Ortalaması" , toplam_odenen_net_ucret / toplam_kisi_sayisi)
print("Bu Ay En Az Olması Gereken 200 lük Banknot = ", toplam_ikiyuzluk_banknot)
print("Bu Ay En Az Olması Gereken 100 lük Banknot = ", toplam_yuzluk_banknot)
print("Bu Ay En Az Olması Gereken  50 lik Banknot = ", toplam_ellilik_banknot)
print("Bu Ay En Az Olması Gereken  20 lik Banknot = ", toplam_yirmilik_banknot)
print("Bu Ay En Az Olması Gereken  10 luk Banknot = ", toplam_onluk_banknot)
print("Bu Ay En Az Olması Gereken   5 lik Banknot = ", toplam_beslik_banknot)
print("Bu Ay En Az Olması Gereken   1 lik Madeni Para = ", toplam_birlik)
print("Bu Ay En Az Olması Gereken 0.5 lik Madeni Para = ", toplam_ellilik)
print("Bu Ay En Az Olması Gereken 0.25 lik Madeni Para = ", toplam_yirmibes)
print("Bu Ay En Az Olması Gereken 0.1 lik Madeni Para = ", toplam_onkurus)
print("Bu Ay En Az Olması Gereken 0.05 lik Madeni Para = ", toplam_beskurus)
print("Bu Ay En Az Olması Gereken 0.01 lik Madeni Para = ", toplam_birkurus)
print("1500 Tl Altı Net Ücret Alan Sayısı = ",bin_bes_yuz_alti_ucret_alan)
print("Yüzde 15 Vergi Veren Kişi Sayısı Ve Yüzdesi = " , yuzde_onbes_gelir_vergisi_kisi , ((yuzde_onbes_gelir_vergisi_kisi * 100) / toplam_kisi_sayisi))
print("Yüzde 20 Vergi Veren Kişi Sayısı Ve Yüzdesi = " , yuzde_yirmi_gelir_vergisi_kisi , ((yuzde_yirmi_gelir_vergisi_kisi * 100) / toplam_kisi_sayisi))
print("Yüzde 27 Vergi Veren Kişi Sayısı Ve Yüzdesi = " , yuzde_yirmiyedi_gelir_vergisi_kisi,((yuzde_yirmiyedi_gelir_vergisi_kisi * 100) / toplam_kisi_sayisi))
print("Yüzde 35 Vergi Veren Kişi Sayısı Ve Yüzdesi = " , yuzde_otuzbes_gelir_vergisi_kisi , ((yuzde_otuzbes_gelir_vergisi_kisi * 100) / toplam_kisi_sayisi))
print("Net Ücreti En Yüksek Olan Çalışanın Tc , Ad Soyad , Aylık Toplam Brüt Ücreti ,"
      " Gelir Vergisi Kesintisi ve Aylık Toplam Brüt Ücreti = " , max_net_tc , max_net_ad_soyad , max_net_ucret_brut_ucreti , max_net_gelir_vergisi , aylik_net_ucret_for_max)
print("Brüt Ücreti En Yüksek Olan Çalışanın Tc , Ad Soyad , Aylık Toplam Brüt Ücreti , Gelir Vergisi Kesintisi ve Aylık Net Ücreti = " , max_brut_tc , max_brut_ad_soyad , max_brut_ucret_net_ucreti , max_brut_gelir_vergisi , aylik_brut_ucret_for_max)
print("Tüm Çalışanlar Arasında Evli ve Bekar Yüzdeleri = " , ( evli_sayisi * 100 ) / toplam_kisi_sayisi , (bekar_sayisi * 100) / toplam_kisi_sayisi )
if (evli_sayisi != 0 ) : # Evli sayısı 0 a eşit ise oran hesaplamasında hata olacağından dolayı kontrol ediliyor ...
    print("Evli Olan Çalışanların içinde, Eşleri de Çalışanların Yüzdesi = " , (esi_calisan * 100 ) / evli_sayisi )
print("Bakmakla Yükümlü Olunann Ortalama Çocuk Sayısı = ", toplam_cocuk_sayisi / toplam_kisi_sayisi)
print("Bakmakla Yükümlü Olunan Cocuk Sayısı 3 den Büyük Olanların Sayısı = ",ucden_fazla_cocuk_sahibi_olan)
print("Engelli Çalışanların Sayısı ve Yüzdesi = ", engelli_calisan_sayisi , (engelli_calisan_sayisi * 100 ) / toplam_kisi_sayisi)