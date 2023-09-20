
from sklearn.datasets import fetch_openml


#download training data

print("Downloading data...")
mnist = fetch_openml('mnist_784', version=1)
print("...download complete")
print(mnist.keys())

x, y = mnist['data'], mnist['target']

x_train, x_test, y_train, y_test = x[:6000], x[6000:],y[:6000], y[6000:]

y_train_5 = (y_train == '5')

#creating stochastic gradient descent classifier
#from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
sgd_clf = SVC( gamma="auto" )


print("starting training...")
sgd_clf.fit(x_train, y_train_5)
print("...training complete!")


#testing single input

print(sgd_clf.predict([x_train.iloc[0]]))

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

some_number = np.array(x_train.iloc[0])
image = some_number.reshape(28,28)

plt.imshow(image, cmap='binary')
plt.axis('off')
plt.show()

#cross validation

from sklearn.model_selection import StratifiedKFold
from sklearn.base import clone

skfolds = StratifiedKFold( n_splits = 3, shuffle = True, random_state = 42)

for train_index, test_index in skfolds.split(x_train, y_train_5):
    clone_clf = clone(sgd_clf)

    x_train_folds = x_train.loc[train_index]
    y_train_folds = y_train_5.loc[train_index]
    x_test_fold = x_train.loc[test_index]
    y_test_fold = y_train_5.loc[test_index]

    clone_clf.fit(x_train_folds,y_train_folds)
    y_pred = clone_clf.predict(x_test_fold)
    n_correct = sum( y_pred == y_test_fold )
    print(n_correct / len(y_pred))


from sklearn.base import BaseEstimator
import numpy
from sklearn.model_selection import cross_val_score
class MeValeMLV(BaseEstimator):
    def fit(self, X,y=None):
        return self

    def predict(self, X):
        return np.zeors((len(X),1),dtype=bool)

mvl=MeValeMLV()
cross_val_score(mvl,x_train,y_train_5,cv=3,scoring='acurracy')


from sklearn.model_selection import cross_val_predict

y_train_pred=cross_val_predict(sgd_clf, y)
