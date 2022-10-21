
import pandas as pd
tmdb = pd.read_csv('tmdb_5000_movies.csv')
tmdb.head()

tmdb.describe()

import seaborn as sns

sns.distplot(tmdb.vote_average)

# melhorando o gráfico
import seaborn as sns

ax = sns.distplot(tmdb.vote_average)
ax.set(xlabel="Nota média", ylabel="Densidade")
ax.set_title("Média de votos em filmes no TMDB 5000")

# melhorando o gráfico
import seaborn as sns

ax = sns.distplot(tmdb.vote_average, norm_hist = False, kde = False)
ax.set(xlabel="Nota média", ylabel="Frequência")
ax.set_title("Média de votos em filmes no TMDB 5000")

sns.boxplot(x=tmdb.vote_average)

# gráfico melhorado
ax = sns.boxplot(tmdb.vote_average)
ax.set(xlabel='Nota  média do filme')
ax.set_title('Distribuição de nota média dos filmes do TMDB 5000')

# Consultando filmes com votação = 0

tmdb.query("vote_average == 0").head()

# Limpando o bd

tmdb_com_mais_de_10_votos = tmdb.query("vote_count >= 10")
tmdb_com_mais_de_10_votos.describe()

# Reanalizando os dados

ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_average, norm_hist = False, kde = False)
ax.set(xlabel="Nota média", ylabel="Frequência")
ax.set_title("Média de votos em filmes no TMDB 5000 dentre os filmes com 10 ou mais votos")

ax = sns.boxplot(tmdb_com_mais_de_10_votos.vote_average)
ax.set(xlabel='Nota  média do filme')
ax.set_title('Distribuição de nota média dos filmes do TMDB 5000 dentre os filmes com 10 ou mais votos')

# Analisaremos também o movielens

notas = pd.read_csv("ratings.csv")
notas.head()

# Calculando a média das notas

nota_media_por_filme = notas.groupby("movieId").mean()["rating"]
nota_media_por_filme.head()

ax = sns.distplot(nota_media_por_filme.values)
ax.set(xlabel="Nota média", ylabel="Frequência")
ax.set_title("Média de votos em filmes no Movielens 100k")

# Filtrando o bd, limpando filmes com menos de 10 notas

quantidade_de_votos_por_filme = notas.groupby("movieId").count()
filmes_com_pelo_menos_10_votos = quantidade_de_votos_por_filme.query("rating >= 10").index
filmes_com_pelo_menos_10_votos.values

# Bd com a filtragem dos dados

nota_media_dos_filmes_com_pelo_menos_10_votos = nota_media_por_filme.loc[filmes_com_pelo_menos_10_votos.values]
nota_media_dos_filmes_com_pelo_menos_10_votos.head()

# Analisando os dados

ax = sns.distplot(nota_media_dos_filmes_com_pelo_menos_10_votos)
ax.set(xlabel='Nota média', ylabel='Densidade')
ax.set_title('Média de votos em filmes no MovieLens')

ax = sns.boxplot(x=nota_media_dos_filmes_com_pelo_menos_10_votos.values)
ax.set(xlabel='Nota  média do filme')
ax.set_title('Distribuição de nota média dos filmes do MovieLens')

# Analisando a distribuição percentual cumulativa da quantidade de filmes por média de voto

ax = sns.distplot(nota_media_dos_filmes_com_pelo_menos_10_votos, 
                  hist_kws = {'cumulative':True}, 
                  kde_kws = {'cumulative':True})
ax.set(xlabel='Nota média', ylabel='% acumulado de filmes')
ax.set_title('Média de votos em filmes no MovieLens com mais de 10 votos')

ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_average, 
                  hist_kws = {'cumulative':True}, 
                  kde_kws = {'cumulative':True})
ax.set(xlabel='Nota média', ylabel='% acumulado de filmes')
ax.set_title('Média de votos em filmes no TMDB 5000 com 10 ou mais votos')

# Analisando a distribuição dos dados capturados de outros campos do TMDB

tmdb_com_mais_de_10_votos.head()

tmdb_com_mais_de_10_votos.vote_count

# Analisando a distribuição da contagem de votos

ax = sns.distplot(tmdb_com_mais_de_10_votos.vote_count)
ax.set(xlabel='Número de votos', ylabel='Densidade')
ax.set_title('Número de votos em filmes no TMDB 5000 com 10 ou mais votos')

