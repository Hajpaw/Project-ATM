#!/usr/bin/python3

baza_uzytk = {}

class User:
	def __init__(self,imie,pin,stan_konta):
		self.imie = imie
		self.pin = pin
		self.stan_konta = stan_konta

	def add_user(imie):
		tmp = []
		#tmp.append(input("Podaj imię nowego użytkownika: "))
		tmp.append(int(input("\nPodaj PIN nowego użytkownika: ")))
		tmp.append(int(input("\nPodaj stan konta nowego użytkownika: ")))
		print('\n')
		baza_uzytk[imie] = tmp
		print(imie,'\n',tmp)
		return baza_uzytk
	def check_db():
		print(baza_uzytk)

class Operacja:
	def __init__(self,typ,karta):
		self.typ = typ
		self.karta = karta

	def wyplata(ilosc,kto):
		if baza_uzytk[kto][1] >= ilosc:
			baza_uzytk[kto][1] = baza_uzytk[kto][1] - ilosc
			return baza_uzytk
		else:
			print("Nie masz wystarczających środków na koncie")

	def sprawdzenie(kto):
		print(f'Stan konta {kto} wynosi: ')
		print(baza_uzytk[kto][1])

	def darowizna(ilosc,kto,akcja):
		if baza_uzytk[kto][1] >= ilosc:
			baza_uzytk[kto][1] = baza_uzytk[kto][1] - ilosc
			print(f'Dziękujemy za przekazanie pieniędzy na rzecz {akcja}')
			return baza_uzytk
		
		else:
			print("Nie masz wystarczających środków na koncie")

#User.add_user('Wojtek')

#print(baza_uzytk)
