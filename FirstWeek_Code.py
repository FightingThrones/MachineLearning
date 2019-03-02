#波士顿房价数据集-加载示例
#示例1：
# from sklearn.datasets import load_boston
# boston=load_boston()
# print(boston.data.shape)
#示例2：
from sklearn.datasets import load_boston
data,target=load_boston(return_X_y=True)
print(data.shape)
print(target.shape)

# #鸢尾花数据集-加载示例
# from sklearn.datasets import load_iris
# iris=load_iris()
# print(iris.data.shape)
# print(iris.target.shape)
# Target_names=list(iris.target_names)
# print(Target_names)

#            手写数字数据集
#手写数字数据集包括1797个0-9的手写数字数据,
# 每个数字由8*8大小的矩阵构成，矩阵中值的范围
# 是0-16,代表颜色的深度.
# 使用sklearn.datasets.load_digits即可加载相关数据集
# 其参数包括：
# .return_X_y:若为True，则以(data，target)形式返回
# (包括data和target);
# .n_class:表示返回数据的类别数,如:n_class=5,则返回
#  0到4的数据样本
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
digits=load_digits()
print(digits.data.shape)
print(digits.images.shape)
plt.matshow(digits.images[0])
plt.show()