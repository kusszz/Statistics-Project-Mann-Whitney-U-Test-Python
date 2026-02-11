import pandas as pd
import os.path
from Project_functions import count_rejections
from Project_functions import perform_test

'''
Mann-Whitney U Test  

Hypotheses:
H0: Physical activity has no effect on well-being
H1: Physical activity affects well-being

Sample size: 60
'''

# for FutureWarning
pd.set_option('future.no_silent_downcasting', True)

path=os.path.join(os.path.expanduser("~"), 'Desktop', 'Quiz odpowiedzi.xlsx') #file path
plik=pd.read_excel(path)
#print(plik)

#print(plik.columns) #column names

#approach 1 ------------------------------------------------------------------------------------
#I'm taking 'Physical activity (exercises, workouts, walks of at least 20 minutes, etc.)' and 'Does back pain affect your mood or stress levels?' columns
test=plik[["Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)","Czy ból pleców wpływa na Twój nastrój/stres?"]]

#Standardizing values in the 'Physical activity' column
test.loc[:,"Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)"] = test["Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)"].replace({
    "<1x/tydzień": "Rzadziej niż 1 raz w tygodniu",  "1-2x/tydzień": "1–2 razy w tygodniu"
})

#I want full records only
test=test.dropna()
#'Nie dotyczy' means 'Not applicable' - I also don't want that
test = test[test["Czy ból pleców wpływa na Twój nastrój/stres?"] != 'Nie dotyczy']

# Physical activity->binary
# Mało ruchu (low activity): brak, Rzadziej niż 1 raz w tygodniu, 1–2 razy w tygodniu
# Dużo ruchu (high activity): 3–4 razy w tygodniu, 5 razy w tygodniu lub więcej

binary= {
    'brak': "Mało_ruchu",
    'Rzadziej niż 1 raz w tygodniu': "Mało_ruchu",
    '1–2 razy w tygodniu': "Mało_ruchu",
    '3–4 razy w tygodniu': "Dużo_ruchu",
    '5 razy w tygodniu lub więcej': "Dużo_ruchu"
}
test["Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)"]=test["Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)"].replace(binary)


# well-being -> ordinal
ordinal={
    'Nie' : 0,
    'Trochę' : 1,
    'Tak, bardzo': 2
}
test.loc[:,"Czy ból pleców wpływa na Twój nastrój/stres?"]=test["Czy ból pleców wpływa na Twój nastrój/stres?"].replace(ordinal)

low=[] 
high=[]

for row in test.itertuples():
    if row[1]=='Mało_ruchu':
        low.append(row[2])
    elif row[1]=='Dużo_ruchu':
        high.append(row[2])

# print(test)

print(perform_test(low,high))

print(count_rejections(low, high))


#approach 2 ------------------------------------------------------------------------------------
# This time I'm taking:
# "Physical activity (exercises, workouts, walks of at least 20 minutes, etc.)" (binary),
# "Does back pain affect your mood/stress?" (ordinal),
# "Has back pain prevented you from attending a social event?" (ordinal) ,
# "Does back pain make it difficult for you to sleep?" (ordinal),
# "Does back pain limit your professional activity?" (ordinal)

test2=plik[["Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)","Czy ból pleców wpływa na Twój nastrój/stres?",'Czy ból pleców uniemożliwił Ci udział w wydarzeniu towarzyskim?','Czy ból pleców utrudnia Ci sen?','Czy ból pleców ogranicza Twoją aktywność zawodową?']]

test2.loc[:,"Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)"] = test2["Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)"].replace({
    "<1x/tydzień": "Rzadziej niż 1 raz w tygodniu",  "1-2x/tydzień": "1–2 razy w tygodniu"
})

#I want full records only
test2=test2.dropna()
test2 = test2[test2["Czy ból pleców wpływa na Twój nastrój/stres?"] != 'Nie dotyczy']
test2 = test2[test2['Czy ból pleców ogranicza Twoją aktywność zawodową?'] != 'Nie dotyczy']

test2.loc[:,"Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)"]=test2["Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.)"].replace(binary)
test2.loc[:,"Czy ból pleców wpływa na Twój nastrój/stres?"]=test2["Czy ból pleców wpływa na Twój nastrój/stres?"].replace(ordinal)

social_event={
    'Nie': 0,
    'Tak, raz':1,
    'Tak, wielokrotnie':2
}

test2.loc[:,'Czy ból pleców uniemożliwił Ci udział w wydarzeniu towarzyskim?']=test2['Czy ból pleców uniemożliwił Ci udział w wydarzeniu towarzyskim?'].replace(social_event)

sleep={
    'Nigdy':0,
    'Rzadko':1,
    'Czasami':2,
    'Tak, często':3
}
test2.loc[:,'Czy ból pleców utrudnia Ci sen?']=test2['Czy ból pleców utrudnia Ci sen?'].replace(sleep)

professional_activity={
    'Nie': 0,
    'Tak, trochę':1,
    'Tak, znacząco':2
}

test2.loc[:,'Czy ból pleców ogranicza Twoją aktywność zawodową?']=test2['Czy ból pleców ogranicza Twoją aktywność zawodową?'].replace(professional_activity)

# print(test2.head())

low2=[]
high2=[]

for row in test2.itertuples():
    if row[1]=='Mało_ruchu':
        low2.append(row[2] + row[3] + row[4] + row[5])
    elif row[1]=='Dużo_ruchu':
        high2.append(row[2] + row[3] + row[4] + row[5])

print(perform_test(low2, high2))

print(count_rejections(low2, high2))


