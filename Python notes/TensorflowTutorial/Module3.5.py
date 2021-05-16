from __future__ import absolute_import, division, print_function, unicode_literals

# Complex Arrays
import numpy as np

# Loading/Viewing datasets
import pandas as pd

# Visualizes graphs and charts
import matplotlib.pyplot as plt

# Clears output
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf

# ________________________________________________

# Load dataset.
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
# print(dftrain.head())
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')
# print(dftrain.head())
# Name: 0, dtype: object 0 <- he did not survive
# print(dftrain.loc[0], y_train.loc[0])
# print(dftrain["age"])

# print(dftrain.describe())

# print(dftrain.shape)

# _________________________________________

# dftrain.age.hist(bins=20)
# dftrain.sex.value_counts().plot(kind='barh')
# dftrain['class'].value_counts().plot(kind='barh')
# pd.concat([dftrain, y_train], axis=1).groupby('sex').survived.mean().plot(kind='barh').set_xlabel('% survive')
# plt.show()



                    # LINEAR REGRESSION EXAMPLE
#__________________________________________

# Categorical Data is NOT numeric
CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']

# Numeric IS numeric
NUMERIC_COLUMNS = ['age', 'fare']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = dftrain[feature_name].unique()  # gets a list of all unique values from given feature column
  # For 'sex", it would be male and female ^
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(feature_columns)

# _______________________________________________________

#           Definitions
# Epoch: The number of times you feed the model the same information
# Overfitting: Too many Epochs, to the point it just memorizes the datapoints

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():  # inner function, this will be returned
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))  # create tf.data.Dataset object with data and its label
    if shuffle:
      ds = ds.shuffle(1000)  # randomize order of data
    ds = ds.batch(batch_size).repeat(num_epochs)  # split dataset into batches of 32 and repeat process for number of epochs
    return ds  # return a batch of the dataset
  return input_function  # return a function object for use

train_input_fn = make_input_fn(dftrain, y_train)  # here we will call the input_function that was returned to us to get a dataset object we can feed to the model
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

#           Creating The Model
# We create a linear estimtor by passing the feature columns we created earlier
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)

#           Training The Model
linear_est.train(train_input_fn)  # train
result = linear_est.evaluate(eval_input_fn)  # get model metrics/stats by testing on testing data

clear_output()  # clears console output
print(result['accuracy'])  # the result variable is simply a dict of stats about our model
print(result)

result = list(linear_est.predict(eval_input_fn))
print(dfeval.loc[2])
# [1] is chance of survival. Probabilities has 2 values
print(result[2]['probabilities'][1])
