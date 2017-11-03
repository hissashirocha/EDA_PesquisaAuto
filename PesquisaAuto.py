import pandas as pd
from random import sample
import numpy as np

planilha = pd.read_excel('PesquisaAuto.xlsx', sheet_name=0, usecols="A:K") # Carrega a primeira aba da planilha (sheet_name = 0) e apenas as colunas de A a K

# print("Soma: " + str(planilha['Imagem'].sum()) +
#       "\nMedia: " + str(planilha['Imagem'].mean()) +
#       "\nMin: " + str(planilha['Imagem'].min()) +
#       "\nMax: " + str(planilha['Imagem'].max()))

# print(planilha['Imagem'].describe())

# Descrevendo as estatisticas basicas para cada coluna do DataFrame
# for column in planilha:
#     print(planilha[column].describe())

# Visualizando uma parcela dos dados
# print(planilha.head(5))
# print(planilha.tail(5))
# print(planilha.sample(5))

# Amostra aleatoria
randomIndex = np.array(sample(range(len(planilha)), 5))
amostra = planilha.ix[randomIndex]
print(amostra)

# Fazendo consultas no DataFrame
print(planilha.query('Imagem > Preco'))
print(planilha.query('Genero == 1'))
print(planilha[planilha.Genero == 2])

# Lidando com Missing Values
print(pd.isnull(planilha['Pequeno'])) #Testa se existem missing values - retorna True ou False
# print(planilha.Pequeno.fillna("sim")) #Preenche missing values com "sim"
print(planilha.dropna(axis=0)) # Detela linhas que tenham algum valor missing
print(planilha.dropna(axis=1)) # Detelha colunas que tenham algum valor missing
# print(planilha.interpolate()) # Implementa metodos de interpolacao, como polynomial ou cubic interpolation

# Criando linha de totais nas columas Imagem, Utilitario e Preco
# sum_row = planilha[["Imagem","Utilitario","Preco"]].sum() # Soma totais para cada uma das colunas
# sum_planilha = pd.DataFrame(data=sum_row).T # Transpoe a coluna em linha
# sum_planilha = sum_planilha.reindex(columns=planilha.columns) # Acrescenta as demais colunas da tabela original
# planilha_final = planilha.append(sum_planilha,ignore_index=True) # Acrescenta os totais nas colunas respectivas
# print(planilha_final.tail()) # Apresenta as ultimas linhas
