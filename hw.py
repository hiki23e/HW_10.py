import random
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

encoder = OneHotEncoder(sparse_output=False)
encoder.fit_transform(data[['whoAmI']])
data_head = encoder.fit_transform(data[['whoAmI']])
data_head_df = pd.DataFrame(data_head, columns=encoder.categories_[0])
print(data_head_df)
