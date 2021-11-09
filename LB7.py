import pickle
import numpy as np
import pandas as pd


def sort_shells(data, N):
    len=N
    len=len//2
    while len > 0:        
        for i in range(N-len):
            n=i
            while (n >= 0) and (data.iloc[n,8] < data.iloc[n+len,8]):
                buf = data.iloc[n]
                data.iloc[n]=data.iloc[n+len]
                data.iloc[n+len]=buf
                n=n-1
        len=len//2
    return data


students_file_results={'Name_Surname':['Ivanov Ivan', 'Petrov Pavel', 'Sidorov Ivan', 'Koval Julia', 'Fedorova Maria', 'Kim Daniil', 'Kim Dmitriy','Baryshev Igor', 'Koval Olga', 'Petrova Maria', 'Ivanova Valentina', 'Petrov Vasiliy', 'Fedorov Mikhail', 'Karasev Dmitriy', 'Gordov Mikhail'],
                 'Group': [1, 2, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1],
                 'Mathematics': [4, 5, 4, 4, 5, 5, 3, 3, 4, 3, 4, 5, 4, 4, 4],
                 'Informatics': [3, 4, 3, 4, 5, 5, 5, 3, 5, 5, 4, 4, 5, 5, 5],
                 'Physics': [5, 4, 4, 5, 5, 5, 5, 5, 5, 3, 3, 5, 5, 3, 4],
                 'History': [3, 4, 4, 5, 5, 5, 4, 4, 5, 5, 5, 4, 4, 4, 5],
                 'Russian': [4, 5, 5, 5, 4, 5, 5, 4, 3, 3, 5, 4, 4, 4, 5]}
     

st=pd.DataFrame(students_file_results, columns=['Name_Surname', 'Group','Mathematics', 'Informatics', 'Physics', 'History', 'Russian' ])



st['Sum'] = st[['Mathematics', 'Informatics', 'Physics', 'History', 'Russian']].sum(axis=1)

print(st)

st['Mean']= st[['Mathematics', 'Informatics', 'Physics', 'History', 'Russian']].mean(axis=1)
print(st)

sort_mean=st[st.Mean> 4.0] [['Name_Surname','Group', 'Mathematics', 'Informatics', 'Physics', 'History', 'Russian','Mean']]


mean_sort=sort_mean.sort_values('Mean', ascending=True)
print(mean_sort)

sort_shells(st,15)

print(st[st.Mean> 4.0] [['Name_Surname','Group', 'Mathematics', 'Informatics', 'Physics', 'History', 'Russian','Mean']])

count_gr=st.groupby(['Group'])['Name_Surname'].count()

print(count_gr)

pvt=st.pivot_table(index=['Group'],values=['Name_Surname'], aggfunc='count')
print(pvt)


                                          
                                  
student=[
    {'Name_Surname': 'Ivanov Ivan', 'Items':'Mathematics','Arears':'test'},
    {'Name_Surname': 'Petrov Pavel', 'Items':'Mathematics','Arears':'test'},
    {'Name_Surname': 'Sidorov Ivan', 'Items':'Physics','Arears':'test'},
    {'Name_Surname': 'Sidorov Ivan', 'Items':'Russian','Arears':'test'},
    {'Name_Surname': 'Koval Julia', 'Items':'Russian','Arears':'test'},
    {'Name_Surname': 'Koval Julia', 'Items':'Mathematics','Arears':'test'},
    {'Name_Surname': 'Fedorova Maria', 'Items':'Informatics','Arears':'test'},
    {'Name_Surname': 'Fedorova Maria', 'Items':'Physics','Arears':'test'},
    {'Name_Surname': 'Baryshev Igor', 'Items':'History','Arears':'test'},
    {'Name_Surname': 'Baryshev Igor', 'Items':'Physics','Arears':'test'}
    ]

sdf=pd.DataFrame(student,columns=['Name_Surname','Items', 'Arears'])
print(sdf)

pvt1=sdf.pivot_table(index=['Name_Surname'], values=['Items'], aggfunc='count')
print(pvt1)

st_new=pd.concat([st, sdf], axis=1)
print(st_new)

