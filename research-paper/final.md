# Big Data Tools for Anomaly Detection 






## ***Introduction***

The number of cyberattacks on system networks has grown exponentially over the past several years [1]. These attacks can devastate businesses and individuals alike on a large scale. In order to prevent these threats, network defense systems utilize signature-based intrusion detection and anomaly-based intrusion detection methods. Signature-based intrusion detection prevents known attacks to systems by flagging threats based on a list of known indicators that precede an attack. On the other hand, anomaly-based detection evaluates the current network to a baseline of normal network behavior to flag suspicious behavior if it deviates from normal traffic. While signature-based detections are effective at preventing known threats, anomaly-based detection systems are significantly more effective at preventing threats that the system may have not seen before. This is a particularly useful attribute as the amount of network traffic continues to grow, and the types of attacks evolve in form. Modern anomaly-based intrusion detection methods utilize big data tools such as machine learning algorithms to create defense systems that can identify abnormalities in network traffic. The paper will begin by evaluating the general framework for anomaly-based detection. Next, the paper will evaluate specific approaches and algorithms for anomaly-based detection. Lastly, the paper will evaluate recent advances in anomaly-based detection systems using big data tools. Overall, the paper aims to describe the role of big data tools, specifically machine learning algorithms, in anomaly-based intrusion detection systems and identify potential future trends. 



## ***General approach for all anomaly detection***

As it relates to employing machine learning algorithms, anomaly-based detection systems for networks typically utilize a training dataset to develop a model of normal behavior and then apply the model to network traffic in order to detect anomalies [2]. Depending on the number of available labels in the dataset: supervised, semi-supervised, and unsupervised techniques are used to develop algorithms for anomaly-based detection systems. Supervised techniques require labels that specify normal behavior versus abnormal behavior. On the other hand, semi-supervised techniques utilize a small amount of labeled data to create the model and use the majority of the unlabeled data to test the accuracy of the model. Unsupervised learning utilizes a dataset with unlabeled data with the assumption that a majority of the data is “normal” behavior, after which the model identifies behavior that deviates from the rest of the data. Using either supervised, semi-supervised, or unsupervised training, three main approaches can be used to construct anomaly-based detection systems using machine learning algorithms. 









## ***Nearest-neighbor approach***

The first approach to building an anomaly-based detection system using machine learning is a type of clustering technique called nearest-neighbor. The nearest-neighbor-based approach detects anomalies based on distance. The K Nearest-Neighbor algorithm is the most popular algorithm for this approach, and it stores the training data and evaluates new data by computing a score based on the K Nearest-Neighbor. Depending on the type of data, either Euclidean distance or Hamming distance is used [3]. Euclidean distance is typically used for continuous data, while hamming distance is used for discrete data. Figure 2.1 illustrates an example of the K-Nearest Neighbor algorithm in which data points that are anomalous by the score are indicated with the color red. The advantages of K Nearest-Neighbor detection techniques are that it is relatively easily applicable and it can handle data types such as text. KNN, however, has a large overhead, especially if the data contains many features, and its performance is poor for clusters with diverse features[4]. 





![](Aspose.Words.865fb2c8-08d2-4415-8812-a02a1e9b05b1.001.png)

***Figure 2.1***





## ***Density based approach***

The second approach to building an anomaly-based detection system using machine learning is also a type of clustering named density-based clustering. Density-based clustering groups data according to specific parameters in regions that are not as dense and are considered anomalies. Local Density Cluster-based Outlier Factor (LDCOF)  is the most common algorithm for density-based clustering as it relates to anomaly detection. LDCOF divides a dataset into clusters primarily by using k-means and then computes the LDCOF scores by dividing the distance of an object to its cluster center by the average distance [5]. Figure 3.1 illustrates an example of density-based clustering in which there are primarily three main clusters, and the sparse black points represent the outliers in the data. Similar to the nearest neighbor approach, while modeling is relatively easy, density-based clustering has a high computational complexity of O(N^2) [4].






![](Aspose.Words.865fb2c8-08d2-4415-8812-a02a1e9b05b1.002.png)

**Figure 3.1**



## ***Classification based approach***

The third approach to building an anomaly-based detection system using machine learning is classification. Classification models are trained with a dataset containing both normal and anomalous data. Next, the model is tested with new data and it predicts the label of the class which is either an anomaly or normal. There are two main classification approaches namely multi-class classification and binary-class classification. Multi-class classification is trained on data with several features as normal classes. Neural networks are an example of a multi-class classification algorithm. Neural networks are modeled after neurons in the human brain and can be used in anomaly detection as a means for understanding feature representation and anomaly scores [6]. Figure 6.1 offers an example of a possible deep learning framework for anomaly detection. The other main classification model is binary classification. Binary classification uses only normal labeled data in order to differentiate between normal cases and anomaly cases. An example of a binary classification algorithm is Support Vector Machine. As shown in figure 6.2 SVM produces a plane in the feature space and separates the data into two classes one which contains anomalies and the other which is the normal data. 








