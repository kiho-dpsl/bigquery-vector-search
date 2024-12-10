import json


def preprocess_data(df):
    df['texts'] = df.apply(lambda row: json.dumps({'job_title': row['job_title'], 'company_desc': row['company_desc'], 'location': row['location'], 'industry': row['industry'], 'keywords': row['keywords']}), axis=1)
    df['metadatas'] = df.apply(lambda row: {'name': row['name'], 'email': row['email'], 'job_title': row['job_title'], 'company': row['company'], 'location': row['location'], 'industry': row['industry']}, axis=1)
    return df[['texts', 'metadatas']]