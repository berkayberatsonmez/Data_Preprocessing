#1.kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

#2.verionisleme
#2.1 veri yukleme
veriler = pd.read_excel("satislar.xlsx")

print(veriler)

aylar = veriler[['Aylar']]
print(aylar)

satislar = veriler[['Satislar']]
print(satislar)

#satislar2 = veriler.iloc[:,:1].values
#print(satislar2)




#verilerin test için bölünmesi
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(aylar,satislar,test_size=0.33,random_state=4)
'''
#verilerin ölçeklenmesi
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)
#fit etmenin amacı sayıları birbirine yaklaştırmak ve büyük sayılarla uğraşmamaki
'''
#model inşası (linear regression kullanılıcak)
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(x_train,y_train)    #fit fonksiyonu modeli inşa etmeye oluşturmaya yarıyor

tahmin = lr.predict(x_test)

x_train = x_train.sort_index() #verileri indexlere göre sıralıyor
y_train = y_train.sort_index()

plt.plot(x_train,y_train)
plt.plot(x_test,lr.predict(x_test)) #linear regresiondaki karşılığını göster

plt.title("aylara göre satış")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")







