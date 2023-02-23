
# <font color=green size=10>CURSO DE ESTATÍSTICA - PARTE 4</font>
***

# <font color=green>1 CONHECENDO OS DADOS</font>
***

## <font color=green>1.1 Dataset do projeto</font>
***

### Pesquisa Nacional por Amostra de Domicílios - 2015

A <b>Pesquisa Nacional por Amostra de Domicílios - PNAD</b> investiga anualmente, de forma permanente, características gerais da população, de educação, trabalho, rendimento e habitação e outras, com periodicidade variável, de acordo com as necessidades de informação para o país, como as características sobre migração, fecundidade, nupcialidade, saúde, segurança alimentar, entre outros temas. O levantamento dessas estatísticas constitui, ao longo dos 49 anos de realização da pesquisa, um importante instrumento para formulação, validação e avaliação de políticas orientadas para o desenvolvimento socioeconômico e a melhoria das condições de vida no Brasil.

### Fonte dos Dados

https://ww2.ibge.gov.br/home/estatistica/populacao/trabalhoerendimento/pnad2015/microdados.shtm

### Variáveis utilizadas

> ### Renda
> ***

Rendimento mensal do trabalho principal para pessoas de 10 anos ou mais de idade.

> ### Idade
> ***

Idade do morador na data de referência em anos.

> ### Altura (elaboração própria)
> ***

Altura do morador em metros.

> ### UF
> ***

|Código|Descrição|
|---|---|
|11|Rondônia|
|12|Acre|
|13|Amazonas|
|14|Roraima|
|15|Pará|
|16|Amapá|
|17|Tocantins|
|21|Maranhão|
|22|Piauí|
|23|Ceará|
|24|Rio Grande do Norte|
|25|Paraíba|
|26|Pernambuco|
|27|Alagoas|
|28|Sergipe|
|29|Bahia|
|31|Minas Gerais|
|32|Espírito Santo|
|33|Rio de Janeiro|
|35|São Paulo|
|41|Paraná|
|42|Santa Catarina|
|43|Rio Grande do Sul|
|50|Mato Grosso do Sul|
|51|Mato Grosso|
|52|Goiás|
|53|Distrito Federal|

> ### Sexo	
> ***

|Código|Descrição|
|---|---|
|0|Masculino|
|1|Feminino|

> ### Anos de Estudo
> ***

|Código|Descrição|
|---|---|
|1|Sem instrução e menos de 1 ano|
|2|1 ano|
|3|2 anos|
|4|3 anos|
|5|4 anos|
|6|5 anos|
|7|6 anos|
|8|7 anos|
|9|8 anos|
|10|9 anos|
|11|10 anos|
|12|11 anos|
|13|12 anos|
|14|13 anos|
|15|14 anos|
|16|15 anos ou mais|
|17|Não determinados| 
||Não aplicável|

> ### Cor
> ***

|Código|Descrição|
|---|---|
|0|Indígena|
|2|Branca|
|4|Preta|
|6|Amarela|
|8|Parda|
|9|Sem declaração|

#### <font color='red'>Observação</font>
***
> Os seguintes tratamentos foram realizados nos dados originais:
> 1. Foram eliminados os registros onde a <b>Renda</b> era inválida (999 999 999 999);
> 2. Foram eliminados os registros onde a <b>Renda</b> era missing;
> 3. Foram considerados somente os registros das <b>Pessoas de Referência</b> de cada domicílio (responsável pelo domicílio).

### Solução do problema com dependência do statsmodels
"""

!pip install scipy==1.2 --upgrade

"""### Importando bibliotecas

https://pandas.pydata.org/

https://www.numpy.org/

https://seaborn.pydata.org/
"""

import pandas as pd
import numpy as np
import seaborn as sns

"""### Lendo o dataset do projeto"""

dados = pd.read_csv('dados.csv')

dados.head()

"""---

# <font color=green>2 RODANDO UMA REGRESSÃO LINEAR</font>
***

## Dataset de exemplo
> ### $Y$ = Gasto das famílias
> ### $X$ = Renda das Famílias
"""

dataset = {
    'Y': [3011, 1305, 1879, 2654, 2849, 1068, 2892, 2543, 3074, 849, 2184, 2943, 1357, 2755, 2163, 3099, 1600, 353, 1778, 740, 2129, 3302, 2412, 2683, 2515, 2395, 2292, 1000, 600, 1864, 3027, 1978, 2791, 1982, 900, 1964, 1247, 3067, 700, 1500, 3110, 2644, 1378, 2601, 501, 1292, 2125, 1431, 2260, 1770],
    'X': [9714, 3728, 6062, 8845, 8378, 3338, 8507, 7947, 9915, 1632, 6825, 8918, 4100, 9184, 6180, 9997, 4500, 1069, 5925, 2466, 6083, 9712, 7780, 8383, 7185, 7483, 7640, 2100, 2000, 6012, 8902, 5345, 8210, 5662, 2700, 6546, 2900, 9894, 1500, 5000, 8885, 8813, 3446, 7881, 1164, 3401, 6641, 3329, 6648, 4800]
}

dataset = pd.DataFrame(dataset)
dataset.head()

dataset.shape

"""### Estatísticas descritivas"""

dataset.describe()

"""### Análise gráfica

https://seaborn.pydata.org/generated/seaborn.boxplot.html
"""

ax = sns.boxplot(data=dataset, orient='h', width=0.5)
ax.figure.set_size_inches(12, 6)
ax.set_title('Box plot', fontsize=20)
ax.set_xlabel('Reais (R$)', fontsize=16)
ax

"""https://seaborn.pydata.org/generated/seaborn.lmplot.html"""

ax = sns.lmplot(x="X", y="Y", data=dataset)
ax.fig.set_size_inches(12, 6)
ax.fig.suptitle('Reta de Regressão - Gasto X Renda', fontsize=16, y=1.02)
ax.set_xlabels("Renda das Famílias", fontsize=14)
ax.set_ylabels("Gasto das Famílias", fontsize=14)
ax

"""### Análise da correlação

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html
"""

dataset.corr()

"""### Modelo de regressão linear simples

https://www.statsmodels.org/stable/regression.html
"""

import statsmodels.api as sm

