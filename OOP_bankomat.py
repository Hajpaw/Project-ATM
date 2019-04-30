#!/usr/bin/python3

import sys
import os
import time
from getpass import getpass
import operacje

os.system('toilet -f mono12 -F metal Bankomat')
print('\n')
os.system('cal')
print('\n')

admin = sys.argv
if len(admin) == 2:
	while admin[1] == 'adduser':
		os.system('date')
		to_add_or_not_to_add = input("Jeśli chcesz sprawdzić bazę danych naciśnij *B*\nJeśli chcesz dodać użytkownika naciśnij *A*\nJeśli chcesz dodać kilku użytkowników naciśnij *W*\nJeśli chcesz wyjść naciśnij *Q*\n: ")
		if to_add_or_not_to_add.lower() == 'a':
			jakie_imie_a = input('Podaj imię użytkownika: ')
			operacje.User.add_user(jakie_imie_a)

		elif to_add_or_not_to_add.lower() == 'b':
			operacje.User.check_db()

		elif to_add_or_not_to_add.lower() == 'w':
			ile_kont = int(input("Podaj liczbę kont, które chcesz dodać\n: "))
			for i in range(ile_kont):
				jakie_imie_w = input('Podaj imię użytkownika: ')
				print('\n')
				operacje.User.add_user(jakie_imie_w)

		elif to_add_or_not_to_add.lower() == 'q':
			break

		else:
			print("Wystąpił błąd!\nŹle wprowadzone dane!")

elif len(admin) == 1:
	while True:
		os.system('date')
		rodzaj_trans = input("\nWybierz czy chcesz wykonać transakcję z kartą *K*  czy bez karty *BK*\nNaciśnij *Q* aby wyjść\n: ")
		time.sleep(1)
		if rodzaj_trans.lower() == 'k':
			print("Proszę włożyć kartę")
			time.sleep(4)
			kim_jestes_k = input("Podaj swoje imię\n: ")
			if kim_jestes_k in operacje.baza_uzytk.keys():
				check_pin = int(getpass("Wprowadź kod PIN\n: "))
				if check_pin == int(operacje.baza_uzytk[kim_jestes_k][0]):
					co_dalej = input("Wybierz co chcesz dalej zrobić:\nSprawdzić stan konta - wciśnij *S*\nPrzekazać darowiznę - wciśnij *D*\nWypłacić - wciśnij *W*\nPowrócić do poprzedniego ekranu - wciśnij *B*\nWyjść - wciśnij *Q*\n:")
					if co_dalej.lower() == 's':
						operacje.Operacja.sprawdzenie(kim_jestes_k)

					elif co_dalej.lower() == 'q':
						break

					elif co_dalej.lower() == 'b':
						continue

					elif co_dalej.lower() == 'w':
						no_ile = int(input("Podaj kwotę, którą chcesz wypłacić\n: "))
						if no_ile%10==0:
							operacje.Operacja.wyplata(no_ile,kim_jestes_k)

						else:
							print('Źle wprowadzona kwota. Pamiętaj, że wypłacać możesz tylko kwoty zaokrąglone do dziesiątek.')

					elif co_dalej.lower() == 'd':
						jaka_akcja = input("Wpisz nazwę akcji, na którą chcesz przekazać datek\nDamian\nSzlachetnaPaczka,\nWOŚP\nGreenpeace\n: ")
						no_ile_d = int(input(f"Podaj kwotę, którą chcesz przeznaczyć na {jaka_akcja}\n: "))
						operacje.Operacja.darowizna(no_ile_d,kim_jestes_k,jaka_akcja)

				else:
					print("Wprowadzono błędny kod PIN")

			else:
				print("Użytkownik nie znajduje się w bazie")

		elif rodzaj_trans.lower() == 'bk':
			print("Proszę zbliżyć kartę")
			time.sleep(5)
			kim_jestes = input("Podaj swoje imię\n: ")
			time.sleep(1)
			ile_bk = int(input("Jaką ilość chcesz wypłacić?\n50\n40\n20\n: "))
			if ile_bk is int and kim_jestes is string:
				operacje.Operacja.wyplata(ile_bk,kim_jestes)

			else:
				print("Coś poszło nie tak!")
				continue

		elif rodzaj_trans.lower() == 'q':
			print("Dziękujemy za korzystanie z naszych usług")
			time.sleep(0.5)
			os.system('figlet Do ')
			os.system('figlet zobaczenia!')
			time.sleep(1)
			break

		else:
			print("Wystąpił błąd!\nŹle wprowadzone dane!")
			continue
