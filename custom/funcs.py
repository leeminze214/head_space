# def embed_number_list(emb,it):
#     value = ''
#     for num,j in enumerate(it):
#         num +=1
#         value += f'{num}. [{j}]({it[j]})\n'
#     return value

def embed_list(emb,it):
    value = ''
    for i in it:
        emb.add_field()
        value += f'{i}'
    return value