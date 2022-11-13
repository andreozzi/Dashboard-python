

import pandas as pd
from pandas.core.frame import DataFrame
import plotly.express as px
import plotly
import plotly.graph_objects as go
import dash
from dash import Dash, dcc, html, Input, Output 
import dash_bootstrap_components



##Objetivo do gráfico monstrar em um gráfico de barras a Porcentagem de acertos de lançes livres de times do leste e oeste dos eua 
## puxando as bases de dados e transformando-as em lista
#Base 1 - 2014-15
df_s14_15 = pd.read_csv(r'C:\Users\Victor\.vscode\project\docs\SEASON 2014-15 STATS OF NBA BOTH CONFERENCE  - 1.csv')

#Base 2 - 2015-16
df_s2015_16 = pd.read_csv(r'C:\Users\Victor\.vscode\project\docs\SEASON 2015-16 STATS OF NBA BOTH CONFERENCE  - 1.csv')

#Base 3 - Temporada 2016-17

df_s2016_17 = pd.read_csv(r'C:\Users\Victor\.vscode\project\docs\SEASON 2016-17 STATS OF NBA BOTH CONFERENCE  - 1.csv')
dflista_s16_17 = df_s2016_17.values.tolist()

#Base 4 

df_s2017_18 = pd.read_csv(r'C:\Users\Victor\.vscode\project\docs\SEASON 2017-18 STATS OF NBA BOTH CONFERENCE  - 1.csv')

#Base 5 - temporada 2018-19

df_s18_19 = pd.read_csv(r'C:\Users\Victor\.vscode\project\docs\SEASON 2018-19 STATS OF NBA BOTH CONFERENCE  - 1 (1).csv')

#Base 6 - temporada 2019-20

df_19_20 = pd.read_csv(r'C:\Users\Victor\.vscode\project\docs\SEASON 2019-20 STATS OF NBA BOTH CONFERENCE  - 1.csv')

#Base 7 - base para extrairmos o dado se o time é do west ou east

df_east_west = pd.read_csv(r'C:\Users\Victor\.vscode\project\docs\SEASON STATS OF NBA 2012-13 WESTREN CONFERENCE  - 1.csv')
dflista_east_west = df_east_west.values.tolist()



## Criando algumas funções
def criar_listas(dataframe):
    listona = dataframe.values.tolist()
    return listona

def colunas(dataf, nome_coluna): # Esta função recebe como primeiro argumento o nome da lista do df que se deseja retirar a coluna e como segundo o nome da coluna que se deseja extrair os dado, sempre entre '' ou ""
    
    valores_coluna = list()
    lista_do_df = criar_listas(dataf)
    indexingbae = list(dataf).index(nome_coluna) 
    for valores in lista_do_df:
        valor = valores[indexingbae]
        valores_coluna.append(valor)
    return valores_coluna

    


def porcentagem_de_acertos(total_lances, lances_feitos): #Essa funçao recebe como argumento o total de lances feitos e o total de pontos feitos e retorna a porcentagem de pontos feitos em relaçao as tentativas
    x = ((lances_feitos)/(total_lances))*100
    return int(x)


##Vendo quais times sao east ou west
##Separado valores em west e east

def separando_val_east(data, coluna_dos_valores): # essa função recebe como argumento o dataframe que sera analisado, e o nome da coluna em str e retornara os valores de times do east
 
    west = colunas(df_east_west, 'Name')
    east_west = colunas(data, 'Team')
    lista_east = list()
    valores = colunas(data, coluna_dos_valores)
    for n in east_west:    
        if n not in west:
            lista_east.append(valores[east_west.index(n)])
        
    return lista_east


def separando_val_west(data, coluna_dos_valores): # essa função recebe como argumento o dataframe que sera analisado, e o nome da coluna em str e retornara os valores de times do west   
    west = colunas(df_east_west, 'Name')
    east_west = colunas(data, 'Team')
    lista_west = list()
    valores = colunas(data, coluna_dos_valores)
    for n in east_west:    
        if n in west:
            lista_west.append(valores[east_west.index(n)])
            
        

    return lista_west

def ordem_east_west(df):
    ordem_east_west = list()
    ambos = colunas(df, 'Team')
    west = colunas(df_east_west, 'Name')
    for n in ambos:
        if n in west:
            ordem_east_west.append('West')
        else:
            ordem_east_west.append('East')
    return ordem_east_west

def string_comvirgula_parainteiro_APENASDADOS2015_16(lista_de_valores): ##Essa função recebe como argumentos uma lista e retorna uma nova lista com valores na formatação certa

    novalista = list()
    for n in lista_de_valores:
        n = n.replace(",", '')
        nn = int(n)
        novalista.append(nn)
    return(novalista)



##Criação do gráfico 
##Aqui estou selecionando as tentativas de lance livre de cada ano dos times do east 