Y = dataset.Y
X = sm.add_constant(dataset.X)

Y.head()

X.head()

"""### Estimando o modelo"""

resultado_regressao = sm.OLS(Y, X).fit()

print(resultado_regressao.summary())

"""### Obtendo as previsões dentro da amostra"""

dataset['Y_previsto'] = resultado_regressao.predict()
dataset

"""---

# <font color=green>3 CORRELAÇÃO</font>
***

## <font color=green>3.1 Covariância</font>
***

A covariância, ou variância conjunta, é a medida do grau de interdependência (ou inter-relação) numérica entre duas variáveis. É definida da seguinte maneira:

### Covariância populacional

# $$\sigma_{xy} = \frac 1n\sum_{i=1}^{n}(X_i-\mu_x)(Y_i-\mu_y)$$

### Covariância amostral

# $$S_{xy} = \frac 1{n-1}\sum_{i=1}^{n}(X_i-\bar{X})(Y_i-\bar{Y})$$

### Gerando uma amostra aleatória para facilitar o entendimento
"""

amostra = dados.query('Renda < 5000').sample(n = 20, random_state = 101)

"""### Obtendo a matriz de covariância"""

# O método pandas .cov gera a matriz de covariância, que é utilizada para o cálculo do Coeficiente de correlação de Pearson.
# Devemos construir a matriz de covariância utilizando variáveis contínuas.
# Quando temos um número positivo significa que quanto x aumenta y tende também a aumentar. Uma cov negativa significa o inverso.
# Quando a cov se aproxima de zero podemos intender que não existe uma relação forte de correlação entre as duas variáveis.
amostra[['Idade', 'Renda', 'Anos de Estudo', 'Altura']].cov()

"""### Identificando as variâncias na diagonal principal da matriz"""

amostra.Idade.var()

"""## <font color=green>3.2 Interpretação da Covariância</font>
***

Valor de $S_{xy}$ positivo indica uma associação linear positiva entre x e y, ou seja, à medida que o valor de x aumenta, o valor de y também aumenta. Neste caso, podemos ver na figura abaixo que os pontos que têm a maior influência sobre $S_{xy}$ devem estar nos quadrantes I e III.

Se o valor de $S_{xy}$ for negativo temos um indicativo de associação linear negativa entre x e y, ou seja, à medida que x aumenta, o valor de y diminui. Neste caso, podemos ver na figura abaixo que os pontos que têm a maior influência sobre $S_{xy}$ devem estar nos quadrantes II e IV.

Finalmente, se os pontos estiverem uniformemente distribuídos pelos quadrantes, o valor de $S_{xy}$ se aproximará de zero, indicando que não existe nenhuma associação linear entre x e y.

<img src="https://caelum-online-public.s3.amazonaws.com/1273-estatistica-parte4/01/img026.png" width=50%>

### Verificando a existência de uma associação linear negativa
"""

# Avaliando a cov entre as variáveis Renda e Idade podemos ver um valor sendo puxado para o negativo, indicado que não existe uma correlação positiva entre as duas variáveis, ou seja
# a tendência é que o aumento de uma tende a diminuir a outra do BD.

x = amostra.Renda
y = amostra.Idade

ax = sns.scatterplot(x, y)
ax.figure.set_size_inches(10, 6)
ax.hlines(y = y.mean(), xmin = x.min(), xmax = x.max(), colors='black', linestyles='dashed')
ax.vlines(x = x.mean(), ymin = y.min(), ymax = y.max(), colors='black', linestyles='dashed')

"""### Verificando a existência de uma associação linear positiva"""

# Na analise da Renda e de Anos de Estudo observamos uma cov positiva que puxa o gráfico para o lado positivo também, indicando que o aumento de uma variável leva ao aumento da outra.

x = amostra.Renda
y = amostra['Anos de Estudo']

ax = sns.scatterplot(x, y)
ax.figure.set_size_inches(10, 6)
ax.hlines(y = y.mean(), xmin = x.min(), xmax = x.max(), colors='black', linestyles='dashed')
ax.vlines(x = x.mean(), ymin = y.min(), ymax = y.max(), colors='black', linestyles='dashed')

"""### Verificando a inexistência de uma associação linear entre as variáveis"""

# O gráfico nulo de cov indica uma não correlação entre as variáveis Idade e Altura.

x = amostra.Idade
y = amostra.Altura

ax = sns.scatterplot(x, y)
ax.figure.set_size_inches(10, 6)
ax.hlines(y = y.mean(), xmin = x.min(), xmax = x.max(), colors='black', linestyles='dashed')
ax.vlines(x = x.mean(), ymin = y.min(), ymax = y.max(), colors='black', linestyles='dashed')

"""### <font color='red'>Observação Importante:</font>
> Pelo que foi apresentado pode parecer que valores elevados, tanto positivos quanto negativos, para a covariância indicam relações lineares fortes entre as variáveis envolvidas. No entanto, um problema quando se usa a covariância como uma medida da intensidade da relação linear é que o valor da covariância depende das unidades de medida para x e y.
> 
> Uma medida da relação entre duas variáveis que não é afetada pelas unidades de medida para x e y é o coeficiente de correlação que veremos no próximo tópico.

## <font color=green>3.3 Coeficiente de correlação de Pearson</font>
***

É obtido dividindo-se a covariância da população ou amostra pelo produto do desvio padrão populacional ou amostral de x pelo desvio padrão populacional ou amostral de y.

O coeficiente de correlação varia de -1 a +1. Valores que se aproximam de -1 ou +1 indicam uma relação linear forte. Quanto mais próxima a correlação estiver de zero, mais fraca será a relação.

Um ponto importante é que o coeficiente de correlação é uma medida de associação linear e não necessariamente de causação. Uma correlação alta entre duas variáveis não significa, necessariamente, que variações em uma delas provocará alterações na outra.

### Coeficiente de correlação de Pearson - dados populacionais

# $$\rho_{xy} = \frac{\sigma_{xy}}{\sigma_{x}\sigma_{y}}$$

### Coeficiente de correlação de Pearson - dados amostrais

# $$r_{xy} = \frac{s_{xy}}{s_{x}s_{y}}$$

Onde

$\sigma_{xy}$ = covariância populacional entre x e y

$s_{xy}$ = covariância amostral entre x e y

$\sigma_{x}$ e $\sigma_{y}$ = desvios padrão populacionais de x e y, respectivamente

$s_{x}$ e $s_{y}$ = desvios padrão amostrais de x e y, respectivamente

### Obtendo $s_{xy}$
"""

