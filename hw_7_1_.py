"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
 Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте
 алгоритм (сделайте его умнее)."""
# def selection_sort(array_to_sort):
#     a = array_to_sort
#     for i in range(len(a)):
#         idx_min = i
#         for j in range(i+1, len(a)):
#             if a[j] < a[idx_min]:
#                 idx_min = j
#         tmp = a[idx_min]
#         a[idx_min] = a[i]
#         a[i] = tmp
#     return a
#
#
# ary = [0,3,5,1,2,3,5,4,2,34,43,24]
# print(selection_sort(ary))

def random_list():
    import random
    par_1 = int(input(f'Введите нижнюю границу диапазона: '))
    par_2 = int(input(f'Введите верхнюю границу диапазона: '))
    par_3 = int(input(f'Введите кол-во чисел в списке: '))
    list = []
    for i in range(par_3):
        list.append(random.randint(par_1, par_2))
    return list


li = random_list()
n = 1
while n < len(li):
     for i in range(len(li)-n):
          if li[i] > li[i+1]:
               li[i],li[i+1] = li[i+1],li[i]
     n += 1
print(li)

