# def embed_number_list(emb,it):
#     value = ''
#     for num,j in enumerate(it):
#         num +=1
#         value += f'{num}. [{j}]({it[j]})\n'
#     return value
from custom.refers import time_names

def embed_time(emb,time_list):
    for i in range(4):
        emb.add_field(name= f'{time_names[i]}',value = f'{time_list[i]}')

def string_time(emb,time_list):
    value = ''
    for i in range(4):
        value+= f'{time_names[i]}: {time_list[i]}\n'
    return value