# Obtendo a covariância

s_xy = dados[['Altura', 'Renda']].cov()
s_xy

# Filtrando o valor da covariância na matriz

s_xy= s_xy.Altura.loc['Renda']
s_xy

"""### Obtendo $s_x$ e $s_y$"""

# Obtendo o desvio padrão de x e y

s_x = dados.Altura.std()
s_y = dados.Renda.std()

"""### Obtendo o coeficiente de correlação $r_{xy}$"""

# Sendo o valor negativo indica uma correlação inversa entre as variáveis, no entando sendo valor próximo a zero podemos dizer que a correlação não possui um laço muito forte.

r_xy = s_xy / ( s_x * s_y)
r_xy

"""### Obtendo uma matriz de correlação com o Pandas"""

# Utilizando o método .corr() do pandas temos de forma direta a relação entre as duas variáveis

dados[['Altura', 'Renda']].corr()

# Avaliando a correlação de Pearson do nosso ds
# Sendo uma valor alto e positivo entendemos que existe uma correlação forte entre as variáveis onde quando uma aumenta a outra aumenta e vice versa,
# o que faz sentivo afinal quando a Renda aumenta é natural o gasto da família também aumentar.

dataset[['Y', 'X']].corr()

# No gráfico anterior podíamos notar uma correlação negativa entre as variáveis Renda e Altura, porém não podiamos determinar sua intensidade, porém
# com o método .corr() de Pearson conseguimos medir que trata-se de uma relação fraca próxima a zero.

x = amostra.Renda
y = amostra.Altura

ax = sns.scatterplot(x, y)
ax.figure.set_size_inches(10, 6)
ax.hlines(y = y.mean(), xmin = x.min(), xmax = x.max(), colors='black', linestyles='dashed')
ax.vlines(x = x.mean(), ymin = y.min(), ymax = y.max(), colors='black', linestyles='dashed')

# Comparando os resultados do nosso ds em relação a Renda e o Gasto da famímilia percebemos uma relação forte com .corr() positivo, que gera uma gráfico bem definido.

x = dataset.Y
y = dataset.X

ax = sns.scatterplot(x, y)
ax.figure.set_size_inches(10, 6)
ax.hlines(y = y.mean(), xmin = x.min(), xmax = x.max(), colors='black', linestyles='dashed')
ax.vlines(x = x.mean(), ymin = y.min(), ymax = y.max(), colors='black', linestyles='dashed')

# Exercício:

import numpy as np

sigma_XY_exer = 2178803.59
sigma_X_2_exer = 7328865.85
sigma_Y_2_exer = 667839.78

sigma_X_exer = np.sqrt(sigma_X_2_exer)
sigma_Y_exer = np.sqrt(sigma_Y_2_exer)

r_XY_exer = sigma_XY_exer / (sigma_X_exer * sigma_Y_exer)
print('Correlação ->', r_XY_exer.round(4))

"""---

# <font color=green>4 REGRESSÃO LINEAR</font>
***

A análise de regressão diz respeito ao estudo da dependência de uma variável (a variável dependente) em relação a uma ou mais variáveis, as variáveis explicativas ou independentes, visando estimar e/ou prever o valor médio da primeira em termos dos valores conhecidos ou fixados das segundas.

#### Terminologia

> A variável que é prevista é conhecida como variável dependente (*Y*).

> A variável utilizada para prever o valor da variável dependente é conhecida como variável independente (*X*).

Em nosso treinamento vamos abordar o tipo mais simples de análise de regressão que considera uma variável dependente e apenas uma variável independente onde a relação entre as variáveis se aproxima de uma linha reta.

## <font color=green>4.1 Regressão linear simples</font>
***

### Função consumo

Um economista famoso do passado concluiu em um de seus estudos que os indivíduos tendem a aumentar o seu consumo conforme sua renda aumenta. Logicamente esta teoria ganhou um pouco mais de complexidade, mas vamos utilizar sua forma mais simples para entender o procedimento de análise de regressão com a seguninte formulação:

# $$Y_i = \beta_1 + \beta_2X_i$$

Onde

- $Y_i$ é o gasto das famílias ou consumo das famílias

- $X_i$ é a renda disponível

- $\beta_1$ é conhecido como intercepto (no modelo teórico acima é conhecido como consumo autônomo, ou seja, o consumo quando o rendimento é zero)

- $\beta_2$ é o coefiente angular (no modelo teórico é a propensão marginal a consumir)

Em uma análise de regressão linear simples, o interesse está em estimar a função de regressão populacional como a apresentada acima, ou seja, estimar os valores dos parâmetros $\beta_1$ e $\beta_2$ com base nas observações de $Y$ e $X$.

### Carregando o dataset
"""

# DS modelo de estudo

dataset = {
    'Y': [3011, 1305, 1879, 2654, 2849, 1068, 2892, 2543, 3074, 849, 2184, 2943, 1357, 2755, 2163, 3099, 1600, 353, 1778, 740, 2129, 3302, 2412, 2683, 2515, 2395, 2292, 1000, 600, 1864, 3027, 1978, 2791, 1982, 900, 1964, 1247, 3067, 700, 1500, 3110, 2644, 1378, 2601, 501, 1292, 2125, 1431, 2260, 1770],
    'X': [9714, 3728, 6062, 8845, 8378, 3338, 8507, 7947, 9915, 1632, 6825, 8918, 4100, 9184, 6180, 9997, 4500, 1069, 5925, 2466, 6083, 9712, 7780, 8383, 7185, 7483, 7640, 2100, 2000, 6012, 8902, 5345, 8210, 5662, 2700, 6546, 2900, 9894, 1500, 5000, 8885, 8813, 3446, 7881, 1164, 3401, 6641, 3329, 6648, 4800]
}

dataset = pd.DataFrame(dataset)
dataset.head()

