import json

def calcular_faturamento(faturamento_diario):
    faturamento = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]
    menor_valor = min(faturamento)
    maior_valor = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_da_media = sum(1 for valor in faturamento if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_da_media

if __name__ == "__main__":
    with open('dados.json', 'r') as file:
        faturamento_diario = json.load(file)
    
    menor_valor, maior_valor, dias_acima_da_media = calcular_faturamento(faturamento_diario)
    
    print(f"Menor valor de faturamento: {menor_valor}")
    print(f"Maior valor de faturamento: {maior_valor}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
