#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter


# In[89]:


data = pd.read_csv('movie_bd_v5.xls')
data.sample(5)


# In[125]:


data.describe()


# # Предобработка

# In[104]:


answers = {} # создадим словарь для ответов

# тут другие ваши предобработки колонок например:

#Check for Zero-values
data.info()

#change release_date to datetime format
data['release_date'] = pd.to_datetime(data['release_date'])

#Create column for profit value:
data['profit'] = data['revenue'] - data['budget']


# # 1. У какого фильма из списка самый большой бюджет?

# Использовать варианты ответов в коде решения запрещено.    
# Вы думаете и в жизни у вас будут варианты ответов?)

# In[41]:


# в словарь вставляем номер вопроса и ваш ответ на него
# Пример: 
answers['1'] = '2. Spider-Man 3 (tt0413300)'
# запишите свой вариант ответа

# если ответили верно, можете добавить комментарий со значком "+"


# In[105]:


# тут пишем ваш код для решения данного вопроса:
answers['1'] = '723. Pirates of the Caribbean: On Stranger Tides' #'+'

data[data.budget == data.budget.max()]


# ВАРИАНТ 2

# In[79]:


# можно добавлять разные варианты решения

data.budget.sort_values(ascending = False).head(1)


# # 2. Какой из фильмов самый длительный (в минутах)?

# In[147]:


# думаю логику работы с этим словарем вы уже поняли, 
# по этому не буду больше его дублировать


# In[106]:


answers['2'] = '1157. Gods and Generals (tt0279111)' # "+"

longest_film = data[data.runtime == data.runtime.max()]
longest_film


# # 3. Какой из фильмов самый короткий (в минутах)?
# 
# 
# 
# 

# In[107]:


answers['3'] = '768. Winnie the Pooh (tt1449283)' # "+"

shortest_film = data[data.runtime == data.runtime.min()]
shortest_film


# # 4. Какова средняя длительность фильмов?
# 

# In[108]:


answers['4'] = '110' # "+"

mean_runtime = data['runtime'].mean()
print(round(mean_runtime))


# # 5. Каково медианное значение длительности фильмов? 

# In[109]:


answers['5'] = '107.0'

median_runtime = data['runtime'].median()
median_runtime


# # 6. Какой самый прибыльный фильм?
# #### Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма. (прибыль = сборы - бюджет) в нашем датасете это будет (profit = revenue - budget) 

# In[110]:


# лучше код получения столбца profit вынести в Предобработку что в начале
answers['6'] = '239. Avatar (tt0499549)' # "+"

max_profit_film = data[data.profit == data.profit.max()]
max_profit_film


# # 7. Какой фильм самый убыточный? 

# In[111]:


answers['7'] = '1245. The Lone Ranger (tt1210819)' # "+"

min_profit_film = data[data.profit == data.profit.min()]
min_profit_film


# # 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[112]:


answers['8'] = '1478' # "+"

positive_moneyrate = data[data.revenue > data.budget]['original_title'].count()
display(positive_moneyrate)


# # 9. Какой фильм оказался самым кассовым в 2008 году?

# In[113]:


answers['9'] = '599. The Dark Knight (tt0468569)' # "+"

import datetime as dt

films_2008 = data[data['release_date'].dt.year == 2008]
films_2008[films_2008.revenue == films_2008.revenue.max()]


# # 10. Самый убыточный фильм за период с 2012 по 2014 г. (включительно)?
# 

# In[114]:


answers['10'] = '1245. The Lone Ranger (tt1210819)' # "+"

films_1214 = data[(data['release_date'].dt.year >= 2012) 
                 & (data['release_date'].dt.year <= 2014)]
films_1214[films_1214.profit == films_1214.profit.min()]


# # 11. Какого жанра фильмов больше всего?

# In[138]:


# эту задачу тоже можно решать разными подходами, попробуй реализовать разные варианты
# если будешь добавлять функцию - выноси ее в предобработку что в начале
display(data['genres'].str.split('|').explode().())


# ВАРИАНТ 2

# In[115]:


answers['11'] = 'Drama' # "+"

display(data['genres'].str.split('|').explode().value_counts())

    


# # 12. Фильмы какого жанра чаще всего становятся прибыльными? 

# In[116]:


answers['12'] = 'Drama' # "+"

profitable_films = data[data['profit'] > 0]
display(profitable_films['genres'].str.split('|').explode().value_counts())


# # 13. У какого режиссера самые большие суммарные кассовые сбооры?

# In[117]:


answers['13'] = 'Peter Jackson' # "+"

director_revenue = data.groupby(['director'])['revenue'].sum().sort_values(ascending = False)
display(director_revenue)


# # 14. Какой режисер снял больше всего фильмов в стиле Action?

# In[118]:


answers['14'] = 'Robert Rodriguez' # "+"
data['dirs'] = data.director.str.split('|')
action_director = data[data.genres.str.contains('Action')][['dirs']]
action_director_exp = action_director.explode('dirs')
action_director_exp.dirs.value_counts()


# # 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году? 

# In[119]:


answers['15'] = 'Chris Hemsworth' # "+"

films_2012 = data[data['release_date'].dt.year == 2012][['cast', 'revenue']]

