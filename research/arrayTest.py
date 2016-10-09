import numpy as np

def test():
    array_a = np.array([0,1])
    print(array_a)
    print(array_a[0])
    array_b = np.array([[0,0],[0,1]])
    print(array_b)
    print(array_b[0][0])
    print(array_b[0][1])
    print(array_b[1][1])

if __name__ == "__main__":
    test()
