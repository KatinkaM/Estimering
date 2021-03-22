from sklearn.datasets import load_iris

iris = load_iris()
print("Data set for training: ")
print(iris.data[0:29])
print("Data set for testing: ")
print(iris.data[129:149])
print(len(iris.data))