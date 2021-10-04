import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa3dba6b6245fc92b5c627540037bf035"
# Your Auth Token from twilio.com/console
auth_token = "37849b9f9bf70f9f537566b5c400b788"

client = Client(account_sid, auth_token)

# comentario em python
# Passo a passo de solução
# Abrir arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']



# tabela_vendas = pd.read_excel ('Vendas.xlsx') # lendo um arquivo excel
# usando o loop for para executar varios arquivos

for mes in lista_meses:
#print(mes)
# tabela_vendas = pd.read_excel('Vendas.xlsx')
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') #nome dinamico
#print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] #localiza um linha da tabela
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
# Quando você usa o loc ele devolve uma tabela precisa usar o .values[0]
        print (f'No mês de {mes} o Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511982971491",
            from_="+12182454435",
            body=f'No mês de {mes} o Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
        print('Mensagem enviada!')


# para cada arquivo:
# verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000
# se for maior do que 55.000 -> Envia um SMS com o Nome, o mês eas vendas do vendedor
# Caso não seja maior do que 55.000 não quero fazer nada
# Instalar as Bibliotecas que será utilizada:
# pandas - integração entre python e excel
# openpyxl - integração entre python e excel
# twilio - envia o SMS pelo python