import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("govt.csv")
df.head()
df.shape
df.columns
df.info
df.describe()
df.isnull().sum()
df.isnull().sum().sum()
df.duplicated().sum()
df.columns
df['state_name'].nunique()
df.columns
district_count = df['district_name'].value_counts()
top10_districts = district_count.head(10)
top10_districts
import matplotlib.pyplot as plt

top10_districts.plot(kind='bar', figsize=(10,5))
plt.title("Top 10 Districts by Number of Schools")
plt.xlabel("District")
plt.ylabel("Number of Schools")
plt.xticks(rotation=45)
plt.show()
import matplotlib.pyplot as plt
top10_districts.plot(kind='bar')
management_count = df['sch_mgmt_name'].value_counts()
management_count
top10_management = management_count.head(10)
top10_management
import matplotlib.pyplot as plt

top10_management.plot(kind='bar', figsize=(10,5))
plt.title("Top 10 School Management Types")
plt.xlabel("Management Type")
plt.ylabel("Number of Schools")
plt.xticks(rotation=45)
plt.show()
boys_total = df[['pre_primary_boy',
                 'class1_boy','class2_boy','class3_boy','class4_boy',
                 'class5_boy','class6_boy','class7_boy','class8_boy',
                 'class9_boy','class10_boy','class11_boy','class12_boy']].sum().sum()

boys_total
girls_total = df[['pre_primary_girl',
                  'class1_girl','class2_girl','class3_girl','class4_girl',
                  'class5_girl','class6_girl','class7_girl','class8_girl',
                  'class9_girl','class10_girl','class11_girl','class12_girl']].sum().sum()

girls_total
import matplotlib.pyplot as plt

plt.figure(figsize=(6,5))
plt.bar(['Boys', 'Girls'], [boys_total, girls_total])
plt.title('Total Boys vs Total Girls')
plt.xlabel('Gender')
plt.ylabel('Number of Students')
plt.show()
category_count = df['school_category'].value_counts()
category_count
top10_category = category_count.head(10)
top10_category
import matplotlib.pyplot as plt

top10_category.plot(kind='bar', figsize=(10,5))
plt.title("Top 10 School Categories")
plt.xlabel("School Category")
plt.ylabel("Number of Schools")
plt.xticks(rotation=45)
plt.show()

