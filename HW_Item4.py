prime_list = []

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(num)

numbers_to_check = prime_list

for num in numbers_to_check:
    if num < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
                
    if not is_prime:
        print(f"{num} ไม่เป็นจำนวนเฉพาะ")
    else:
        print(f"{num} เป็นจำนวนเฉพาะ")
