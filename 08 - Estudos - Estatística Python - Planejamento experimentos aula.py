
<h1 style='color: blue; font-size: 34px; font-weight: bold;'> Planejamento de Experimentos 
</h1>

# <font color='red' style='font-size: 30px;'>1.0 Introdução   </font>
<hr style='border: 2px solid red;'>




<p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>    
<i> “Chamar um especialista em estatística depois que o experimento foi feito pode ser o mesmo que pedir para ele fazer um exame post-mortem. Talvez ele consiga dizer do que foi que o experimento morreu.”  </i>     
</p>    

<p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: right; text-indent: 0px;'>    
    <b>Sir Ronald Fisher</b>  

<hr>

# <font color='red' style='font-size: 30px;'> Introdução à análise de experimentos   </font>
<hr style='border: 2px solid red;'>

# <font color = 'purple'> Inserindo o experimento num Data Frame </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>

## Importando as bibliotecas

### Pandas

https://pandas.pydata.org/
"""

import pandas as pd

"""### Numpy

http://www.numpy.org/
"""

import numpy as np

"""<p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
    <font color="red"> <b>Ensaios realizados na forma normalizada</b> 


<img width='800px' src='figuras/Figura_2.png'>

<p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
<font color="MidnightBlue"> Construindo uma matriz representando todos os ensaios realizados:
"""

ensaios = np.array([ [-1,-1], [1,-1], [-1,1], [1,1]   ])

"""### pyDOE2

https://pypi.org/project/pyDOE2/
"""

import pyDOE2 as doe

"""## Costruindo um planejamento fatorial de 2²

"""

ensaios  = doe.ff2n(2)

ensaios

"""## Incerindo o planejamento em um Data Frame"""

experimento = pd.DataFrame(ensaios, columns = ['Farinha','Chocolate']    )

experimento

"""### Inserindo coluna com os resultados """

experimento['Porcoes'] = [19,37,24,49]

experimento

"""<hr>
<p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
    <font color="MidnightBlue"> <b>Conclusão:</b> Temos, por fim, nosso experimento representado por um <i>DataFrame</i> do Pandas. Usaremos este <i>DataFrame</i> para iniciarmos a análise do nosso experimento. 
    
<hr>

# <font color = 'purple'> Analisando graficamente o experimento   </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>

###  Importando o Seaborn

https://seaborn.pydata.org
"""

import seaborn as sns

# paletas -> Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10, tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain, terrain_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r
sns.set_palette('terrain')

# estilo -> white, dark, whitegrid, darkgrid, ticks
sns.set_style('darkgrid')

"""### Para a farinha"""

ax1 = sns.lmplot(data = experimento, x = 'Farinha', y = 'Porcoes', ci = None, hue = 'Chocolate')


ax1.set(xticks = (-1,1))

"""### Para o chocolate"""

ax2 = sns.lmplot(data = experimento, x = 'Chocolate', y = 'Porcoes', ci = None, hue = 'Farinha'     )

ax2.set(xticks = (-1,1))

"""# <font color = 'purple'> Ajustando o modelo estatístico </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>

<hr>

<img width='800px' src='figuras/Figura_3.png'>

<p style='margin: 30px 30px;'> 

<hr>

### Bibliotecas  Stats Model
"""

import statsmodels.api as sm 

import statsmodels.formula.api as smf

"""### ."""

modelo = smf.ols(data = experimento, formula = 'Porcoes ~ Farinha + Chocolate + Farinha:Chocolate')

modelo_ajustado = modelo.fit()

print(modelo_ajustado.summary() )

"""# <font color = 'purple'> Aumentando os Graus de liberdade  </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>



<p style='margin: 30px 30px;'>

<hr>


<p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>
    <font color="red"> <b>Replicatas no centro</b>


<img width='800px' src='figuras/Figura_5.png'> 


<p style='margin: 30px 30px;'> 
    
    
 
    

    
<hr>
"""

centro = np.array([ [0,0,29],
                    [0,0,30],
                    [0,0,29],
                    [0,0,30],             ])

centro_dataframe = pd.DataFrame(centro, columns = ['Farinha', 'Chocolate','Porcoes'], index = [4,5,6,7]     )

centro_dataframe

"""### ."""

experimento = experimento.append(centro_dataframe)

experimento

"""# <font color = 'purple'>  Análise de significância estatística   </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>
"""

modelo = smf.ols(data = experimento, formula = 'Porcoes ~ Farinha + Chocolate + Farinha:Chocolate'     )

modelo_ajustado = modelo.fit()

print(modelo_ajustado.summary())

"""<p style='margin: 200px 200px;'>    


<hr>


    
 <img width='400px' src='figuras/Figura_6.png'> 


<p style='margin: 30px 30px;'>    

<hr>


 <img width='600px' src='figuras/Figura_7.png'> 


<p style='margin: 30px 30px;'>        
    
    
 <hr>   
    

  
 <img width='600px' src='figuras/Figura_10.png'> 


<p style='margin: 30px 30px;'>       
  
<hr>

# <font color = 'purple'> Teste de significância estatística usando o <b>t<b>    </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>

<hr>
<img width='600px' src='figuras/Figura_11.png'> 


<hr>
  <p style='margin: 30px 30px;'>     
<img width='900px' src='figuras/Figura_8.png'> 


<hr>

<p style='margin: 150px 150px;'>     
<img width='1000px' src='figuras/Figura_20.png'



<hr>
<p style='margin: 150px 150px;'>
"""

t_valores = modelo_ajustado.tvalues

t_valores

nome= t_valores.index.tolist()

nome

"""### ."""

