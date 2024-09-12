## Görev 1:  Seaborn kütüphanesi içerisinden Titanicveri setini tanımlayınız.##


import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)

df = sns.load_dataset("titanic")


## Görev 2:  Titanic verisetindeki kadın ve erkek yolcuların sayısınıbulunuz. ##

df = sns.load_dataset("titanic")

df["sex"].value_counts()

## Görev3:  Her birsutuna ait  unique değerlerin sayısını bulunuz. ##

df = sns.load_dataset("titanic")
df.nunique()


## Görev4:  pclass değişkeninin unique değerlerininsayısını bulunuz.

df["pclass"].nunique()

##  Görev5:  pclass ve parch değişkenlerinin unique değerlerinin sayısınıbulunuz.  ##

i=["pclass","parch"]

df[i].nunique()

## Görev6:  embarked değişkeninin tipini kontrolediniz.
## Tipini category olarakdeğiştiriniz  ve  tekrarkontrolediniz


df["embarked"].head()
print(df["embarked"].dtypes)

df["embarked"].astype("category")
print(df["embarked"].astype("category"))

## Görev7:  embarked değeri C olanların tüm bilgelerini gösteriniz.


df[df["embarked"] == "C"].head()


## Görev8:  embarked değeri S olmayanların tüm bilgelerini gösteriniz.

df[df["embarked"] != "S"].head()



##  Görev9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.

df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()


##   Görev10:  Fare'i500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.

df.loc[(df["fare"] > 500 ) | (df["age"] > 70 )].head()


## Görev 11:  Her bir değişkendeki boş değerlerin  toplamını  bulunuz.

df.isnull().sum()


##  Görev 12:  who değişkenini dataframe’den çıkarınız.

df.drop("who", axis=1)


## Görev13:  deck değikenindeki  boş  değerleri deck değişkenin  en  çok tekrar  edendeğeri(mode) iledoldurunuz.

df_filled=df.fillna({"deck":df["deck"].mode()})

print(df_filled)


## Görev14:  age değikenindekiboşdeğerleriage değişkeninmedyanıiledoldurunuz.


df.fillna({"age":df["age"].median()})


##   Görev15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerinibulunuz

df.groupby(["pclass", "sex"])["survived"].agg(['sum', 'count', 'mean'])


## 30 yaşınaltındaolanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın.
## Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz.
## (apply velambda yapılarınıkullanınız)

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)

df["age_flag"]



## Görev17:  Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.


tips = sns.load_dataset("tips")
tips.head()


## Görev18: Time değişkeninin kategorilerine(Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.


tips.groupby("time")["total_bill"].agg(["sum", "min", "max", "mean"])


##  Görev19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.


tips.groupby(["day",  "time"])["total_bill"].agg(["sum", "min", "max", "mean"])



##Görev 20:  Lunch zamanına ve kadın  müşterilere  ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasınıbulunuz.


newdata = tips[(tips["time"] == "Lunch") & (tips["sex"] == "Female")]

newdata.groupby("day").agg({
    "total_bill": ["sum", "min", "max", "mean"],
    'tip': ["sum", "min", "max", "mean"]
})

######### hata veriyor çözemedim


## Görev 21: size'i 3'ten küçük, total_bill 'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)


data1 = tips.loc[(tips["size"] < 3) & (tips["total_bill"] > 10)]

data1['total_bill'].mean()


##Görev22: total_bill_tip_sum  adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.


tips["total_bill_tip_sum"] = tips["total_bill"] + tips["tip"]

print(tips)


##Görev23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız


sıra= tips.sort_values("total_bill_tip_sum", ascending=False)

ilk30  = sıra.head(30)