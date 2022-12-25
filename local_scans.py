import os
ex_list = []
with open('/home/cricket/Downloads/pre_all.json', 'r') as pre:
    for i in pre.readlines():
        ex_list.append(i.split('/')[-1].split('"')[0])

for i in os.listdir('/home/cricket/Downloads/all_json'):
    if i in ex_list:
        os.remove(f'/home/cricket/Downloads/all_json/{i}')