films_2012['cast'] = films_2012['cast'].apply(lambda spl:spl.split('|'))
films_2012_exp = films_2012.explode('cast')
films_2012_exp.groupby(['cast'])['revenue'].sum().sort_values(ascending = False)


# # 16. Какой актер снялся в большем количестве высокобюджетных фильмов?

# In[120]:


answers['16'] = 'Matt Damon' # "+"

high_budget = data[data['budget'] > data['budget'].mean()]
high_budget['cast'] = high_budget['cast'].apply(lambda y:y.split('|'))
high_budget_exp = high_budget.explode('cast')
high_budget_exp['cast'].value_counts()


# # 17. В фильмах какого жанра больше всего снимался Nicolas Cage? 

# In[121]:


answers['17'] = 'Action' # "+"

cage_films = data[data.cast.str.contains('Nicolas Cage', na = False)]
cage_films['genres'] = cage_films['genres'].apply(lambda s: s.split('|'))
cage_films_exp = cage_films.explode('genres')
cage_films_exp.genres.value_counts()


# # 18. Самый убыточный фильм от Paramount Pictures

# In[122]:


answers['18'] = 'K-19: The Widowmaker (tt0267626)' # "+"

paramount_films = data[data.production_companies.str.contains(
    'Paramount Pictures', na = False)]
paramount_films[paramount_films.profit == paramount_films.profit.min()]


# # 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[123]:


answers['19'] = '2015' # "+"

data.groupby(['release_year'])['revenue'].sum().sort_values(ascending = False)


# # 20. Какой самый прибыльный год для студии Warner Bros?

# In[124]:


answers['20'] = '2014' # "+"

warner_films = data[data.production_companies.str.contains(
    'Warner Bros', na = False)]
warner_films.groupby(['release_year'])['profit'].sum().sort_values(ascending = False)


# # 21. В каком месяце за все годы суммарно вышло больше всего фильмов?
# 
# 

# In[125]:


answers['21'] = '9 (September)' # "+"

data_months = data.copy()
data_months['months'] = data.release_date.dt.month
data_months.groupby('months')['original_title'].count().sort_values(ascending = False)


# # 22. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)

# In[126]:


answers['22'] = '450' # "+"

summer_films = data[(data.release_date.dt.month >= 6) 
                    & (data.release_date.dt.month <= 8)]
summer_films.original_title.count()


# # 23. Для какого режиссера зима – самое продуктивное время года? 

# In[127]:


answers['23'] = 'Peter Jackson' # "+"

data['dirs'] = data.director.str.split('|')
data_exp = data.explode('dirs')

winter_films = data_exp[(data_exp.release_date.dt.month == 12) 
                    |(data_exp.release_date.dt.month <= 2)]
winter_films['dirs'].value_counts()


# # 24. Какая студия дает самые длинные названия своим фильмам по количеству символов?

# In[128]:


answers['24'] = 'Four By Two Productions' 

def counter(movie_bd, x):
    data_plot=movie_bd[x].str.cat(sep='|')
    dat=pd.Series(data_plot.split('|'))
    info=dat.value_counts(ascending=False)
    return info

data['title_words_length'] = data.original_title.map(lambda x: len(x.split(' ')))

sum_gen=counter(data,'production_companies')

for gen in sum_gen.index:
    sum_gen[gen] = data['title_words_length'][data['production_companies'].map(
        lambda x: True if gen in x else False)].mean()
    
sum_gen = pd.DataFrame(sum_gen).sort_values(0, ascending=False)
display(sum_gen)


# # 25. Описание фильмов какой студии в среднем самые длинные по количеству слов?

# In[129]:


answers['25'] = 'Midnight Picture Show' # "+"

data['overview_length'] = data.overview.str.split().apply(len)
data_companies = data.copy()
data_companies['production_companies'] = data['production_companies'].apply(
    lambda x: x.split('|'))
data_companies_exp = data_companies.explode('production_companies')
data_companies_exp.groupby(['production_companies'])[
    'overview_length'].mean().sort_values(ascending = False)


# # 26. Какие фильмы входят в 1 процент лучших по рейтингу? 
# по vote_average

# In[130]:


answers['26'] = 'Inside Out, The Dark Knight, 12 Years a Slave' # "+"

data_best = data.copy()
data_best_99 = data_best[data_best.vote_average 
                         > data_best.quantile(0.99, numeric_only=True)['vote_average']]
data_best_99


# # 27. Какие актеры чаще всего снимаются в одном фильме вместе?
# 

# ВАРИАНТ 2

# In[131]:


answers['27'] = 'Daniel Radcliffe & Rupert Grint' # "+"

from itertools import combinations
actor_list = data.cast.str.split('|').tolist()
combo_list=[]

for i in actor_list:
    for j in combinations(i, 2):
        combo_list.append(' '.join(sorted(j)))
        
combo_list = pd.DataFrame(combo_list)
combo_list.columns = ['actor_combinations']
combo_list.actor_combinations.value_counts().head(10)


# # Submission

# In[132]:


# в конце можно посмотреть свои ответы к каждому вопросу
answers


# In[133]:


# и убедиться что ни чего не пропустил)
len(answers)


# In[ ]:





# In[ ]:




