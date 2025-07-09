def main():
    case = 1
    while True:
        n, b = map(int, input().split())
        if n == 0 and b == 0:
            break
        if b == 1:
            print(f"Case {case}: {n} {b} 0")
            case += 1
            continue
        
        if n == 0 or n == 1:
            calls_mod = 1 % b
        else:
            fib_n1_mod = fib_mod(n + 1, b)
            calls_mod = (2 * fib_n1_mod - 1) % b
        
        print(f'Case {case}: {n} {b} {calls_mod}')
        case += 1


def pisano_period(m):
    if m == 1:
        return 1
    a, b = 0, 1
    for i in range(m * m):
        a, b = b, (a + b) % m
        if a == 0 and b == 1:
            return i + 1
    return m * m


def fib_mod(n, m):
    if n == 0:
        return 0
    period = pisano_period(m)
    n = n % period
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % m
    return b


main()