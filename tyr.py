import numpy as np
# with_mask = with_mask.reshape(200,50*50*3)

# withoutMask = withoutMask.reshape(200,50*50*3)
# # print(with_mask.shape)
# print("----------------------")

# print(withoutMask.shape)
with_mask = np.load('with_mask.npy')
withoutMask = np.load('with_Outmask.npy')
# print(with_mask.shape)
# print(withoutMask.shape)
with_mask = with_mask.reshape(200,50*50*3)
withoutMask = withoutMask.reshape(200, 50*50*3)
# print(with_mask.shape)
# print(withoutMask.shape)
X = np.r_[with_mask, withoutMask]
# print('---------------')
# print(X.shape)

labels = np.zeros(X.shape[0])
labels[200:] = 1.0

from sklearn.svm import SVC
fro sklearn.met