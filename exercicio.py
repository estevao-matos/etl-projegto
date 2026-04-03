import pandas as pd #extração
users = [{'id': 1, 'name': 'estevão'},
           {'id': 2, 'name': 'dudu'},
           {'id': 3, 'name': 'Bela'}]
df = pd.DataFrame(users)
print(df)

def gerar_mensagem(nome): #transformação
  return f"{nome}, invista hoje para garantir um futuro financeiro melhor!"
  df['mensagem'] = df['name'].apply(gerar_mensagem)

print(df)

df.to_csv('resultado.csv', index=False)

import pandas as pd

# 1. Extração
users = [{'id': 1, 'name': 'estevão'},
         {'id': 2, 'name': 'dudu'},
         {'id': 3, 'name': 'Bela'}]
df = pd.DataFrame(users)

print("--- Primeiro Print (Antes da Transformação) ---")
print(df)

# 2. Transformação
def gerar_mensagem(nome):
    return f"{nome}, invista hoje para garantir um futuro financeiro melhor!"

# ESTA LINHA DEVE FICAR FORA DA FUNÇÃO (sem espaços extras no início)
df['mensagem'] = df['name'].apply(gerar_mensagem)

print("\n--- Segundo Print (Depois da Transformação) ---")
print(df)

# 3. Carregamento
df.to_csv('resultado.csv', index=False)
