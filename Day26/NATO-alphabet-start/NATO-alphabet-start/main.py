student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_letters = {row.letter:row.code for (index, row) in data.iterrows()}
# print(dict_letters)
{"A": "Alfa", "B": "Bravo"}
def generate_phonetic():
    word = input("enter the word you want to rephrase: ").upper()
    try:
        result = [dict_letters[w] for w in word]
    except KeyError:
        print("Only alphabets are allowed")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
