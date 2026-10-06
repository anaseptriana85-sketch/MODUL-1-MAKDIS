total_belanja = 75000
voucher = True

gratis_ongkir = total_belanja or voucher

if gratis_ongkir:
   print("MENDAPATKAN GRATIS ONGKIR")
else:
  print(" TIDAK MENDAPATKAN GRATIS ONGKIR")