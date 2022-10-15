import ZadanieDomowe

print("KALKULATOR \n\n" +
      "1. v szeciana \n" +
      "2. v ostroslupa czworokatnego \n" +
      "3. v graniastoslupa trojkatnego" + 
      "4. v walca \n" +
      "5. v kuli \n" +
      "6. v stozka" + 
      "7. v piramidy \n" +
      "8. v torusa \n" +
      "9. v kuli odjac v torusa \n" + 
      "10. v szesciana odjac v kuli \n" +
      "11. v szesciana dodac v kuli" + 
      "12. v szescian_dodac_v_stozek \n" +
      "13. v kuli dodac v walca \n" +
      "14. v piramidy_odjac_v_szescianu \n" +
      "15. v cztery_razy_v_stozka \n" +
      "16. v walec_dodac_v_stozka_odjac_v_kuli \n" +
      "17. v walec_odjac_v_kuli \n" + 
      "18. v dwa_razy_v_szesciana_dodac_v_graniastoslupa_trojkatnego \n \n" )

while True:
    inp = int(input("wybierz co chcesz zrobic :  "))

    if inp == 1:
        print(ZadanieDomowe.v_szescian())
    elif inp == 2:
        print(ZadanieDomowe.v_ostroslup_czworokatny())
    elif inp == 3:
        print(ZadanieDomowe.v_graniastoslup_trojkatny())
    elif inp == 4:
         r = float(input("podaj r: "))
         h = float(input("podaj h: "))
         print(ZadanieDomowe.v_walec(r, h))
    elif inp == 5:
        r = float(input("podaj r: "))
        print(ZadanieDomowe.v_kuli(r))
    elif inp == 6:
        r = float(input("podaj r: "))
        h = float(input("podaj h: "))
        print(ZadanieDomowe.v_stozek(r, h))
    elif inp == 7:
        a = float(input("podaj a: "))
        h = float(input("podaj h: "))
        print(ZadanieDomowe.v_piramidy(a, h))
    elif inp == 8:
        r = float(input("podaj r: "))
        R = float(input("podaj R: "))
        print(ZadanieDomowe.v_torus(r, R))
    elif inp == 9:
        r = float(input("podaj r: "))
        R = float(input("podaj R: "))
        print(ZadanieDomowe.v_kuli_odjac_v_torusa(r, R))
    elif inp == 10:
        r = float(input("podaj r: "))
        print(ZadanieDomowe.v_szescian_odjac_v_kuli(r))
    elif inp == 11:
        r = float(input("podaj r: "))
        ZadanieDomowe.v_szesciana_dodac_v_kuli(r)
    elif inp == 12:
        r = float(input("podaj r: "))
        h = float(input("podaj h: "))
        ZadanieDomowe.v_szescian_dodac_v_stozek(r, h)
    elif inp == 13:
        r = float(input("podaj r: "))
        h = float(input("podaj h: "))
        ZadanieDomowe.v_kuli_dodac_v_walca(r, h)
    elif inp == 14:
        print(ZadanieDomowe.v_piramidy_odjac_v_szescianu())
    elif inp == 15:
        print(ZadanieDomowe.cztery_razy_v_stozka())
    elif inp == 16:
        ZadanieDomowe.v_walec_dodac_v_stozka_odjac_v_kuli()
    elif inp == 17:
        r = float(input("podaj r: "))
        h = float(input("podaj h: "))
        ZadanieDomowe.v_walec_odjac_v_kuli(r, h)
    elif inp == 18:
        ZadanieDomowe.dwa_razy_v_szesciana_dodac_v_graniastoslupa_trojkatnego()
    else:
        print("podales zla liczbe sprobuj ponownie! ")