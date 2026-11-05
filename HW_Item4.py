numbers_to_check = [2, 4, 7, 10, 13, 15, 17]

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