def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

def sum_primes(max):
    sum = 0
    for j in range(2, max):
        if is_prime(j):
            sum += j
    return sum

def print_primes_in_interval(min, max):
    primes_list_in_interval = []
    for i in range(min, max):
        if is_prime(i):
            primes_list_in_interval.append(i)
    return primes_list_in_interval
            
        
         
# print(is_prime(20021641))

# print(sum_primes(100))

primes = print_primes_in_interval(10000, 10050)
print(', '.join(str(v) for v in primes))