tmdb.budget

# Limpando do bd filmes com budget = 0

ax = sns.distplot(tmdb.query("budget > 0").budget)
ax.set(xlabel='Gastos', ylabel='Densidade')
ax.set_title('Gastos em filmes no TMDB 5000')

tmdb.query("popularity == 0")

# Analisando a distribuição da popularidade

ax = sns.distplot(tmdb.popularity)
ax.set(xlabel='Popularidade', ylabel='Densidade')
ax.set_title('Popularidade dos filmes no TMDB 5000')

# Verificando a coluna runtime se possui algum filme com valor nulo

tmdb.runtime.isnull().sum()

# Analisando a distribuição do runtime dropando valores nulo

ax = sns.distplot(tmdb.runtime.dropna())
ax.set(xlabel='Duração', ylabel='Densidade')
ax.set_title('Duração dos filmes no TMDB 5000')

# Filtrando runtime com valores maiores que zero e não nulos

ax = sns.distplot(tmdb.query("runtime>0").runtime.dropna())
ax.set(xlabel='Tempo de duração', ylabel='Densidade')
ax.set_title('Duração dos filmes no TMDB 5000')

# Analisando a distribuição cumulativa de filmes por runtime

ax = sns.distplot(tmdb.query("runtime>0").runtime.dropna(),
                 hist_kws={'cumulative':True},
                 kde_kws={'cumulative':True})
ax.set(xlabel='Tempo de duração', ylabel='% de filmes')
ax.set_title('Duração dos filmes no TMDB 5000')

# Verificando a máxima duração de 80% dos filmes

tmdb.query("runtime>0").runtime.dropna().quantile(q=0.8)

# Movielens: média dos filmes com pelo menos 10 votos

print("Media dos filmes com pelo menos 10 votos", nota_media_dos_filmes_com_pelo_menos_10_votos.mean())

# Cálculo da média de 5 notas
nota_media_dos_filmes_com_pelo_menos_10_votos[0:5].mean()

# Tamanho da amostra
len(nota_media_dos_filmes_com_pelo_menos_10_votos)

# Gerando uma lista com a média das notas somadas acumuladamente
medias = list()
for i in range(1, len(nota_media_dos_filmes_com_pelo_menos_10_votos)):
    medias.append(nota_media_dos_filmes_com_pelo_menos_10_votos[0:i].mean())
medias

# Verificando o comportamento da média com a adição de notas na amostra

import matplotlib.pyplot as plt

medias = list()
for i in range(1, len(nota_media_dos_filmes_com_pelo_menos_10_votos)):
    medias.append(nota_media_dos_filmes_com_pelo_menos_10_votos[0:i].mean())
plt.plot(medias)

# Analisando o mesmo comportamento das médias com a adição de notas porém misturando os dados do db com o sample

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(75243)
temp = nota_media_dos_filmes_com_pelo_menos_10_votos.sample(frac=1)

medias = list()
for i in range(1, len(temp)):
    medias.append(temp[0:i].mean())
plt.plot(medias)

# Melhorando o código

np.random.seed(75243)
temp = nota_media_dos_filmes_com_pelo_menos_10_votos.sample(frac=1)

medias = [temp[0:i].mean() for i in range(1, len(temp))]

plt.plot(medias)

# Verificando o intervalo de confiança no ztest

from statsmodels.stats.weightstats import zconfint

zconfint(nota_media_dos_filmes_com_pelo_menos_10_votos)

# Verificando o intervalo de confiança no ttest

from statsmodels.stats.weightstats import DescrStatsW

descr_todos_com_10_votos = DescrStatsW(nota_media_dos_filmes_com_pelo_menos_10_votos)
descr_todos_com_10_votos
descr_todos_com_10_votos.tconfint_mean()

# Vamos ver o filme 1 ...

filmes = pd.read_csv("movies.csv")
filmes.head()

filmes.query("movieId==1")

# Filtrando as notas do filme 1 da lista
notas1 = notas.query("movieId ==1")
notas1.head()

# Verificando a distribuição de notas do filme
ax = sns.distplot(notas1.rating)
ax.set(xlabel='Nota', ylabel='Densidade')
ax.set_title('Distribuição das notas para o Toy Story')

ax = sns.boxplot(notas1.rating)
ax.set(xlabel='Notas')
ax.set_title('Distribuição das notas para o Toy Story')

