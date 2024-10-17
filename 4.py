print("Введите последовательность чисел:")

def comb_sort(arr):
    n = len(arr)
    step = n
    while step > 1 or flag:
       if step > 1:
           step = int(step / 1.25)
       flag, i = False, 0
       while i + step < n:
          if arr[i] > arr[i + step]:
              arr[i], arr[i + step] = arr[i + step], arr[i]
              flag = True
          i += step
    return arr

numbers = list(map(int, input().strip().split()))

sorted_numbers = comb_sort(numbers)

print(' '.join(map(str, sorted_numbers)))
