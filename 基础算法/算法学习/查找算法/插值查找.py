#待查找列表需有序，是基于二分法查按照，将查找点的u西安则改进为自适应选择的查找法
#对比二分法，即采用value = (key -list[low])/(list[high] - list[low])代替1/2
def Bin_Search(lis, key):
    low = 0
    high = len(lis) - 1
    time = 0
    while low < high:
        time += 1
        mid = low + int((high-low) * (key -lis[low])/(lis[high] - lis[low]))
        print("mid =% s, low =% s, high =% s" % (mid, low, high))
        if key < lis[mid]:
            high = mid - 1
        elif key >lis[mid]:
            low = mid + 1
        else:
            print("times: %s" %time)
            return mid
        print("times: %s" %time)
        return False
if __name__ == "__main__":
    LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
    result = Bin_Search(LIST, 444)
    print(result)