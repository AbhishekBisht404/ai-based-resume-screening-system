import pandas as pd
from sklearn.utils import resample

df = pd.read_csv("cleaned_resumes.csv")

target_size = df['job_category'].value_counts().max()

df_upsampled = pd.concat([
    resample(df[df['job_category'] == label],
             replace=True,
             n_samples=target_size,
             random_state=42)
    for label in df['job_category'].unique()
])

df_upsampled = df_upsampled.sample(frac=1, random_state=42).reset_index(drop=True)


df_upsampled.to_csv("cleaned_resumes_upsampled.csv", index=False)

print("Upsampled class distribution:")
print(df_upsampled['job_category'].value_counts())
