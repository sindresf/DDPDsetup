# TODO: here make (copy paste in)
# TODO: super simple ML thing
# TODO: for the google fire to connect to and run

import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits


def test(digit: int = 0, shuffle: bool = False):
    digits = load_digits()
    if shuffle:
        np.random.shuffle(digits.images)
    plt.gray()
    plt.matshow(digits.images[digit])
    plt.show()

    data = scale(digits.data)

    n_digits = len(np.unique(digits.target))
    labels = digits.target

    model = KMeans(init='random', n_clusters=n_digits, n_init=10)
    model.fit(data)
    print("KMeans base inertia, ", model.inertia_)
    print("KMeans base completeness score, ", metrics.completeness_score(labels, model.labels_),)
    print("KMeans base v_measure score, ", metrics.v_measure_score(labels, model.labels_),)
    print("KMeans base silhouette score, ", metrics.silhouette_score(data, model.labels_, metric='euclidean', sample_size=250))
    print()
    reduced_data = PCA(n_components=2).fit_transform(data)
    kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
    kmeans.fit(reduced_data)
    print("KMeans with effort inertia, ", kmeans.inertia_)
    print("KMeans with effort completeness score, ", metrics.completeness_score(labels, kmeans.labels_),)
    print("KMeans with effort v_measure score, ", metrics.v_measure_score(labels, kmeans.labels_),)
    print("KMeans with effort silhouette score, ",
          metrics.silhouette_score(data, kmeans.labels_, metric='euclidean', sample_size=250))

    h = .006
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')
    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=120, linewidths=2,
                color='w', zorder=10)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()
