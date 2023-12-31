#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	puissance = (voltage ** 2) / resistance
	return puissance

def orthogonal(v1, v2):
	dot_product = (v1[0] * v2[0]) + (v1[1] * v2[1])
	return dot_product == 0
       
def average(values):
	list_number = [ number for number in values if number >= 0]
	positive_number = 0
	for number in list_number:
		positive_number += number
		average_positive = positive_number / len(list_number)
	return average_positive


def bills(value):
    hundred = twenties = tens = fives = ones = 0
    while value != 0:
        if  value >= 100:
            hundred += (value // 100)
            value %= 100
        elif value >= 20:
            twenties += (value // 20)
            value %= 20
        elif value >= 10:
            tens += (value // 10)
            value %= 10
        elif value >= 5:
            fives += (value // 5)
            value %= 5
        elif value >= 1:
            ones += (value // 1)
            value %= 1
    return (hundred,twenties,tens, fives, ones)


def format_base(value, base,letters):
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		digit_value = abs_value % base
		result += letters[digit_value]
		abs_value //= base
	if value < 0:
		result += "-"
	return result[::-1]


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-2003, 16,"0123456789ABCDEF"))
