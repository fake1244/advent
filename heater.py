

def heat():
    arr = [0] * 8000
    for i in range(10000):
        for j in range(len(arr)):
            arr[j] *= 5
            # arr[j] /= 5
        print("added 1")

if __name__ == '__main__':
    heat()