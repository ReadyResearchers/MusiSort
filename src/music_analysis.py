#import tensorflow as tf
import numpy as np
import var_data as vd
from sklearn import datasets
from scipy.spatial import cKDTree
from sklearn import cluster
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram
from sklearn.metrics import silhouette_score
from scipy.stats import zscore
from sklearn.utils.multiclass import unique_labels

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    plot = dendrogram(linkage_matrix, **kwargs)
    
def iqr(a, outlierConstant):
    """
    a : numpy.ndarray (array from which outliers have to be removed.)
    outlierConstant : (scale factor around interquartile region.)                         
    """
    num = a.shape[0]

    upper_quartile = np.percentile(a, 75)
    lower_quartile = np.percentile(a, 25)
    IQR = (upper_quartile - lower_quartile) * outlierConstant
    quartileSet = (lower_quartile - IQR, upper_quartile + IQR)

    outlier_indx = []
    for i in range(num):
        if a[i] >= quartileSet[0] and a[i] <= quartileSet[1]: pass
        else: outlier_indx += [i]            

    return outlier_indx  


def function(arr):
    lst = []
    for i in range(arr.shape[0]):
        lst += iqr(a = arr[i,:], outlierConstant=0.5) 
    return lst
    
def remove_outliers(data, m = 2.):
    # Remove the far data points making data messed up in pca graph
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s<m]

def outlier_filter(data_x, data_y):
    indices = np.where(np.absolute(zscore(data_x)) > 6)[0]
    indices_filter = [i for i,n in enumerate(data_x) if i not in indices]

    split1 = data_y[indices_filter]
    split2 = data_x[indices_filter]
    
    indices2 = np.where(np.absolute(zscore(split1)) > 6)[0]
    indices_filter2 = [i for i,n in enumerate(split1) if i not in indices2]
    
    split1 = split1[indices_filter2]
    split2 = split2[indices_filter2]
    
    return np.vstack((split2, split1)).T

def reduce_data(data, dim):
    pca = PCA(dim)
    red_data = pca.fit_transform(data)
    return red_data
    
def save_2d_plot(data, name):
    fig = plt.scatter(data[0:len(data), 0], data[0:len(data), 1])
    plt.savefig(name + ".png")
    plt.clf()
    
def get_labels(data):
    # Takes a 2d array with each element being a vector
    # (50, 100) , 50 100 element vectors
    k = 30
    
    sil_score_max = 9999
    best_labels = None

    for n_cluster in range(2,k):
        model = KMeans(n_clusters = n_cluster, n_init=5).fit(data)
        labels = model.labels_
        sil_score = silhouette_score(data, labels)
        if sil_score < sil_score_max:
            sil_score_max = sil_score
            best_labels = labels
    return best_labels

def get_labels_simple(data, k):
    model = KMeans(n_clusters = k, n_init=1).fit(data)
    return model.labels_

def train_music_model():
    vd.convert_list_to_array()
    song_data = vd.array_audio
    
    song_titles = song_data[0]
    mel_labels = get_labels(song_data[1])
    pitch_labels = get_labels_simple(song_data[2], 10)
    bounds_labels = get_labels(song_data[3])
    
    condensed_labels = np.vstack((mel_labels, pitch_labels, bounds_labels)).T
    #condensed_labels = np.vstack((mel_labels, bounds_labels)).T
    
    final_labels = get_labels(condensed_labels)
    
    category_count = unique_labels(final_labels)
    
    songs = {}
    
    for label in category_count:
        songs[label] = []
    
    for index, label in enumerate(final_labels):
        songs[label].append(song_titles[index])
        
    for i in songs:
        print("Category ", i, " : \n\n")
        print(songs[i], "\n\n")
    
    '''
    k = 30
    
    sil_score_max = 9999 #this is the minimum possible score
    best_n_clusters = None
    best_labels = None
    clust_best = -1

    for n_cluster in range(2,k):
        model = KMeans(n_clusters = n_cluster, n_init=5).fit(song_data)
        labels = model.labels_
        sil_score = silhouette_score(song_data, labels)
        print("The average silhouette score for %i clusters is %0.2f" %(n_cluster,sil_score))
        if sil_score < sil_score_max:
            sil_score_max = sil_score
            best_n_clusters = model.cluster_centers_
            best_labels = labels
            clust_best = n_cluster
            
    print("Best Cluster : ", clust_best)
    categories = {}
    for i in range(clust_best):
        categories[("" + str(i))] = []
    
    for index, song_title in enumerate(vd.array_audio[0]):
        categories[("" + str(best_labels[index]))].append(song_title)
    
    for i in range(clust_best):
        print("\n\nCategory", i, ":", categories["" + str(i)])
    '''
         
    '''
    k_means_func = cluster.AgglomerativeClustering(distance_threshold=None, n_clusters=, linkage='average').fit(song_data)#KMeans(n_clusters=k, n_init=25).fit(song_data)
    print("\nLabels: ", k_means_func.labels_)
    plt.title("Hierarchical Clustering Dendrogram")
    plot_dendrogram(k_means_func, truncate_mode="level", p=k)
    plt.xlabel("Number of points in node (or index of point if no parenthesis).")
    plt.savefig("test.png")
    plt.show()
    '''
            