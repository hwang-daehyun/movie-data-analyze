import pandas as pd
import re
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import nltk

# Load the Excel file
df = pd.read_excel("C:\\Users\\User\\Downloads\\241104_분석 데이터.xlsx")

# Preprocess text (Korean)
def preprocess_text(text):
    # Remove punctuation and numbers
    text = re.sub(r'[^ㄱ-ㅎ가-힣\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Preprocess Q14 and Q15 columns
df['Q14_Preprocessed'] = df['Q14. 귀하께서는 삼성증권을 이용하는 사람들은 어떤 사람들이라고 생각하십니까? 삼성증권을 이용하는 사람들의 특징이나 이미지를 생각나는 대로 자유롭게 적어 주시기 바랍니다.'].apply(preprocess_text)
df['Q15_Preprocessed'] = df['Q15. 귀하께서는 토스증권을 이용하는 사람들은 어떤 사람들이라고 생각하십니까? 토스증권을 이용하는 사람들의 특징이나 이미지를 생각나는 대로 자유롭게 적어 주시기 바랍니다.'].apply(preprocess_text)

# Combine the Q14 and Q15 preprocessed columns into one list for embedding
combined_text = df['Q14_Preprocessed'].tolist() + df['Q15_Preprocessed'].tolist()

# Load a pre-trained multilingual model for text embeddings
model = SentenceTransformer('xlm-r-100langs-bert-base-nli-stsb-mean-tokens')

# Generate embeddings for the combined text
embeddings = model.encode(combined_text)

# Find the optimal number of clusters using silhouette score
def find_optimal_clusters(embeddings, max_k):
    best_score = -1
    best_k = 2
    for k in range(2, max_k + 1):
        kmeans_model = KMeans(n_clusters=k, random_state=42)
        kmeans_model.fit(embeddings)
        score = silhouette_score(embeddings, kmeans_model.labels_)
        if score > best_score:
            best_score = score
            best_k = k
    return best_k

# Find the optimal number of clusters
optimal_clusters = find_optimal_clusters(embeddings, 10)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans.fit(embeddings)

# Assign cluster labels back to the original dataframe
df['Q14_Code'] = kmeans.labels_[:len(df)]
df['Q15_Code'] = kmeans.labels_[len(df):]

# Generate a summary for each cluster code with representative texts
cluster_summary = []
unique_clusters = np.unique(kmeans.labels_)

for cluster_num in unique_clusters:
    # Extract representative descriptions from the cluster
    cluster_texts = np.array(combined_text)[np.where(kmeans.labels_ == cluster_num)]
    representative_texts = cluster_texts[:3]  # Select the first 3 texts for summarization

    # Append cluster information
    cluster_summary.append({
        'Cluster_Code': cluster_num,
        'Representative_Texts': "\n".join(representative_texts),
        'Meaning': f"Cluster {cluster_num} groups descriptions that share similar characteristics."
    })

# Create a DataFrame from the cluster summary
summary_df = pd.DataFrame(cluster_summary)

# Save both the clustered descriptions and cluster summary to an Excel file
output_path = 'clustered_descriptions_with_summary.xlsx'
with pd.ExcelWriter(output_path) as writer:
    df.to_excel(writer, sheet_name='Clustered_Descriptions', index=False)
    summary_df.to_excel(writer, sheet_name='Cluster_Meanings', index=False)

print(f"Clustered data and cluster meanings saved to {output_path}")
