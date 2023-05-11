import pandas as pd
import matplotlib.pyplot as plt

tabelatotal = pd.read_csv('INFLUD19.csv', sep=';', encoding='latin1')
tabelatotal["DT_NOTIFIC"] = pd.to_datetime(tabelatotal["DT_NOTIFIC"], format="%d/%m/%Y")
tab2019 = tabelatotal[tabelatotal["DT_NOTIFIC"].dt.year == 2019]


tabocorrenciasporcidade = tab2019['ID_MUNICIP'].value_counts()
topcidades = tabocorrenciasporcidade.head(5)


print(" Cidades com mais casos de síndrome respiratória em 2019")
for cidade, ocorrencias in topcidades.items():
    print(f" {cidade} com {ocorrencias} casos")

cidades = topcidades.index
ocorrencias = topcidades.values

plt.bar(topcidades.index, topcidades.values, color='red', width=0.6)
plt.xlabel('Cidades')
plt.ylabel('ocorrências')
plt.title( 'Cidades com mais casos de síndrome respiratória em 2019 ')
for i in range(len(topcidades)):
    plt.text(topcidades.index[i], topcidades.values[i]+20, str(topcidades.values[i]), ha='center')
plt.show()