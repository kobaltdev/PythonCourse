def sum_even_numbers(start, stop):
    sum = 0
    for i in range(start, stop+1):
        if i % 2 == 0:
            sum += i

sum_even_numbers(0, 100)
