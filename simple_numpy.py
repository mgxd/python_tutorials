import numpy as np

# set a random seed so that the same numbers alway come up
np.random.seed(3) 
 
# create some dummy data using numpy
# add .T at the end of numpy objects to transpose them
# X constitutes the feature space, y will constitute the responses
# below we create a 10 by 7 matrix
X = np.array([np.random.normal(size=5) for x in range(7)]).T
y = np.random.normal(size=5)

# you can figure out the dimensions of any numpy array 
print(X.shape, y.shape)

# indexing numpy arrays
# index a column using X[first_dimension, second_dimension]
# X[:,:] will give you the entire matrix, it is equivalent to X
# you can also specify ranges for indexing
# index rows 1 to 3, column 4
X[:3, 3]

# single index will give you a row
X[2]

# numpy is "vectorized"
# so indexing a single column on its own will look like a row vector
X[:, 2]

# compute the sum, column wise
X.sum(0)

# compute the sum, row wise
X.sum(1)

# other operations are similar
print(X.min(0), X.max(1))

# if you want to turn a multi dimensional array or matrix into a single "list" like thing
X.flatten()

# numpy also has a bunch of nice functions, or methods
# compute covariance and correlation matrices of X
np.corrcoef(X)
np.cov(X)