![](Aspose.Words.865fb2c8-08d2-4415-8812-a02a1e9b05b1.003.png)

**Figure 6.1**



![](Aspose.Words.865fb2c8-08d2-4415-8812-a02a1e9b05b1.004.png)

***Figure 6.2***




## ***Trends in anomaly detection*** 

Anomaly detection systems continue to evolve, and new iterations which overcome the weakness of former versions continue to be developed. For example, one weakness of current anomaly detection systems is the high-false positivity rate. Since anomaly-based detection systems look for any deviations from normal network traffic, many models tend to overfit the data causing high-false positives as the model cannot effectively generalize the data. In response, researchers have proposed combining deep learning with big data tools as a means to mitigate this concern [7]. Big data tools allow for larger training sets which in turn reduce the number of false positives as there is a larger set of normal cases. Figure 7.1 illustrates the general efficiency of deep learning techniques as the amount of data grows. Specifically for anomaly detection, as the number of IoT devices increases and, as a result, the number of network traffic, deep learning methods coupled with anomaly detection systems will be essential in preventing threats. 



![](Aspose.Words.865fb2c8-08d2-4415-8812-a02a1e9b05b1.005.png)

Figure 7.1 




## ***Conclusion*** 

Big data tools, specifically machine learning algorithms, play a vital role in modern anomaly-based intrusion detection systems. Nearest neighbor, density-based, and classification are common approaches to anomaly detection. While clustering models such as nearest neighbor and density-based techniques focus on grouping data to identify anomalies, classification labels the data in order to find anomalies. In addition, general trends indicate that the future of anomaly detection is a combination of deep learning and a larger training set made possible by big data tools. Overall, the paper examined the role of big data tools in anomaly-based intrusion detection systems and potential trends for the future. 









***References*** 


[1]  Hernandez, A. (n.d.). Cyber attacks on IOT devices are growing at alarming rates [encryption digest 64]. Venafi. Retrieved May 1, 2022, from https://www.venafi.com/blog/cyber-attacks-iot-devices-are-growing-alarming-rates-encryption-digest-64 

[2] *What is anomaly detection? definition & faqs - avi networks*. (n.d.). Retrieved May 1, 2022, from https://avinetworks.com/glossary/anomaly-detection/ 

[2.1] Alam, M. (2020, October 24). *k-Nearest Neighbors (kNN) for anomaly detection*. Medium. https://towardsdatascience.com/k-nearest-neighbors-knn-for-anomaly-detection-fdf8ee160d13


[3] Valcheva, S. (2018, February 21). *Anomaly Detection Algorithms: in Data Mining (With Comparison)*. Blog for Data-Driven Business. <https://www.intellspot.com/anomaly-detection-algorithms/>



[3.1] *DBSCAN Clustering in ML | Density based clustering*. (2019, May 6). GeeksforGeeks. https://www.geeksforgeeks.org/dbscan-clustering-in-ml-density-based-clustering/?ref=lbp

[4] Maurya, C. (2022, March). *(PDF) Anomaly Detection in Big Data*. ResearchGate. https://www.researchgate.net/publication/358996501\_Anomaly\_Detection\_in\_Big\_Data


[5] Wang, R., Zhu, Q., Luo, J., & Zhu, F. (2021). Local dynamic neighborhood based outlier detection approach and its framework for large-scale datasets. *Egyptian Informatics Journal*, *22*(2), 125–132. https://doi.org/10.1016/j.eij.2020.06.001


[6] Pang, G. (2020, July 10). *Deep Learning for Anomaly Detection: A Comprehensive Survey*. Medium. <https://towardsdatascience.com/a-comprehensive-survey-on-deep-learning-for-anomaly-detection-b1989b09ae38>

[6.1] Pang, G. (2020, July 10). *Deep Learning for Anomaly Detection: A Comprehensive Survey*. Medium. <https://towardsdatascience.com/a-comprehensive-survey-on-deep-learning-for-anomaly-detection-b1989b09ae38>

[6.2] Polzer, D. (2022, February 8). *A Comprehensive Beginners Guide to the Diverse Field of Anomaly Detection*. Medium. https://towardsdatascience.com/a-comprehensive-beginners-guide-to-the-diverse-field-of-anomaly-detection-8c818d153995#2751

[7] Al Jallad, K., Aljnidi, M., & Desouki, M. S. (2020). Anomaly detection optimization using big data and deep learning to reduce false-positive. *Journal of Big Data*, *7*(1). https://doi.org/10.1186/s40537-020-00346-1

[7.1] Al Jallad, K., Aljnidi, M., & Desouki, M. S. (2020). Anomaly detection optimization using big data and deep learning to reduce false-positive. *Journal of Big Data*, *7*(1). https://doi.org/10.1186/s40537-020-00346-1