"""### Identificando a relação entre as variáveis

https://seaborn.pydata.org/generated/seaborn.lmplot.html

Plota a reta de regressão entre duas variáveis juntamente com a dispersão entre elas.
"""

# Avaliando inicialmente de forma gráfica se existe uma relação entre as duas variáveis

ax = sns.lmplot(x="X", y="Y", data=dataset)
ax.fig.set_size_inches(12, 6)
ax.fig.suptitle('Reta de Regressão - Gasto X Renda', fontsize=16, y=1.02)
ax.set_xlabels("Renda das Famílias", fontsize=14)
ax.set_ylabels("Gasto das Famílias", fontsize=14)
ax

"""### Matriz de correlação"""

# Aplicado o método .corr() identificamos que númericamente a relação linear entre as duas variáveis é realmente muito forte. 
# Sendo os limites do método entre 1 e -1 confirmamos essa forte relação.

dataset.corr()

"""### Função de regressão populacional

A equação formulada acima é conhecida como **função de regressão populacional (FRP)** e em alguns livros é também representada da seguinte forma:

# $$E(Y|X_i) = \beta_1 + \beta_2X_i$$

Ela afirma que o valor esperado da distribuição de $Y$, dado $X_i$, tem uma relação funcional com $X_i$, isto é, a resposta média de $Y$ varia com $X$. O coeficientes $\beta_1$ e $\beta_2$ são conhecidos como coeficientes de regressão e também são conhecidos como intercepto e coeficiente angular, respectivamente.

<img src="https://caelum-online-public.s3.amazonaws.com/1273-estatistica-parte4/01/img027.png" width=50%>

O gráfico de dispersão acima deixa claro que com o aumento da renda familiar, em média, as despesas de consumo das famílias aumentam, mas não no mesmo nível. O que podemos dizer é que para um nível de renda $X_i$ as despesas médias de consumo de uma
família agrupam-se em torno do consumo médio de todas as famílias deste nível $X_i$, isto é, em torno de sua esperança condicional $E(Y|X_i)$. Portanto, podemos expressar o desvio individual de $Y_i$ em torno de seu valor esperado da seguinte forma:

# $$u_i = Y_i - E(Y|X_i)$$

ou

# $$Y_i = E(Y|X_i) + u_i$$

onde o desvio $u_i$ é uma variável aleatória não-observável que assume valores positivos ou negativos. Esta variável é também cohecida como termo de erro estocástico.

Observe que a podemos representar a FRP em sua forma estocástica da seguinte maneira:

# $$Y_i = \beta_1 + \beta_2X_i + u_i$$

## <font color=green>4.2 O método de mínimos quadrados</font>
***

Considere a seguinte **função de regressão da população (FRP)** para duas variáveis:

# $$Y_i = \beta_1 + \beta_2X_i + u_i$$

Como a **FRP** não pode ser obtida de forma direta, precisamos estimá-la através da **função de regressão amostral (FRA)**.

# $$Y_i = \hat{\beta}_1 + \hat{\beta}_2X_i + \hat{u}_i$$
# $$Y_i = \hat{Y}_i + \hat{u}_i$$

onde $\hat{Y}_i$ é o valor estimado de $Y_i$.

A partir da equação acima podemos expressar o erro da seguinte maneira:

# $$\hat{u}_i = Y_i - \hat{Y}_i$$
# $$\hat{u}_i = Y_i - \hat{\beta}_1 - \hat{\beta}_2X_i$$

A ideia é determinar **FRA** de forma que fique o mais próximo possível do valor observado de $Y$. Intuitivamente uma forma interessante de fazer isso seria determinar **FRA** de maneira que a soma dos resíduos seja a menor possível.

# $$\sum\hat{u}_i = \sum{(Y_i - \hat{Y}_i)}$$

Avaliando a figura abaixo se pode verificar que talvez o critério de minimizar a soma dos resíduos não seja a melhor abordagem para solucionar o problema.

<img src="https://caelum-online-public.s3.amazonaws.com/1273-estatistica-parte4/01/img015.png" width=50%>

O critério de minimização da soma dos resíduos assume que todos os resíduos tem o mesmo peso no somatório, o que nem sempre se comprova. Em nosso exemplo os resíduos $\hat{u}_1$ e $\hat{u}_4$ encontram-se bem mais afastados da **FRA** que $\hat{u}_2$ e $\hat{u}_3$. Isso acarreta na possibilidade de que a soma dos $\hat{u}_i$'s seja bastante pequena e até mesmo nula, mesmo que os resíduos estejam muito dispersos em relação a reta de regressão.

Para evitar tal problema adotou-se o critério de minimização da soma dos quadrados dos resíduos que é conhecido como **Método de Mínimos Quadrados**.

# $$\sum\hat{u}_i^2 = \sum{(Y_i - \hat{Y}_i)^2}$$
# $$\sum\hat{u}_i^2 = \sum{(Y_i - \hat{\beta}_1 - \hat{\beta}_2X_i)^2}$$

Após um procedimento de diferenciação, algumas simplificações e manipulações algébricas obtemos os **estimadores de mínimos quadrados**.

# $$
\begin{equation}
\boxed{\hat{\beta}_2 = \frac{n\sum{X_iY_i} - \sum{X_i}\sum{Y_i}}{n\sum{X_i^2} - (\sum{X_i})^2}}
\end{equation}
$$

# $$
\begin{equation}
\boxed{
\begin{eqnarray}
\hat{\beta}_1 &=& \frac{\sum{X_i^2}\sum{Y_i} - \sum{X_i}\sum{X_iY_i}}{n\sum{X_i^2} - (\sum{X_i})^2}\\
&=& \bar{Y} - \hat{\beta}_2\bar{X}
\end{eqnarray}
}
\end{equation}
$$

## <font color=green>4.3 Estimadores de mínimos quadrados ordinários</font>
***

### Obter $n$
"""

# Obtendo o tamanho n do ds
n = len(dataset)
n

"""### Obter $\sum{Y}$"""

# Somando os resultados da variável Y
SOMA_Y = dataset.Y.sum()
SOMA_Y

"""### Obter $\sum{X}$"""

# Somando os resultados da variável X
SOMA_X = dataset.X.sum()
SOMA_X

