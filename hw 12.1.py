# Задание №1
# Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
# В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк


import pickle


job_title = [
    {
        'name': 'Alexandr',
        'position': 'engineer',
    },
    {
        'name': 'Maksim',
        'positione': 'director'
    }
]

file = open('omtp.com.ua', 'wb')
file.write(pickle.dumps(job_title))
file.close()

