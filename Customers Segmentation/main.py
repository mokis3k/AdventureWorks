import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

df = pd.read_csv('CustomerFeaturesTable.csv', sep=';')

features = ['TotalQuantity', 'TotalRevenue', 'OrderCount', 'CategoryCount', 'AvgCheck', 'RecencyDays']
X = df[features]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

cluster_names = {
    0: 'Least valuable',
    1: 'Premium',
    2: 'Frequent buyers',
    3: 'Inactive premium'
}
df['ClusterName'] = df['Cluster'].map(cluster_names)

cluster_profile = (
    df.groupby(['Cluster', 'ClusterName'])[features]
    .mean()
    .round(2)
    .reset_index()
)
cluster_profile.to_csv('ClusterProfiles.csv', index=False)

customer_clusters = df[['CustomerID', 'Cluster']]
customer_clusters.to_csv('CustomerClusters.csv', index=False)

print("- ClusterProfiles.csv (с ClusterName)")
print("- CustomerClusters.csv (CustomerID + Cluster)")