
# <font color=green size=10>CURSO DE ESTATÍSTICA - PARTE 4</font>
***

## Trabalho sobre correlação e regressão

Utilizando os conhecimentos adquiridos em nosso treinamento realize a análise de regressão proposta abaixo.

Siga o roteiro proposto e vá completando as células vazias.

# <font color=green>DATASET DO PROJETO</font>
***

### Fonte: https://www.kaggle.com/dongeorge/beer-consumption-sao-paulo

### Descrição:
A cerveja é uma das bebidas mais democráticas e consumidas no mundo. Não sem razão, é perfeito para quase todas as situações, desde o happy hour até grandes festas de casamento.

Os dados (amostra) foram coletados em São Paulo - Brasil, em uma área universitária, onde existem algumas festas com grupos de alunos de 18 a 28 anos de idade (média).

### Dados:
- **temp_media** - Temperatura Média (°C)
- **consumo** - Consumo de Cerveja (litros)

---

### Solução do problema com dependência do statsmodels
"""

!pip install scipy==1.2 --upgrade

"""### Utilize a célula abaixo para importar as biblioteca que precisar para executar as tarefas
#### <font color='red'>Sugestões: pandas, numpy, scipy, statsmodels</font>
"""

import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import probplot
import matplotlib.pyplot as plt

"""### Importe o dataset"""

dataset = pd.read_csv('dados_projeto.csv', sep=';')

"""### Visualize o conteúdo do DataFrame"""

dataset.shape

dataset.head()

"""### Obtenha e avalie as estatísticas descritivas dos dados"""

dataset.describe()

"""### Análise gráfica
### Construa um box plot para cada variável do dataset
"""

ax = sns.boxplot(data=dataset, x='Y', orient='h', width=0.5)
ax.figure.set_size_inches(12,6)
ax.set_title('Box plot', fontsize=20)
ax.set_xlabel('Consumo de cerveja (litros)', fontsize=16)
ax

ax = sns.boxplot(data=dataset, x='X', orient='h', width=0.5)
ax.figure.set_size_inches(12,6)
ax.set_title('Box plot', fontsize=20)
ax.set_xlabel('Temperatura média', fontsize=16)
ax

"""### Identifique se existe uma relação linear entre as variáveis $Y$ e $X$
### <font color='red'>Utilizando o método gráfico</font>
"""

ax = sns.lmplot(x='X', y='Y', data=dataset)
ax.fig.set_size_inches(12,6)
ax.fig.suptitle('Reta de Regrassão - Temperatura x Consumo de cerveja', fontsize=16, y=1.02)
ax.set_xlabels("Temperatura média", fontsize=14)
ax.set_ylabels("Consumo de cerveja (litros)", fontsize=14)
ax

"""### <font color='red'>Utilizando a matriz de correlação</font>"""

dataset.corr()

"""### Avalie os resultados acima:

É possível afirmar que existe uma relação linear entre as variáveis?

Resp.:

É possível quantificar a intensidade dessa relação?

Resp.:

É possível afirmar que existe uma relação de causalidade entre $Y$ e $X$ a partir dos resultados da matriz de correlação?

Resp.:

### Prepare os dados para estimar um modelo de regressão linear simples
"""

Y = dataset.Y
X = sm.add_constant(dataset.X)

"""### Estime o modelo de regressão linear simples"""

resultado_regressao = sm.OLS(Y, X).fit()

"""### Visualize o resultado da regressão"""

print(resultado_regressao.summary())

"""### Obtenha o $Y$ previsto"""

dataset['Y_previsto'] = resultado_regressao.predict()
dataset.head()

"""### Utilizando nosso modelo estimado para fazer previsões.
### Qual seria o consumo de cerveja para um dia com temperatura média de 42° C?
"""

resultado_regressao.predict([1, 42])[0]

"""### Obtenha os resíduos da regressão"""

dataset['Residuos'] = resultado_regressao.resid
dataset.head()

"""### Plote um gráfico de dispersão dos resíduos da regressão contra o $Y$ previsto"""

ax = sns.scatterplot(x=dataset.Y_previsto, y=dataset.Residuos)
ax.figure.set_size_inches(12, 6)
ax.set_title('Resíduos vs Y_Previsto', fontsize=18)
ax.set_xlabel('Y_Previsto', fontsize=14)
ax.set_ylabel('Resíduos', fontsize=14)
ax

"""### Obtenha o QQPlot dos resíduos"""

(_, (_, _, _)) = probplot(dataset.Residuos, plot=plt)

"""### <font color='red'>A partir dos outputs acima, qual conclusão podemos tirar sobre o comportamento dos resíduos?</font>

### Obtenha o R² da regressão pelo método da soma dos quadrados

# $$R^2 = \frac{SQR}{SQT}$$
"""

SQE = resultado_regressao.ssr
SQE

SQR = resultado_regressao.ess
SQR

SQT = SQR + SQE
SQT

R2 = SQR / SQT
R2

resultado_regressao.rsquared