fta_14_15_east=  separando_val_east(df_s14_15, 'FTA')
fta_15_16_east =  separando_val_east(df_s2015_16, 'FTA')
fta_16_17_east =  separando_val_east(df_s2016_17, 'FTA')
fta_17_18_east =  separando_val_east(df_s2017_18, 'FTA')
fta_18_19_east = separando_val_east(df_s18_19, 'FTA')

##Agora vamos pegar o lances que foram pontuados dos times do east

ftm_14_15_east=  separando_val_east(df_s14_15, 'FTM')
ftm_15_16_east =  separando_val_east(df_s2015_16, 'FTM')
ftm_16_17_east =  separando_val_east(df_s2016_17, 'FTM')
ftm_17_18_east =  separando_val_east(df_s2017_18, 'FTM')
ftm_18_19_east = separando_val_east(df_s18_19, 'FTM')

##Agora novamente repitir esse precesso para times do west

fta_14_15_west=  separando_val_west(df_s14_15, 'FTA')
fta_15_16_west =  separando_val_west(df_s2015_16, 'FTA')
fta_16_17_west =  separando_val_west(df_s2016_17, 'FTA')
fta_17_18_west =  separando_val_west(df_s2017_18, 'FTA')
fta_18_19_west = separando_val_west(df_s18_19, 'FTA')



ftm_14_15_west=  separando_val_west(df_s14_15, 'FTM')
ftm_15_16_west =  separando_val_west(df_s2015_16, 'FTM')
ftm_16_17_west =  separando_val_west(df_s2016_17, 'FTM')
ftm_17_18_west =  separando_val_west(df_s2017_18, 'FTM')
ftm_18_19_west = separando_val_west(df_s18_19, 'FTM')


##Dentro da base de dados de 2015 algumas colunas receberam valores em formato de string e nao erm inteiros, ouseja nao da para transformar direto em nmero inteiro, por isso fiz essa funcao, mas ela so serve para os dados de 2015-16

fta_15_16_east = string_comvirgula_parainteiro_APENASDADOS2015_16(fta_15_16_east)
ftm_15_16_east = string_comvirgula_parainteiro_APENASDADOS2015_16(ftm_15_16_east)
fta_15_16_west = string_comvirgula_parainteiro_APENASDADOS2015_16(fta_15_16_west) 
ftm_15_16_west = string_comvirgula_parainteiro_APENASDADOS2015_16(ftm_15_16_west)

##Agora vamos fazer a soma dos valores dessas listas para depois calcular a porcentagem de acertos

w1415fta = sum(fta_14_15_west)
w1516fta = sum(fta_15_16_west)
w1617fta = sum(fta_16_17_west)
w1718fta = sum(fta_17_18_west)
w1819fta = sum(fta_18_19_west)

w1415ftm = sum(ftm_14_15_west)
w1516ftm = sum(ftm_15_16_west)
w1617ftm = sum(ftm_16_17_west)
w1718ftm = sum(ftm_17_18_west)
w1819ftm = sum(ftm_18_19_west)

e1415fta = sum(fta_14_15_east)
e1516fta = sum(fta_15_16_east)
e1617fta = sum(fta_16_17_east)
e1718fta = sum(fta_17_18_east)
e1819fta = sum(fta_18_19_east)

e1415ftm = sum(ftm_14_15_east)
e1516ftm = sum(ftm_15_16_east)
e1617ftm = sum(ftm_16_17_east)
e1718ftm = sum(ftm_17_18_east)
e1819ftm = sum(ftm_18_19_east)


total_acerto_ambas14_15 = w1415fta + e1415fta
total_acerto_ambas15_16 = w1516fta + e1516fta
total_acerto_ambas16_17 = w1617fta + e1617fta
total_acerto_ambas17_18 = w1718fta + e1718fta
total_acerto_ambas18_19 = w1819fta + e1819fta




west1415 = porcentagem_de_acertos(total_acerto_ambas14_15, w1415fta)
west1516 = porcentagem_de_acertos(total_acerto_ambas15_16, w1516fta)
west1617 = porcentagem_de_acertos(total_acerto_ambas16_17, w1617fta)
west1718 = porcentagem_de_acertos(total_acerto_ambas17_18, w1718fta)
west1819 = porcentagem_de_acertos(total_acerto_ambas18_19, w1819ftm)

east1415 = porcentagem_de_acertos(total_acerto_ambas14_15, e1415fta)
east1516 = porcentagem_de_acertos(total_acerto_ambas15_16, e1516fta)
east1617 = porcentagem_de_acertos(total_acerto_ambas16_17, e1617fta)
east1718 = porcentagem_de_acertos(total_acerto_ambas17_18, e1718fta)
east1819 = porcentagem_de_acertos(total_acerto_ambas18_19, e1819fta)

anos = ['2014-15', '2015-16', '2016-17', '2017-18', '2018-19']
westy = list()
westy.append(west1415)
westy.append(west1516)
westy.append(west1617)
westy.append(west1718)
westy.append(west1819)