"""### Obter $\sum{X^2}$"""

# Para obtermos o somatório da variável x ao quadrado, inicialmente criamos uma coluna no ds com o valor de x ao quadrado
dataset['X2'] = dataset.X ** 2
dataset.head()

# Após a criação da coluna fazemos a soma para obter a soma dos quadrados de X
SOMA_X2 = dataset.X2.sum()
SOMA_X2

# Uma forma mais simples para obter a soma do quadrado de X é utilizando o método apply do Pandas com lambda como abaixo
SOMA_X2 = dataset.X.apply(lambda x: x**2).sum()
SOMA_X2

"""### Obter $\sum{Y^2}$"""

# Da mesma forma obtemos a soma dos quadrados de Y
SOMA_Y2 = dataset.Y.apply(lambda y: y**2).sum()
SOMA_Y2

"""### Obter $\sum{XY}$"""

# Obtendo o somatório do produto de X e Y
# Primeiro criamos a coluna com o produto das duas variáveis
dataset['XY'] = dataset.X * dataset.Y
dataset.head()

# Somando a coluna XY temos a soma dos produtos das variáveis.
SOMA_XY = dataset.XY.sum()
SOMA_XY

# Utilizando o mesmo método .apply conseguimos o somatório do produto das variáveis
SOMA_XY = dataset.apply(lambda data: data.X * data.Y, axis = 1).sum()
SOMA_XY

# Apagando as colunas desnecessárias criadas no ds
dataset.drop(['XY'], axis = 1, inplace = True)
dataset.head()

"""### Obter $\hat{\beta}_2$

# $$\hat{\beta}_2 = \frac{n\sum{X_iY_i} - \sum{X_i}\sum{Y_i}}{n\sum{X_i^2} - (\sum{X_i})^2}$$
"""

# Calculando o valor de beta 2
numerador = n * SOMA_XY - SOMA_X * SOMA_Y
denominador = n * SOMA_X2 - (SOMA_X)**2
beta_2 = numerador / denominador
beta_2

"""### Obter $\hat{\beta}_1$

# $$
\begin{eqnarray}
\hat{\beta}_1 &=& \frac{\sum{X_i^2}\sum{Y_i} - \sum{X_i}\sum{X_iY_i}}{n\sum{X_i^2} - (\sum{X_i})^2}\\
&=& \bar{Y} - \hat{\beta}_2\bar{X}
\end{eqnarray}
$$ 
"""

# Calculando o valor de beta 1
beta_1 = dataset.Y.mean() - beta_2 * dataset.X.mean()
beta_1

"""### Obtendo a estimativa dos parâmetros com o StatsModels

### Importando a biblioteca
https://www.statsmodels.org/stable/index.html
"""

import statsmodels.api as sm

Y = dataset.Y
X = sm.add_constant(dataset.X)

Y.head()

# com o método sm.add_constant, adicionamos ao ds uma coluna com a constante 1
X.head()

"""### Estimando o modelo"""

resultado_regressao = sm.OLS(Y, X, missing='drop').fit()

"""### Visualizando os parâmetros estimados"""

beta_1

beta_2

# Com o método sm.OLS e o .params temos de forma simplificada dos valores de beta_1 e beta_2
resultado_regressao.params

beta_1 = resultado_regressao.params[0]
beta_1

beta_2 = resultado_regressao.params[1]
beta_2

"""### Intervalo de confiança para os parâmetros estimados"""

# O método .conf_int é utilizado para determinar os parâmetros de confiança
resultado_regressao.conf_int(alpha=0.05)

"""### Exercício | C03 A07"""

dsex0307 = {
    'Y': [670, 220, 1202, 188, 1869, 248, 477, 1294, 816, 2671, 1403, 1586, 3468, 973, 701, 5310, 10950, 2008, 9574, 28863, 6466, 4274, 6432, 1326, 1423, 3211, 2140], 
    'X': [1.59, 0.56, 2.68, 0.47, 5.2, 0.58, 1.32, 3.88, 2.11, 5.53, 2.6, 2.94, 6.62, 1.91, 1.48, 10.64, 22.39, 4.2, 21.9, 59.66, 14.22, 9.57, 14.67, 3.28, 3.49, 6.94, 6.25]
}

dsex0307 = pd.DataFrame(dsex0307)

Yex0307 = dsex0307.Y
Xex0307 = sm.add_constant(dsex0307.X)

resultado_regressaoex0307 = sm.OLS(Yex0307, Xex0307, missing='drop').fit()

resultado_regressaoex0307.params

"""## <font color=green>4.4 Obtendo previsões</font>
***

# $$\hat{Y}_i = 207,9033 + 0,2973X_i$$

### Previsões dentro da amostra
"""

dataset['Y_previsto'] = beta_1 + beta_2 * dataset.X
dataset.head(10)

"""### Utilizando o statsmodels"""

# Utilizando o statsmodels temos os números previstos de Y de forma simplificada
dataset['Y_previsto_statsmodels'] = resultado_regressao.predict()
dataset.head(10)

# Removendo a coluna do sm
dataset.drop(['Y_previsto_statsmodels'], axis = 1, inplace = True)
dataset.head()

"""### Estimando o 'Gasto das Famílias' fora da amostra"""

# Criando uma função py para determinar o valor de y com um valor de x
def prever(x):
  return beta_1 + beta_2 * x

# Com a entrada do valor de x (renda da família), o modelo preve o y (gasto médio da família)
prever(7510)

"""### Estimando o 'Gasto das Famílias' fora da amostra via StatsModels"""

# Com o sm temos o mesmo valor de previsão mas forma simplificada
resultado_regressao.predict([1, 7510])[0]

"""### Exercício | C03 A09"""

dsex0309 = {
    'Y': [670, 220, 1202, 188, 1869, 248, 477, 1294, 816, 2671, 1403, 1586, 3468, 973, 701, 5310, 10950, 2008, 9574, 28863, 6466, 4274, 6432, 1326, 1423, 3211, 2140], 
    'X': [1.59, 0.56, 2.68, 0.47, 5.2, 0.58, 1.32, 3.88, 2.11, 5.53, 2.6, 2.94, 6.62, 1.91, 1.48, 10.64, 22.39, 4.2, 21.9, 59.66, 14.22, 9.57, 14.67, 3.28, 3.49, 6.94, 6.25]
}