# Verificando a média das notas do filme 1
notas1.rating.mean()

notas1.rating.count()

# Verificando o intervalo do ztest para o filme 1
zconfint(notas1.rating)

# Com a verificação do p.value determinamos que a média é diferente da média geral
from statsmodels.stats.weightstats import ztest

ztest(notas1.rating, value = 3.4320503405352603)

# Verificando a distribuição das médias cumulativas do filme 1 com a quantidade de notas
np.random.seed(75241)
temp = notas1.sample(frac=1).rating

medias = [temp[0:i].mean() for i in range(1, len(temp))]

plt.plot(medias)

# Na verificação confirmamos que com poucos dados na amostra não conseguiriamos tomar uma definição acertiva quanto a diferença entre os resultados
np.random.seed(75241)
temp = notas1.sample(frac=1).rating

def calcula_teste(i):
    media = temp[0:i].mean()
    stat, p = ztest(temp[0:i], value = 3.4320503405352603) 
    return (i, media, p)

valores = np.array([calcula_teste(i) for i in range(2, len(temp))])

plt.plot(valores[:,0], valores[:,1])
plt.plot(valores[:,0], valores[:,2])
plt.hlines(y = 0.05, xmin = 2, xmax = len(temp), colors = 'r')

# Comparando os dois conjuntos de amostras

print (ztest(notas1.rating, notas.rating))
zconfint(notas1.rating, notas.rating)

from scipy.stats import ttest_ind

ttest_ind(notas.rating, notas1.rating)

descr_todas_as_notas = DescrStatsW(notas.rating)
descr_toystory = DescrStatsW(notas1.rating)
comparacao = descr_todas_as_notas.get_compare(descr_toystory)

comparacao.summary()

comparacao.summary(use_t=True)

import matplotlib.pyplot as plt

plt.boxplot([notas.rating, notas1.rating], labels=["Todas as notas", "Toy Story"])
plt.title("Distribuição das notas de acordo com filmes")

# Testando o boxplot com uma amostra pequenas teriamos que as médias são parecidas, distorcendo a realidade
import matplotlib.pyplot as plt

plt.boxplot([notas.rating, notas1[3:12].rating], labels=["Todas as notas", "Toy Story (do 3 ao 12)"])
plt.title("Distribuição das notas de acordo com filmes")

descr_todas_as_notas = DescrStatsW(notas.rating)
descr_toystory = DescrStatsW(notas1[3:12].rating)
comparacao = descr_todas_as_notas.get_compare(descr_toystory)

comparacao.summary(use_t=True)

# Comparando a média de dois filmes

filmes.query("movieId in [1, 593, 72226]")

notas1 =  notas.query("movieId == 1")
notas593 =  notas.query("movieId == 593")
notas72226 =  notas.query("movieId == 72226")

plt.boxplot([notas1.rating, notas593.rating, notas72226.rating], labels=["Toy Story", "Silence of the Lambs,", "Fantastic Mr. Fox"])
plt.title("Distribuição das notas de acordo com filmes")

notas72226.describe()

sns.boxplot(x = "movieId", y = "rating", data = notas.query("movieId in (1, 593, 72226)"))

descr_1 = DescrStatsW(notas1.rating)
descr_593 = DescrStatsW(notas593.rating)
comparacao = descr_1.get_compare(descr_593)

comparacao.summary()

descr_72226 = DescrStatsW(notas72226.rating)
descr_593 = DescrStatsW(notas593.rating)
comparacao = descr_72226.get_compare(descr_593)

comparacao.summary(use_t=True)

comparacao = descr_1.get_compare(descr_72226)
comparacao.summary(use_t=True)

notas.query("movieId in (1, 593, 72226)").groupby("movieId").count()

# Verificando se temos uma distribuição normal nas amostras

# Sendo p < que nosso limiete de 0,05(5%) descartamos a hipotese de uma distribuição normal
from scipy.stats import normaltest

_, p = normaltest(notas1.rating)
p

# Não sendo uma distribuição normal confirmamos com teste não paramétrico que sendo p < que 0,05(5%), temos que existe uma tendência de os valores de uma amostra ser maiores que da outra amostra.
# Na conclusão entendemos que existe a probabilidade de ao escolhermos 2 notas aleatórias existe uma grande chance de uma ser maior que a outra. 
from scipy.stats import ranksums

_, p = ranksums(notas1.rating, notas593.rating)
p