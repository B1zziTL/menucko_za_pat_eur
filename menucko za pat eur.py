#otvorenie suboru
subor = open("objednane_jedla.txt","r")

#zadefinovanie premennych a zoznamu
pocet_jedal = 0
pocet_z = 0
pocet_c = 0
pocet_m = 0
pocet_o = 0
nedostatok = []

def pocty(): #funkcia na spocitanie jedal
    #zadefinovanie globalnych premennych
    global pocet_jedal, pocet_z, pocet_c, pocet_m, pocet_o

    for riadok in subor: #cyklus na prechadzanie riadkov v subore
        #pripocitanie jedal
        pocet_jedal += 1

        #rozdelenie riadku na slova
        riadocek = riadok.split()

        #podmienka na pripocitanie k jednotlivym jedlam
        if riadocek[1] == "z":
            pocet_z += 1
        elif riadocek[1] == "c":
            pocet_c += 1
        elif riadocek[1] == "m":
            pocet_m += 1
        elif riadocek[1] == "o":
            pocet_o += 1
            
#zavolanie funkcie
pocty()

#podmienka na zistenie nedostatku jedal, pripadne ulozenie do zoznamu
if pocet_z < 20:
    nedostatok.append("z")
if pocet_c < 20:
    nedostatok.append("c")
if pocet_m < 20:
    nedostatok.append("m")
if pocet_o < 20:
    nedostatok.append("o")

#vypisanie pozadovanych hodnot
print("Dokopy:",pocet_jedal)
print("Zelené:",pocet_z)
print("Červené:",pocet_c)
print("Modré:",pocet_m)
print("Oranžové:",pocet_o)
print("Nedostatok:",",".join(nedostatok))

#podmienka na vypisanie oznamu o dostatku vsetkych jedal
if len(nedostatok) == 0:
      print("Všetkých jedál bolo dostatok.")

#zatvorenie suboru
subor.close()
