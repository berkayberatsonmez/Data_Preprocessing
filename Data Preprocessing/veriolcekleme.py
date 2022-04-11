#1.kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

#2.verionisleme
#2.1 veri yukleme
veriler = pd.read_excel("veriler.xlsx")

#print(veriler[['boy','kilo']])

#eksik veriler

#print(veriler2[['yas']])
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

yas = veriler.iloc[:,1:4].values
#test
print(yas)
imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas[:,1:4])
#test
print(yas)
#eksik veriler yerine ortalamasını alıp onu koyduk ki model etkilenmesin
#encoder: Kategorik -> Numeric
ulke = veriler.iloc[:,0:1].values
#test
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder() #sayısal olarak stringlere değer veriyor

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
#test
print(ulke)

ohe = preprocessing.OneHotEncoder() #kolon başlıklarını etiketleri taşımak ve her başlıkların altına 1 veya 0 verip oraya ait olduğunu belli etmek
ulke = ohe.fit_transform(ulke).toarray()
#test
print(ulke)
#ülkeler string değer olduğu için onları numeric yapamazdık bu yüzden onları kolonlara taşıdık ve 1 0 değerlerin verdik eğer ülke tr ise 1
#geri kalan değerlerde 0 olucak şekilde.


#numpy dizileri dataframe dönüşümleri
sonuc = pd.DataFrame(data=ulke, index = range(22), columns=['fr','tr','us'])
#test
print(sonuc)

sonuc2 = pd.DataFrame(data=yas, index = range(22), columns = ['boy','kilo','yas'] )
#test
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
#test
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns= ['cinsiyet'])
#test
print(sonuc3)

#dataframe birleştirme işlemleri
s = pd.concat([sonuc,sonuc2],axis=1) #dataframeleri birleştiriyoruz
#axis satır sayısından eşleme yapıyor
#test
print(s)

s2 = pd.concat([s,sonuc3],axis=1)
#test
print(s2)

#buraya kadar dataframe i düzenledik

#verilerin test için bölünmesi
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split( s,sonuc3,test_size=0.33,random_state=0)

#verilerin ölçeklenmesi
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
#fit etmenin amacı sayıları birbirine yaklaştırmak ve büyük sayılarla uğraşmamak

