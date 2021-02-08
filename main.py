# liczby w indeksie
# a = [1,2,3,4,5,6,7,8,9,10]
# for a in a:
#     c = a-1
#     print(c)

tab = [1,2,3,4,5,6,7,8,9,10]
# print(tab[::2]) # co drugi element począwszy od 0-go elem. w indeksie (nieparzyste) == tab[0::2]
# print(tab[1::2]) # co drugi element począwszy od 1-go elem. w indeksie (nieparzyste) == tab[0::2]
print(tab[2:-2:2]) # -2 za : daje z końca tablicy :2 bierze co drugi element
