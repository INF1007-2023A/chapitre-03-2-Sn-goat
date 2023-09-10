#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	input_voltage = voltage
	input_resistance = resistance
	puissance = (input_voltage ** 2) / input_resistance
	return puissance

def orthogonal(v1, v2):
	dot_product = (v1[0] * v2[0]) + (v1[1] + v2[1])
	return dot_product == 0
       
def average(values):
	list_number = []
	for number in values:
		if number >= 0:
			list_number.append(number)
	positive_number = 0
	for number in list_number:
		positive_number += number
		average_positive = positive_number / len(list_number)
	return average_positive

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	while value != 0:
		if value >= 20:
			pass
		elif value >= 10:
			pass
		elif value >= 5:
			pass
		elif value >= 1:
			pass

	return (twenties, tens, fives, twos, ones);

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
