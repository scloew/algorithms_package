from operator import lt
from random import randint


def merge_sort(list_, reverse=False, compare=lt):
  sub_lists = [[i] for i in list_]
  while len(sub_lists) > 1:
    sub_lists = [_merge(sub_lists[i], sub_lists[i + 1], compare) for i in range(0, len(sub_lists) - 1, 2)] \
                + ([sub_lists[-1]] if len(sub_lists) % 2 else [])
  return sub_lists[0][::-1] if reverse else sub_lists[0]


def _merge(list_1, list_2, compare=lt):
  merged, i, j = [], 0, 0
  while i < len(list_1) and j < len(list_2):
    if compare(list_1[i], list_2[j]):
      merged.append(list_1[i])
      i += 1
    else:
      merged.append(list_2[j])
      j += 1
  return merged + list_1[i:] + list_2[j:]


if __name__ == "__main__":
  print(help(merge_sort))
  print('hello sortss')
  lst = [randint(-500, 500) for _ in range(14)]
  sorted = merge_sort(lst, reverse=True)
  print('original list:= ', lst)
  print('merge sort:=    ', sorted)
  lst.sort(reverse=True)
  print('truth value:=   ', lst)
  print('algorithm correct:=', lst == sorted)

  ##test custome compare function
  lst_two = [{i: randint(-25, 25) for i in range(randint(2, 5))} for _ in range(10)]
  my_compare = lambda dict_one, dict_two: True if len(dict_one) < len(dict_two) else False
  print('original list:= ', lst_two)
  print('sorted list:=   ', merge_sort(lst_two, compare=my_compare))
