#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_mldata
from chainer import cuda, Variable, FunctionSet, optimizers
import chainer.functions as F
import sys

plt.style.use('ggplot')

batchsize = 100

n_epoch   = 20

n_units   = 1000

print 'fetch MNIST dataset'
mnist = fetch_mldata('MNIST original')

mnist.data    = mnist.data.astype(np.float32)
mnist.data   /= 255

mnist.target = mnist.target.astype(np.int32)

def draw_digit(data):
    size = 28
    plt.figure(figsize=(2.5,3))

    X, Y = np.meshgrid(range(size), range(size))
    Z = data.reshape(size, size)
    Z = Z[::-1,:]
    plt.xlim(0,27)
    plt.ylim(0,27)
    plt.pcolor(X,Y,Z)
    plt.gray()
    plt.tick_params(labelbottom="off")
    plt.tick_params(labelleft="off")

    plt.show()

#draw_digit(mnist.data[5])
#draw_digit(mnist.data[12345])
#draw_digit(mnist.data[33456])

N = 60000
x_train, x_test = np.split(mnitst.data, [N])
y_train, y_test = np.split(mnist.traget, [N])
N_test = y_test.size

model = FunctionSet(l1=F.Linear(784, n_units),
                    l2=F.Linear(n_units, n_units),
                    l3=F.Linear(n_units, 10))

def forward(x_data, y_data, train=True):
    x, t = Variable(x_data), Variable(y_data)
    h1 = F.dropout(F.relu(model.l1(x)), train=train)
    h2 = F.dropout(F.relu(model.l2(h1)), train=train)
    y = model.l3(h2)

    return F.softmax_cross_entropy(y, t), F.accuracy(y, t)
