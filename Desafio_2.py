def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or a == n

if __name__ == "__main__":
    n = int(input("Informe um número: ").strip())
    if fibonacci(n):
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")
