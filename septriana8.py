tunai = True
transfer = False

pembayaran = tunai ^ transfer

if pembayaran:
   print("METODE PEMBAYARAN BERHASIL")
else:
  print("METODE PEMBAYARAN TIDAK BERHASIL")