from scipy import stats

"""### .

"""

distribuicao  = stats.t(df = 4)

distribuicao.ppf(q = 1 - 0.025)

limite = [distribuicao.ppf(q = 1 -0.025  )]*len(nome)

limite

"""### Plotando o gráfico """

pareto = sns.barplot(x = t_valores, y = nome )

pareto.figure.set_size_inches(15,6)

pareto.tick_params(labelsize = 20)

pareto.set_xlabel('t-valores', fontsize = 20)


pareto.plot(limite, nome, 'r')

"""# <font color = 'purple'> Propondo um novo modelo   </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>

<hr>

<img width='800px' src='figuras/Figura_3.png'>

<p style='margin: 30px 30px;'> 

<hr>

<p style='margin: 200px 200px;'>


<hr>

<img width='600px' src='figuras/Figura_9.png'> 

<p style='font-size: 18px; line-height: 2; margin: 0px 0px; text-align: justify; text-indent: 0px;'>


<p style='margin: 30px 30px;'>

    
<hr>
"""

modelo_2 = smf.ols(data = experimento, formula = 'Porcoes ~   Farinha + Chocolate'    )

modelo_ajustado_2 = modelo_2.fit()

print(modelo_ajustado_2.summary()  )

"""<hr>

# <font color = 'purple'> Gráfico Padronizado de Pareto do novo modelo    </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>
"""

t_valores = modelo_ajustado_2.tvalues

t_valores

nome = t_valores.index.tolist()

nome

"""### ."""

distribuicao = stats.t(df = 5)

distribuicao.ppf(q = 1 - 0.025)

limite = [distribuicao.ppf(q = 1 - 0.025    )]*len(nome)


limite

"""### Plotando o gráfico"""

pareto = sns.barplot(x = t_valores, y = nome)

pareto.figure.set_size_inches(15,6)

pareto.tick_params(labelsize = 20)

pareto.set_xlabel('t-valor', fontsize = 20)


pareto.plot(limite, nome, 'r')

"""<font color='red' style='font-size: 30px;'> Preditos por observados  </font>
<hr style='border: 2px solid red;'>
"""

observados = experimento['Porcoes']

observados

"""### ."""

preditos = modelo_ajustado_2.predict()

preditos

"""### ."""

import matplotlib.pyplot as plt

plt.figure(figsize = (10,5))

plt.xlabel('Preditos', fontsize = 16)

plt.ylabel('Observados', fontsize = 16)


#linha de guia

x = np.linspace(start = 15, stop = 50, num = 10      )


y = np.linspace(start = 15, stop = 50, num = 10)


plt.plot(x,y, 'r')


#comparacao 

plt.scatter(preditos, observados)

"""<hr>"""

print(modelo_ajustado_2.summary())

"""### .

# <font color = 'purple'> Explorando o modelo   </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>
"""

parametros = modelo_ajustado_2.params

parametros

"""### .

### Definindo a função
"""

def modelo_receita(x_f, x_c):
    
    #limite
    
    limite_normalizado = [-1,+1]
    
    limite_farinha = [0.5,1.5]
    
    limite_chocolate = [0.1,0.5]
    
    
    #Converter 
    
    x_f_convertido = np.interp(x_f, limite_farinha, limite_normalizado     )
    
    x_c_convertido = np.interp(x_c, limite_chocolate, limite_normalizado                 )
    
    
    
    
    
    porcoes = parametros['Intercept'] + parametros['Farinha']*x_f_convertido  + parametros['Chocolate']*x_c_convertido
    
    
    return round(porcoes)

modelo_receita(0.6,0.1)

"""<p style='margin: 150px 150px;'>


<hr>

<img width='700px' src='figuras/Figura_22.png'> 


<hr>

# <font color = 'purple'> Mapa de cores   </font>


<p style='margin: 30px 30px;'>
    
<hr style = 'border: 1px solid purple;'>

<p style='margin: 150px 150px;'>


<hr>

<img width='700px' src='figuras/Figura_23.jpg'> 

#### Fonte: National Centers for Environmental Prediction


<hr>



<p style='margin: 50px 50px;'>

<p style='margin: 150px 150px;'>


<hr>

<img width='600px' src='figuras/Figura_24.png'> 


<hr>



<p style='margin: 30px 30px;'>
"""

x_farinha = np.linspace(start = 0.5, stop = 1.5, num = 10     )

x_farinha

x_chocolate = np.linspace(start = 0.1, stop = 0.5, num = 10  )


x_chocolate

"""### . """

pontos = []


for cont1 in x_farinha:
    
    temp = []
    
    for cont2 in x_chocolate:
        
        temp.append(modelo_receita(cont1, cont2   ))
        
    pontos.append(temp)

pontos

"""### .

### Construindo a superfície de resposta
"""

import matplotlib.cm as cm

"""https://matplotlib.org/users/colormaps.html"""

#base

plt.figure(figsize = (16,6))

plt.xlabel('Farinha (kg)', fontsize = 16)

plt.ylabel('Chocolate (kg)', fontsize = 16)


#Mapa de cores 

mapa_cor = plt.imshow(pontos, origin = 'lower',  cmap = cm.rainbow, interpolation= 'quadric', extent = (0.5,1.5, 0.1,0.5)   )


#Barra de cor

plt.colorbar().set_label('Porcoes', fontsize = 16)


#linha 

linhas = plt.contour(x_farinha, x_chocolate, pontos, colors = 'k', linewidths = 1.5       )


plt.clabel(linhas, inline = True, fmt = '%1.0f', fontsize = 15.0 , inline_spacing = 10      )