dsex0309 = pd.DataFrame(dsex0307)

Yex0309 = dsex0309.Y
Xex0309 = sm.add_constant(dsex0309.X)

resultado_regressaoex0309 = sm.OLS(Yex0309, Xex0309, missing='drop').fit()

beta_1ex0309 = resultado_regressaoex0309.params[0]
beta_1ex0309

beta_2ex0309 = resultado_regressaoex0309.params[1]
beta_2ex0309

resultado_regressaoex0309.predict([1, 2.345678])[0]

"""## <font color=green>4.5 Resíduos</font>
***

Como vimos anteriormente, o resíduo da i-ésima observação é a diferença entre o valor observado de nossa variável dependente ($Y_i$) e o valor estimado da variável dependente ($\hat{Y}_i$).

# $$\hat{u}_i = Y_i - \hat{Y}_i$$

Em outras palavras, $\hat{u}_i$ é o erro obtido ao se utilizar a equação de regressão estimada para prever o valor da variável dependente.
"""

dataset['u'] = dataset.Y - dataset.Y_previsto
dataset.head()

# Utilizando o método .resid do sm criamos de forma simples a diferença entre o y e o y_previsto
dataset['Residuos'] = resultado_regressao.resid
dataset.head()

# Rodando .drop para manter apenas a coluna criada pelo sm
dataset.drop(['u'], axis = 1, inplace = True)
dataset.head()

dataset.Residuos.mean()

"""## <font color=green>4.6 Suposições sobre o termo de erro $u$</font>
***

### 1. O termo de erro $u$ é uma variável aleatória com média igual a zero: $E(u) = 0$
### 2. A variância de $u$ é a mesma para todos os valores de $X$
### 3. O valores de $u$ são independentes
### 4. O termo de erro $u$ é uma variável aleatória normalmente distribuída.

### Plotando os resíduos do modelo

https://seaborn.pydata.org/generated/seaborn.scatterplot.html
"""

ax = sns.scatterplot(x=dataset.X, y=dataset.Residuos)
ax.figure.set_size_inches(12, 6)
ax.set_title('Resíduos vs Variável Independente', fontsize=18)
ax.set_xlabel('X', fontsize=14)
ax.set_ylabel('Resíduos', fontsize=14)
ax

ax = sns.scatterplot(x=dataset.Y_previsto, y=dataset.Residuos)
ax.figure.set_size_inches(12, 6)
ax.set_title('Resíduos vs Y_Previsto', fontsize=18)
ax.set_xlabel('Y_Previsto', fontsize=14)
ax.set_ylabel('Resíduos', fontsize=14)
ax

"""### Hipótese de variância constante

<img src="https://caelum-online-public.s3.amazonaws.com/1273-estatistica-parte4/01/img028.jpg" width=80%>
Fonte: Econometria Básica - 5ª edição - Gujarati e Porter
"""

# Através da análise gráfica determinamos que os valores se distribuem de uma maneira constante
ax = sns.scatterplot(x=dataset.Y_previsto, y=dataset.Residuos**2)
ax.figure.set_size_inches(12, 6)
ax.set_title('Resíduos² vs Y_Previsto', fontsize=18)
ax.set_xlabel('Y_Previsto', fontsize=14)
ax.set_ylabel('Resíduos', fontsize=14)
ax

"""## <font color=green>4.7 O coeficiente de determinação $R^2$</font>
***

O **coeficiente de determinação R²** é uma medida resumida que diz quanto a linha de regressão amostral se ajusta aos dados. Pode ser obtido a partir da seguinte fórmula:

# $$R^2 = \frac{\big[\sum{(Y_i - \bar{Y})(\hat{Y}_i - \bar{Y})}\big]^2}{\sum{(Y_i - \bar{Y}})^2 \sum{(\hat{Y}_i - \bar{Y}})^2}$$

Sabemos que o i-ésimo resíduo representa o erro de usarmos $\hat{Y}_i$ para estimar $Y_i$. A soma dos quadrados desses resíduos é o valor que é minimizado pelo método dos mínimos quadrados. Esse valor pode ser representado da seguinte forma:

# $$SQE = \sum{(Y_i - \hat{Y}_i)^2}$$

O valor da SQE é uma medida do erro de se usar a equação de regressão estimada para estimar os valores da variável dependente na amostra.

Outro componente que podemos medir é a soma dos quadrados total (SQT) que representa a medida do erro envolvido no uso da média ($\bar{Y}$) para fazer as estimativas. A SQT pode ser representada da forma abaixo:

# $$SQT = \sum{(Y_i - \bar{Y})^2}$$

Para quantificar o quanto os valores estimados ($\hat{Y}_i$) se afastam da média ($\bar{Y}$) podemos obter mais uma soma de quadrados. Essa soma é chamada de soma dos quadrados da regressão (SQR) e é representada pela seguinte fórmula:

# $$SQR = \sum{(\hat{Y}_i - \bar{Y})^2}$$

### Soma do quadrados do erros (SQE)
"""

dataset.head()

SQE = dataset.Residuos.apply(lambda u: u**2).sum()
SQE

# Utilizando o método .ssr (sum of square residuals) utilizamos o sm para obter de forma simples o SQE
resultado_regressao.ssr

"""### Soma do quadrados total (SQT)"""

SQT = dataset.Y.apply(lambda y: (y - dataset.Y.mean())**2).sum()
SQT

"""### Soma do quadrados da regressão (SQR)"""

SQR = dataset.Y_previsto.apply(lambda y: (y - dataset.Y.mean())**2).sum()
SQR

# Utilizando o ess (explained sum of squares) utilizamos o sm para obter de forma simples o SQR
resultado_regressao.ess

"""### Relação entre as somas de quadrados

# $$SQT = SQR + SQE$$

Onde,


### $SQE = \sum{(Y_i - \hat{Y}_i)^2}$

### $SQT = \sum{(Y_i - \bar{Y})^2}$

### $SQR = \sum{(\hat{Y}_i - \bar{Y})^2}$


<img src="https://caelum-online-public.s3.amazonaws.com/1273-estatistica-parte4/01/img029.png" width=50%>
"""



