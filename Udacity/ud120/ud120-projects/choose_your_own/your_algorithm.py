#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, fitAndPlot

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn import tree
clf_dt = tree.DecisionTreeClassifier(min_samples_split=40)
fitAndPlot(clf_dt, features_train, labels_train, features_test, labels_test, "dt")

from sklearn import neighbors
clf_kn = neighbors.KNeighborsClassifier(n_neighbors=3)
fitAndPlot(clf_kn, features_train, labels_train, features_test, labels_test, "kn")

from sklearn import ensemble
clf_rf = ensemble.RandomForestClassifier(n_estimators=10)
fitAndPlot(clf_rf, features_train, labels_train, features_test, labels_test, "rf")

from sklearn import ensemble
clf_adab = ensemble.AdaBoostClassifier(n_estimators=100)
fitAndPlot(clf_adab, features_train, labels_train, features_test, labels_test, "adab")

from sklearn.naive_bayes import GaussianNB
clf_nb = GaussianNB()
fitAndPlot(clf_nb, features_train, labels_train, features_test, labels_test, "nb")

from sklearn.svm import SVC
clf_svc = SVC(kernel="rbf",C=10000)
fitAndPlot(clf_svc, features_train, labels_train, features_test, labels_test, "svc")