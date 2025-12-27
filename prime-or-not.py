num = int(input("ENTER THE NUMBER THAT YOU WANT TO CHECK: "))

if num <= 1:
    print("THE NUMBER YOU ENTER IS NOT A PRIME")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break   

    if is_prime:
        print("THE NUMBER YOU ENTER IS PRIME")
    else:
        print("THE NUMBER YOU ENTER IS NOT A PRIME")
