def penjadwalan(s, f, m):
	n = len(s)
	t = 1
	A = []
	B = []

	if n != len(f):
		raise Exception("Jumlah input waktu mulai dan waktu akhir harus sama")

	for i in range(0, n):
		if s[i] >= t and f[i] <= m:
			A.append(i + 1)
			t = f[i]
		else:
			B.append(i + 1)

	return (A, B)

def main():
	s = input("Masukkan waktu mulai: ").split()
	f = input("Masukkan waktu akhir: ").split()
	m = input("Masukkan batas waktu pelayanan: ")
	s = [int(i) for i in s]
	f = [int(i) for i in f]

	try:
		jadwal = penjadwalan(s, f, int(m))

		print("\nJadwal grup band hari pertama:")
		for g in jadwal[0]:
			print("Grup Band No. ", g)

		print("\nJadwal grup band hari berikutnya:")
		for g in jadwal[1]:
			print("Grup Band No. ", g)	

	except Exception as e:
		raise e


if __name__ == '__main__':
	main()

