#二分查找：要求数组是有序的，例如在arr数组里查找某个字key的位置
def BinarySearch(arr, key):
    min = 0
    max = len(arr) -1
    if key in arr:
        while True:
            center = int((min + max) / 2)#得到中位数
            if arr[center] > key:
               max = center - 1
            elif arr[center] < key:
               min = center + 1
            elif arr[center] == key:
               print(str(key) + "在数组里面的第" + str(center + 1) + "个位置")#不加1那第一个数的位置为0
               return arr[center]
    else:
       print("没有该数字")

if __name__ == '__main__':
    arr = [1, 6, 9, 15, 25, 26, 37, 48, 69, 90]
    while True:
        key = input("请输入你要查找的数字：")
        if key == " ":#输入空格结束查找，继续输入数字继续查找
            print("谢谢使用")
            break
        else:
            BinarySearch(arr, int(key))