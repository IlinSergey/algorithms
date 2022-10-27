def binary_search(list, item):
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = (low + hight) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            hight = mid -1
        else:
            low = mid + 1
    return None

item_list = [0, 11, 2, 5, 8 ,7, 11, -1]

print(binary_search(item_list, 2))


