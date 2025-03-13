import pandas as pd
import numpy as np

# Dosya yolunu tanımlama
path = r'path'

# Excel dosyasını okuma
df = pd.read_excel(path)

# DataFrame'in özet bilgilerini yazdırma (ilk kullanım)
print("İlk info:")
df.info()

# 'Motor_hacmi' sütununu tam sayıya çevirme
df['Motor_hacmi'] = df['Motor_hacmi'].astype(int)

# Yeni bir sütun oluşturma: 'Motor_hacmi3' (tam sayı hali)
df['Motor_hacmi3'] = df['Motor_hacmi'].astype(int)

# 'Motor_hacmi2' sütununu oluşturma: Yukarı yuvarlama ve tam sayı
df['Motor_hacmi2'] = np.ceil(df['Motor_hacmi']).astype(int)

# DataFrame'in güncellenmiş özet bilgilerini yazdırma
print("\nGüncellenmiş info:")
df.info()

# Temel istatistikler (sadece sayısal sütunlar)
print("\nSayısal sütunların istatistikleri:")
print(df.describe())

# Tüm sütunların istatistikleri (kategorik dahil)
print("\nTüm sütunların istatistikleri:")
df_tanimlayici_ist = df.describe(include='all').T.reset_index()

# Tanımlayıcı istatistiklerin transpozu ve özet bilgileri
print("\nTanımlayıcı istatistiklerin transpozu:")
print(df_tanimlayici_ist)

# Tanımlayıcı istatistiklerin info'su
print("\nTanımlayıcı istatistiklerin info:")
df_tanimlayici_ist.info()
