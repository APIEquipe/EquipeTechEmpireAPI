import matplotlib.pyplot as plt
time_data={'Fev-Jul/2020':211,'Jul-Dez/2020':313,'Jan-Jul/2021':49,'Jul-Dez/2021':72,'Jan-Jul/2022':16,'Jul-Dez/2022':4}
figura=plt.figure(figsize=(8,5))
social_media=list(time_data.keys())
time_spend=list(time_data.values())
plt.style.use('Solarize_Light2')
plt.bar(social_media,time_spend,label='Valores gastos em bilhões de reais',color='r')
plt.yticks([0,25,50,75,100,125,150,175,200,225,250,275,300])
plt.title('Gastos da União com Combate à COVID-19 -Até 2022')
plt.legend()
plt.show()