"""### Coeficiente de determinação (R²)

A regressão estimada teria um ajuste perfeito se todos os valores da variável dependente ($Y_i$) estiverem sobre a reta de regressão estimada. Quando isso ocorre temos $Y_i - \hat{Y}_i = 0$ para todas as observações, o que resulta em uma $SQE = 0$. Como $SQT=SQR+SQE$, é possível deduzir que para termos um ajuste perfeito $SQT$ deve ser igual a $SQR$ e a razão entre estas medidas ($\frac{SQR}{SQT}$) deve ser igual a 1.

Quando o ajuste não é tão perfeito nota-se que a $SQE$ apresenta valores maiores o que faz a razão $\frac{SQR}{SQT}$ diminuir, e em uma situação de total imperfeição do ajuste teríamos uma $SQR=0$ e $SQE=SQT$ levando a $\frac{SQR}{SQT}=0$.

A razão $\frac{SQR}{SQT}$, que assume valores entre 0 e 1, é utilizada como medida de eficiência do ajuste da equação de regressão estimada. Essa medida é conhecida como coeficiente de determinação (R²).

# $$R^2 = \frac{SQR}{SQT}$$

## <font color='red'>Observação</font>
> Somente com a utilização do R² não é possível tirar conclusões sobre a relação entre $Y$ e $X$ ser ou não ser estatisticamente
significativa. Este tipo de afirmação deve basear-se em considerações que envolvem o tamanho da amostra e as propriedades da distribuição amostral dos estimadores mínimos quadrados.
"""

R2 = SQR / SQT
R2

# Utilizando o método .rsquared temos o R2
resultado_regressao.rsquared

"""### Exercício | C04 A06"""

# Aplicando os resultados do exercício anterior temos:
resultado_regressaoex0309.rsquared

"""## <font color=green>4.8 Testes aplicados a modelos de regressão</font>
***

Como vimos, em uma regressão linear simples, a média da variável dependente ($Y$) é uma função linear da variável independente ($X$):

# $$Y_i = \beta_1 + \beta_2X_i$$

Se o valor de $\beta_2$ for zero podemos verificar que o valor médio de $Y$ não depende do valor de $X$ e, portanto, concluímos que $X$ e $Y$ não estão linearmente relacionados. De forma alternativa, se o valor de $\beta_2$ não for igual a zero, concluímos que as duas variáveis estão relacionadas.

Para testar se a relação de regressão é significativa, é preciso realizar um **teste de hipóteses** para determinar se o valor de $\beta_2$ é zero. Antes de realizar este tipo de teste precisamos obter uma estimativa para $\sigma^2$ (variância do erro).

### Output do modelo de regressão estimado
"""

print(resultado_regressao.summary())

"""### Erro quadrático médio - estimativa de $\sigma^2$

Lembre-se que a **soma dos quadrados do erros (SQE)** é uma medida numérica da variabilidade dos dados observados em torno da reta de regressão estimada. Todas as somas de quadrados, estudadas anteriormente, estão associadas a um determinado número de graus de liberdade. No caso da SQE, como devem ser estimados dois parâmetros, temos $n-2$ graus de liberdade.

O **erro quadrático médio**, representado pela equação abaixo, pode ser obtido dividindo-se a SQE por $n-2$ graus de liberdade.

# $$EQM = \frac{SQE}{n-2}$$
"""

SQE

n

EQM = SQE / (n - 2)
EQM

# Com o método .mse_resid do sm obtemos o erro quadrático médio
EQM = resultado_regressao.mse_resid
EQM

"""### Teste de hipótese para nulidade do coeficiente angular

Considere o seguinte modelo de regressão linear simples:

# $$Y_i = \beta_1 + \beta_2X_i + u_i$$

Se as variáveis $Y$ e $X$ são linearmente relacionadas, espera-se que $\beta_2$ seja diferente de zero. Para testar esta hipótese formulamos um teste de hipótese com a seguinte especificação de hipóteses nula e alternativa:

## $H_0: \beta_2 = 0$
## $H_1: \beta_2 \neq 0$

Caso $H_0$ seja rejeitada, concluiremos que existe uma relação linear estatisticamente significativa entre as duas variáveis.

Considere agora que $b_1$ e $b_2$ são nossos estimadores de mínimos quadrados. Considere que a distribuição amostral de $b_2$ segue uma normal e também as seguintes propriedades:

# $$E(b_2) = \beta_2$$
# $$\sigma_{b_2} = \frac{\sigma}{\sqrt{\sum{(X_i - \bar{X})^2}}}$$

Como não conhecemos o valor de $\sigma$, utilizamos $s$ como estimativa:

# $$s_{b_2} = \frac{s}{\sqrt{\sum{(X_i - \bar{X})^2}}}$$

Note que o valor esperado de $b_2$ é $\beta_2$, logo, $b_2$ é um estimador não viesado de $\beta_2$. Abaixo temos a estatística de teste (t) que segue uma distribuição t de Student com $n-2$ graus de liberdade.

# $$t = \frac{b_2 - \beta_2}{s_{b_2}}$$

### Calculando $s$
"""

s = np.sqrt(resultado_regressao.mse_resid)
s

"""### Calculando $\sum{(X_i - \bar{X})^2}$"""

SOMA_DESVIO2 = dataset.X.apply(lambda x: (x - dataset.X.mean())**2).sum()
SOMA_DESVIO2

"""### Calculando $s_{b_2}$"""

s_beta_2 = s / np.sqrt(SOMA_DESVIO2)
s_beta_2

"""### Determinando as áreas de aceitação e rejeição de $H_0$"""

from scipy.stats import t as t_student

"""![Região de Aceitação](https://caelum-online-public.s3.amazonaws.com/1273-estatistica-parte4/01/img031.png)

### Níveis de confiança e significância
"""

confianca = 0.95
significancia = 1 - confianca

graus_de_liberdade = resultado_regressao.df_resid
graus_de_liberdade

"""### Obtendo $t_{\alpha/2}$"""

probabilidade = (0.5 + (confianca / 2))
probabilidade

t_alpha_2 = t_student.ppf(probabilidade, graus_de_liberdade)
t_alpha_2

