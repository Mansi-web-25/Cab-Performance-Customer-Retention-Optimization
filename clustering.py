from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv('../data/sample_trip_data.csv')

# Features for clustering
features = df[['ride_count', 'avg_rating', 'cancellation_count']]
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(features)

# Visualize
plt.scatter(df['ride_count'], df['avg_rating'], c=df['cluster'])
plt.xlabel('Ride Count')
plt.ylabel('Average Rating')
plt.title('Customer Segmentation')
plt.show()