easty= list()
easty.append(east1415)
easty.append(east1516)
easty.append(east1617)
easty.append(east1718)
easty.append(east1819)




bar1 = go.Bar(x = anos, y=easty, name= 'East' )

bar2 = go.Bar(x = anos, y=westy, name= 'West' )

data1 = [bar1, bar2]

layout = go.Layout(barmode= 'group', title= 'Porcentagem de acertos de lance livre')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
fig = go.Figure(data=data1, layout=layout)
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'])



opcoes_dropdown = list()
for n in anos:
    a = 'Temporada: '+n+' TIMES'
    opcoes_dropdown.append(a)
opcoes_dropdown.append('2014-19 por Conferência')

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children = 'Porcentagem de acertos por conferência de 2014-19'),
    dcc.Dropdown(
        id= 'my dropdown',
        options= opcoes_dropdown,
        value = '2014-19 por Conferência'

    ),
    dcc.Graph(id = 'graf lance', figure= fig),


])


@app.callback(
    Output('graf lance', 'figure'),
    Input('my dropdown', 'value')
    )
def update_figure(selected_year):
    if selected_year == 'Temporada: 2014-15 TIMES':
        b1 = go.Bar(x =colunas(df_s14_15,'Team'), y= colunas(df_s14_15, 'FTA'), name= 'FTA')
        b2 = go.Bar(x = colunas(df_s14_15,"Team"), y=colunas(df_s14_15, 'FTM'), name= 'FTM')
        layaut = go.Layout(barmode='group', title= selected_year)
        dt = [b1,b2]
        figuran = go.Figure(dt, layaut)
        
        colors = {
        'background': '#111111',
        'text': '#7FDBFF'
        }
        
        figuran.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'])
    elif selected_year == 'Temporada: 2015-16 TIMES':
        jj = colunas(df_s2015_16, 'FTA')
        ll = colunas(df_s2015_16, 'FTM')
        jjj = string_comvirgula_parainteiro_APENASDADOS2015_16(jj)
        lll = string_comvirgula_parainteiro_APENASDADOS2015_16(ll)
        b1 = go.Bar(x =colunas(df_s2015_16,'Team'), y= jjj, name= 'FTA')
        b2 = go.Bar(x = colunas(df_s2015_16,"Team"), y=lll, name= 'FTM')
        layaut = go.Layout(barmode='group', title= selected_year)
        dt = [b1,b2]
        figuran = go.Figure(dt, layaut)
        
        colors = {
        'background': '#111111',
        'text': '#7FDBFF'
        }
        
        figuran.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'])
    elif selected_year == 'Temporada: 2016-17 TIMES':
        b1 = go.Bar(x =colunas(df_s2016_17,'Team'), y= colunas(df_s2016_17, 'FTA'), name= 'FTA')
        b2 = go.Bar(x = colunas(df_s2016_17,"Team"), y=colunas(df_s2016_17, 'FTM'), name= 'FTM')
        layaut = go.Layout(barmode='group', title= selected_year)
        dt = [b1,b2]
        figuran = go.Figure(dt, layaut)

        colors = {
        'background': '#111111',
        'text': '#7FDBFF'
        }
        
        figuran.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'])
    elif selected_year == 'Temporada: 2017-18 TIMES':
        b1 = go.Bar(x =colunas(df_s2017_18,'Team'), y= colunas(df_s2017_18, 'FTA'), name= 'FTA')
        b2 = go.Bar(x = colunas(df_s2017_18,"Team"), y=colunas(df_s2017_18, 'FTM'), name= 'FTM')

        layaut = go.Layout(barmode='group', title= selected_year)
        
        dt = [b1,b2]
        figuran = go.Figure(dt, layaut)
        
        colors = {
        'background': '#111111',
        'text': '#7FDBFF'
        }
        
        figuran.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'])

    elif selected_year == 'Temporada: 2018-19 TIMES':
        b1 = go.Bar(x =colunas(df_s18_19,'Team'), y= colunas(df_s18_19, 'FTA'), name= 'FTA')
        b2 = go.Bar(x = colunas(df_s18_19,"Team"), y=colunas(df_s18_19, 'FTM'), name= 'FTM')
        layaut = go.Layout(barmode='group', title= selected_year)
        dt = [b1,b2]
        figuran = go.Figure(dt, layaut)

        colors = {
        'background': '#111111',
        'text': '#7FDBFF'
        }
        
        figuran.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'])
    elif selected_year == '2014-19 por Conferência':
        b1 = go.Bar(x = anos, y=easty, name= 'East' )

        b2 = go.Bar(x = anos, y=westy, name= 'West' )

        dt = [b1, b2]

        layaut = go.Layout(barmode= 'group', title= 'Porcentagem de acertos de lance livre')

        figuran = go.Figure(dt, layaut)

        colors = {
        'background': '#111111',
        'text': '#7FDBFF'
        }
        

        figuran.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'])
    return figuran
   


if __name__ == '__main__':
    app.run_server(debug=True)
