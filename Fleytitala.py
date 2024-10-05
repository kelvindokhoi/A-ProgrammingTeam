import decimal
decimal.getcontext().prec = 10

def skipping(initial, step):
    initial = decimal.Decimal(initial)
    step = decimal.Decimal(step+1)
    total = decimal.Decimal(0)
    if step > 17:
        return decimal.Decimal(initial*decimal.Decimal(1.99999))
    while step > 0:
        total += initial
        initial /= 2
        step -= 1
    return total

def main():
    distance = eval(input())
    bounces = eval(input())
    result = decimal.Decimal(skipping(distance,bounces))
    print(result)

if __name__ == "__main__":
    main()