
# <font color=green size=10>CURSO DE ESTATÍSTICA - PARTE 3</font>

***

## Trabalho sobre testes de hipóteses

Utilizando os conhecimentos adquiridos em nosso treinamento realize o teste de hipóteses proposto abaixo.

Siga o roteiro proposto e vá completando as células vazias. Procure pensar em mais testes interessantes que podem ser realizados com o nosso dataset.

# <font color=green>DATASET DO PROJETO</font>
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

***
***

### Utilize a célula abaixo para importar as biblioteca que precisar para executar as tarefas
#### <font color='red'>Sugestões: pandas, numpy, scipy, statsmodels</font>


import pandas as pd
import numpy as np
from scipy.stats import norm
from statsmodels.stats.weightstats import DescrStatsW, CompareMeans

### Importe o dataset e armazene o conteúdo em uma DataFrame

dados = pd.read_csv('dados.csv')

### Visualize o conteúdo do DataFrame

dados.head()

## <font color='red'>Problema</font>

Você é um pesquisador que estuda o mercado de trabalho brasileiro e resolve estudar as diferenças salariais dos trabalhadores dos estados do Rio de Janeiro e de São Paulo. Durante sua pesquisa você verifica que, aparentemente, os rendimentos dos trabalhadores no estado do Rio de Janeiro são mais baixos que os rendimentos dos trabalhadores no estado de São Paulo. Para confirmar esta conclusão realize um teste de hipótese de comparação de médias em cima de duas amostras de trabalhadores dos dois estados. Siga as seguintes etapas:

- Selecione duas amostras de **500 trabalhadores** para cada um dos dois estados (variável UF) para realizar o teste. Utilize o **parâmetro random_state=101**.
- Considere o **nível de significância de 5%**.
- Teste a hipótese de que a **renda média dos trabalhadores do Rio de Janeiro é menor que a renda média dos trabalhadores de São Paulo**.

---

### Seleção das amostras


rj = dados.query('UF == 33').sample(n = 500, random_state = 101).Renda

sp = dados.query('UF == 35').sample(n = 500, random_state = 101).Renda

### Dados do problema
Obter média e desvio-padrão para as duas amostras


media_amostra_rj = rj.mean()
media_amostra_rj

desvio_padrao_amostra_rj = rj.std()
desvio_padrao_amostra_rj

media_amostra_sp = sp.mean()
media_amostra_sp

desvio_padrao_amostra_sp = sp.std()
desvio_padrao_amostra_sp

significancia = 0.05
confianca = 1 - significancia
n_rj = 500
n_sp = 500
D_0 = 0

## Lembre-se...

<img src='https://caelum-online-public.s3.amazonaws.com/1229-estatistica-parte3/01/img014.png' width=90%>

---

### **Passo 1** - formulação das hipóteses $H_0$ e $H_1$

#### <font color='red'>Lembre-se, a hipótese nula sempre contém a alegação de igualdade</font>

(Formule suas hipóteses aqui)

---

### **Passo 2** - escolha da distribuição amostral adequada

### O tamanho da amostra é maior que 30?
#### Resp.: 

### Podemos afirmar que a população se distribui aproximadamente como uma normal?
#### Resp.: 

### O desvio padrão populacional é conhecido?
#### Resp.:

---

### **Passo 3** - fixação da significância do teste ($\alpha$)


probabilidade = significancia
probabilidade

z_alpha = norm.ppf(probabilidade)
z_alpha.round(2)

---

### **Passo 4** - cálculo da estatística-teste e verificação desse valor com as áreas de aceitação e rejeição do teste


numerador = (media_amostra_rj - media_amostra_sp) - D_0

denominador = np.sqrt((desvio_padrao_amostra_rj ** 2 / n_rj) + (desvio_padrao_amostra_sp ** 2 / n_sp))

z = numerador / denominador

z

---

### **Passo 5** - Aceitação ou rejeição da hipótese nula

### <font color='red'>Critério do valor crítico</font>


z <= z_alpha

### <font color='red'>Critério do valor $p$</font>

### Utilize DescrStatsW


test_rj = DescrStatsW(rj)

test_sp = DescrStatsW(sp)

test_A = test_rj.get_compare(test_sp)

z, p_valor = test_A.ztest_ind(alternative='smaller', value=0)
print('Estatística z ->', z)
print('p-valor ->', p_valor)

### Utilize CompareMeans

test_B = CompareMeans(test_rj, test_sp)

test_B = CompareMeans(test_rj, test_sp)

z, p_valor = test_B.ztest_ind(alternative='smaller', value=0)
print('Estatística z ->', z)
print('p-valor ->', p_valor)

p_valor <= significancia

### <font color='green'>Conclusão: Com um nível de confiança de 95% rejeitamos H0, isto é, concluímos que a renda média no estado do Rio de Janeiro é realmente menor que a renda média no estado de São Paulo.</font>