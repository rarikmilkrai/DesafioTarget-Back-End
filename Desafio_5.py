def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

if __name__ == "__main__":
    s = input("Informe uma string: ").strip()
    print(f"String invertida: {inverter_string(s)}")
