import model

def izris_stanja(igra):
    mozna_stanja = ['', ' _|______ ', '  | \n _|______ ', '  | \n  | \n _|______ ', '  | \n  | \n  | \n _|______ ', '  | \n  | \n  | \n  | \n _|______ ', '  _____\n  | \n  | \n  | \n  | \n _|______ ', '  _____\n  |   |\n  | \n  | \n  | \n _|______ ', '  _____\n  |   |\n  |   o\n  | \n  | \n _|______ ', '  _____\n  |   |\n  |   o\n  |  /|\ \n  | \n _|______ ', '  _____\n  |   |\n  |   o\n  |  /|\ \n  |  / \ \n _|______ ']
    return mozna_stanja[igra.stevilo_napak()]


def izpis_igre(igra):
    print(izris_stanja(igra))
    return (
        "===============================================\n" + 
        "Število preostalih poskusov: {}\n".format(model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1) + 
        "Pravilni del gesla: {}\n".format(igra.pravilni_del_gesla()) +
        "Neuspeli poskusi: {}\n".format(igra.nepravilni_ugibi()) +
        "==============================================="
    )

def izpis_zmage(igra):
    print("Čestitam! Uganil si geslo {}".format(igra.geslo))
    print('Za novo igro vpiši 1!')
    zelja = input()
    if zelja:
        return pozeni_vmesnik()
    else:
        return 'Se vidimo prihodnjič!'

def izpis_poraza(igra):
    print("Porabil si vse poskuse. Geslo je {}".format(igra.geslo))
    print('Za novo igro vpiši 1!')
    zelja = input()
    if zelja:
        return pozeni_vmesnik()
    else:
        return 'Se vidimo prihodnjič!'


def zahtevaj_vnos():
    vnos = input('Črka: ')
    if vnos.isalpha():
        return vnos
    else:
        print('Ta vnos ni smiseln. Poskusite ponovno!\n ')
        return zahtevaj_vnos() 


def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break
