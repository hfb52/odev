
#####################################################
# Görev 1:  Veriyi Hazırlama ve Analiz Etme
#####################################################

# Adım 1:  ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı değişkenlere atayınız.



import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)



xls = pd.ExcelFile("ABTesti/ab_testing.xlsx")
print(xls.sheet_names)

kontrol_grubu = pd.read_excel("ABTesti/ab_testing.xlsx", sheet_name="Control Group")
test_grubu = pd.read_excel("ABTesti/ab_testing.xlsx", sheet_name="Test Group")

kontrol_grubu.head()
test_grubu.head()


# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.


# impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı

# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı

# Earning: Satın alınan ürünler sonrası elde edilen kazanç

kontrol_grubu = kontrol_grubu.assign(ConversionRateCI=lambda x: (x['Click'] / x['Impression'] * 100).astype(int))


kontrol_grubu = kontrol_grubu.assign(ConversionRatePC=lambda x: (x['Purchase'] / x['Click'] * 100).astype(int))

kontrol_grubu.sort_values(by="ConversionRateCI",ascending=False)
kontrol_grubu.sort_values(by="ConversionRatePC",ascending=False)


kontrol_grubu=kontrol_grubu.drop(columns=["conversionrate"])
kontrol_grubu.head()
kontrol_grubu.tail()
kontrol_grubu.shape
kontrol_grubu.info()
kontrol_grubu.columns
kontrol_grubu.index
kontrol_grubu.describe().T
kontrol_grubu.isnull().values.any()
kontrol_grubu.isnull().sum()


test_grubu.head()
test_grubu.tail()
test_grubu.shape()
test_grubu.info()
test_grubu.columns
test_grubu.index
test_grubu.describe().T
test_grubu.isnull().values.any()
test_grubu.isnull().sum


# Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.
kontrol_grubu["group"] = "control"
test_grubu["group"] = "test"

birlesik_veri = pd.concat([kontrol_grubu, test_grubu], ignore_index=True)


birlesik_veri.head()




#####################################################
# Görev 2:  A/B Testinin Hipotezinin Tanımlanması
#####################################################

# Adım 1: Hipotezi tanımlayınız.

H0: M1=M2
H1: M1!=M2


# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analiz ediniz
birlesik_veri.groupby("group").agg({"Purchase": "mean"})


kontrol_grubu["Purchase"].mean()
test_grubu["Purchase"].mean()



#####################################################
# GÖREV 3: Hipotez Testinin Gerçekleştirilmesi
#####################################################


# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir.


############################
# Normallik Varsayımı
############################

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.

test_stat, pvalue = shapiro(birlesik_veri.loc[birlesik_veri["group"] == "control", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#######     p > 0.05 ,   H0 REDDEDİLEMEZ


test_stat, pvalue = shapiro(birlesik_veri.loc[birlesik_veri["group"] == "test", "Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#######     p > 0.05 ,   H0 REDDEDİLEMEZ



############################
# Varyans Homojenligi Varsayımı
############################

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_stat, pvalue = levene(kontrol_grubu["Purchase"],test_grubu["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


#######     p > 0.05 ,   H0 REDDEDİLEMEZ


#####Varsayımlar sağlanıyosa bağımsız iki örneklem t testi (parametrik test)

test_stat, pvalue = ttest_ind(kontrol_grubu["Purchase"],test_grubu["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


#######     p > 0.05 ,   H0 REDDEDİLEMEZ