"""![Região de Aceitação](https://caelum-online-public.s3.amazonaws.com/1273-estatistica-parte4/01/img032.png)

### Obtendo $t = \frac{b_2 - \beta_2}{s_{b_2}}$
"""

t = (beta_2 - 0) / s_beta_2
t

resultado_regressao.tvalues[1]

"""![Região de Aceitação](https://caelum-online-public.s3.amazonaws.com/1273-estatistica-parte4/01/img033.png)

### Etapas e regras de decisão do teste t de significância dos parâmetros

<img src="https://caelum-online-public.s3.amazonaws.com/1273-estatistica-parte4/01/img030.png" width=90%>

### <font color='red'>Critério do valor crítico</font>

> ### Teste Bicaudal
> ### Rejeitar $H_0$ se $t \leq -t_{\alpha / 2}$ ou se $t \geq t_{\alpha / 2}$
"""

t <= -t_alpha_2

# Rejeitamos a hipótese nula
t >= t_alpha_2

"""### <font color='red'>Critério do $p-valor$</font>

> ### Teste Bicaudal
> ### Rejeitar $H_0$ se o valor $p\leq\alpha$
"""

p_valor = 2 * (t_student.sf(t, graus_de_liberdade))
p_valor

p_valor = resultado_regressao.pvalues[1]
p_valor

# Rejeitamos a hipótese nula de que beta_2 é igual a 0
p_valor <= significancia

"""### <font color='green'>Conclusão: Rejeitamos $H_0$ e concluímos que existe uma relação significativa entre as duas variáveis.</font>"""

print(resultado_regressao.summary())

"""---

### Teste F

O teste F também é uma ferramenta para testar a significância na regressão. Baseado na distribuição F de probabilidade, o teste F é utilizado para verificar a significância global na regressão, isto é, em uma regressão múltipla, onde existe mais de uma variável independente, o teste F verifica a nulidade de todos os parâmetros do modelo conjuntamente.

Em nosso caso (regressão linear simples) ele fornece a mesma conclusão obtida com o teste t.

**Hipóteses:**

## $H_0: \beta_2 = 0$
## $H_0: \beta_2 \neq 0$

**Estatística de teste:**

# $$F = \frac{\frac{SQR}{k}}{\frac{SQE}{n-k-1}}$$

Onde,

$SQR$ - soma dos quadrados da regressão

$SQE$ - soma dos quadrados dos erros

$k$ - total de variáveis independentes ($X$)

**Regras de rejeição de $H_0$:**

**Critério do valor crítico** $\rightarrow$ Rejeitar se $F \geq F_{\alpha}$

Onde,

$F_{\alpha}$ - baseia-se na distribuição F com $k$ graus de liberdade no numerador e $n-k-1$ no denominador.

**Critério do p-valor** $\rightarrow$ Rejeitar se $p-valor \leq \alpha$

### Calculando a estatística de teste ($F$)
"""

resultado_regressao.mse_model

resultado_regressao.mse_resid

F = resultado_regressao.mse_model / resultado_regressao.mse_resid
F

# Com o método .fvalue obtemos o F como sm
resultado_regressao.fvalue

"""### Obtendo o p-valor"""

resultado_regressao.f_pvalue

from scipy.stats import f

p_valor = f.sf(F, 1, 48)
p_valor

# Rejeitamos a hipóte nula
p_valor <= 0.05

"""# <font color=green>5 EXTRAS</font>
***

## <font color=green>5.1 Outros testes</font>
***
"""

print(resultado_regressao.summary())

"""### Normalidade dos resíduos - Omnibus

> ### $H_0:$ Os dados se distribuem como uma normal

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html
"""

from scipy.stats import normaltest

statistic, p_valor = normaltest(dataset.Residuos)
print(p_valor)

# Ou seja os dados não se distribuem como uma normal
p_valor <= 0.05

"""https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.probplot.html"""

# Pela dispersão gráfica podemos verificar que não se trata de uma distribuição normal
from scipy.stats import probplot
import matplotlib.pyplot as plt

(_, (_, _, _)) = probplot(dataset.Residuos, plot = plt)

dados.Altura.hist(bins=50)

# Observando os dados de Altura que foram criados dentro de uma distribuição normal, temos o gráfico seguindo exatamente a linha teorica
# o que indica uma têndencia de distribuição normal
(_, (_, _, _)) = probplot(dados.Altura, plot = plt)

"""### Verificando a simetria

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skew.html
"""

from scipy.stats import skew

S = skew(dataset.Residuos)
S

"""### Verificando a curtose

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kurtosis.html
"""

from scipy.stats import kurtosis

C = 3 + kurtosis(dataset.Residuos)
C

"""### Normalidade dos resíduos - Jarque-Bera (statsmodels)

> ### $H_0:$ Os dados se distribuem como uma normal

> ### Estatística de teste
> ### $$JB = \frac{n}{6}(S^2 + \frac{1}{4}(C - 3)^2)$$
> #### Onde,
> #### $n$ - número de observações
> #### $S$ - Coeficiente de assimetria
> #### $C$ - Coeficiente de curtose
"""

JB = (n / 6.) * (S ** 2 + (1 / 4.) * (C - 3) ** 2)
JB

from scipy.stats import chi2

p_valor = chi2.sf(JB, 2)
p_valor

# Rejeitamos a hipótese nula de que os dados se distribuem como uma normal
p_valor <= 0.05

"""### Normalidade dos resíduos - Jarque-Bera (Correção)

> ### $H_0:$ Os dados se distribuem como uma normal

> ### Estatística de teste
> ### $$JB = \frac{n-k}{6}(S^2 + \frac{1}{4}(C - 3)^2)$$
> #### Onde,
> #### $n$ - número de observações
> #### $k$ - número de parâmetros do modelo
> #### $S$ - Coeficiente de assimetria
> #### $C$ - Coeficiente de curtose
"""

JB = (n - 1 / 6.) * (S ** 2 + (1 / 4.) * (C - 3) ** 2)
JB

from scipy.stats import chi2

p_valor = chi2.sf(JB, 2)
p_valor

# Rejeitamos a hipótese nula H0
p_valor <= 0.05