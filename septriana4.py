member = False
promo = True

diskon = member or promo

if diskon:
   print("PELANGGAN MENDAPATKAN DISKON")
else:
  print("PELANGGAN TIDAK MENDAPATKAN DISKON")