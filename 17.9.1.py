lst = input()
#В качестве задания повышенного уровня сложности
# можете выполнить проверку соответствия указанному в условии ввода данных.
if not lst.replace(' ', '').isdigit():
    print('Введены некорректные данные')
    exit(1)
try:
    n = int(input())
except ValueError:
    print('Введено некорректное значение n')
    exit(1)

lst = list(map(int, lst.split()))


def sort(array):
    for i in range(len(array)):
        for j in range(len(array) -i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.
def search(array, n, left, right):
    if n > array[-1] or n <= array[0]:
        print("В списке нет числа, удовлетворяющего условию")
        exit(0)
    if left > right:
        return False
    mid = (left + right) // 2
    print(left, right, mid)
    if array[mid + 1] >= n > array[mid]:
        return mid
    if array[mid] >= n:
        return search(array, n, left, mid - 1)
    if array[mid] < n:
        return search(array, n, mid + 1, right)


print(search(sort(lst), n, 0, len(lst) - 1))