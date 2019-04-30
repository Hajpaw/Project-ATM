#!/usr/bin/python3

baza_uzytk = {}

def db_update():

	data_bb = open("./db.txt","r")
	for line in data_bb:
		x = line.split(",")
		a = x[0]
		b = x[1]
		c = x[2]
		e = len(c) - 1
		c = c[0:e]
		baza_uzytk[a] = [int(b),int(c)]
	data_bb.close()

db_update()

class User:
	def __init__(self,imie,pin,stan_konta):
		self.imie = imie
		self.pin = pin
		self.stan_konta = stan_konta

	def add_user(imie):
		data_b = open("./db.txt","a+")
		pin = (input("\nPodaj PIN nowego użytkownika: "))
		stan_k = (input("\nPodaj stan konta nowego użytkownika: "))
		print('\n')
		data_b.write(imie)
		data_b.write(",")
		data_b.write(pin)
		data_b.write(",")
		data_b.write(stan_k)
		data_b.write("|")
		data_b.close()
		db_update()

	def check_db():
		print(baza_uzytk)

class Operacja:
	def __init__(self,typ,karta):
		self.typ = typ
		self.karta = karta

	def wyplata(ilosc,kto):
		if int(baza_uzytk[kto][1]) >= ilosc:
			(baza_uzytk[kto][1]) = (baza_uzytk[kto][1]) - ilosc
			print(f"Wypłacono {ilosc} zł.\n")
			return baza_uzytk
		else:
			print("Nie masz wystarczających środków na koncie")

	def sprawdzenie(kto):
		print(f'Stan konta {kto} wynosi: {baza_uzytk[kto][1]} zł')

	def darowizna(ilosc,kto,akcja):
		if int(baza_uzytk[kto][1]) >= ilosc:
			(baza_uzytk[kto][1]) = (baza_uzytk[kto][1]) - ilosc
			print(f'Dziękujemy za przekazanie pieniędzy na rzecz {akcja}')
			return baza_uzytk
		
		else:
			print("Nie masz wystarczających środków na koncie")

