#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
number = np.random.randint(1,101)

def game_core(number):
    '''Создаём функцию, которая увеличивает/уменьшает предполагаемое число 
    на среднее значение из диапазона и возвращает число попыток'''
    count = 1 #Счетчик попыток
    max_number = 100
    min_number = 1
    predict = np.random.randint(1,101) #Предполагаемое число
    while number != predict:
        count += 1
        interval_mean = (max_number + min_number)//2
        if number > predict:
            predict += interval_mean
            max_number = interval_mean #Смещаем диапазон значений
        elif number < predict:
            predict -= interval_mean
            max_number = interval_mean
    return(count)
 
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core)
    


# In[ ]:




