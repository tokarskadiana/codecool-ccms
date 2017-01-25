#generatore number uno



list_of_names = [
'Mathilde Hassen',
'Lavonne Haskin',
'Tuan Hatmaker',
'Mee Pannone',
'Norberto Nordeen',
'Jeffry Blomquist',
'Miriam Oden',
'Kenyetta Mcpeters',
'Lula Manzi',
'Raquel Huseby',
'Rolf Ours',
'Isis Studivant',
'Ching Blom',
'Eneida Long',
'Darren Vise',
'Charmain Stutsman',
'Despina Fiorito',
'Leanora Lovelad',
'Breann Balcom',
'Isiah Gadd'
]
first_names = []
last_names =[]

def split(list):
    for names in list:
        split_name = list(names.split(' '))
        first_names.append(split_name[0])
        last_names.append(split_name[1])

# '../data_base/students.csv'

split(list_of_names)

def create_csv(first_names, last_names, file_path):
    with open(file_path, 'w+') as file:
        file.writelines()



create_csv(first_names, last_names)