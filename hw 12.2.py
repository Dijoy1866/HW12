#Задание 2
# Дано два словаря
# Необходимо написать код который будет их объединять
# Но нужно так-же учитывать коллизии, например ситуация когда у нас два одинаковых ключа и чтобы
# не потерять значения нужно записать в один ключ список в котором будут находится значения
# Записать результат в файл result.json в формате JSON.

import json

fast_car = {
    'drift': 'nissan',
    'price': '32k'
}
comfort_car = {
    'drift': 'mazda',
    'starting price': '42000$'
}
same_keys = {}
for key, value in fast_car.items():
    for key1, value1 in comfort_car.items():
        if key == key1:
            same_keys[key1] = [value, value1]
        else:
            break

diff_keys = fast_car | comfort_car
result = diff_keys | same_keys

json_result = json.dumps(result)
with open('result.json', 'w') as file:
    file.write(json_result)
