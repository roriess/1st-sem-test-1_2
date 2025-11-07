def bin_search(xs: list[int], x: int):
    left = 0
    right = len(xs) - 1

    while left < right:
        mid = (left + right) // 2

        if xs[mid] == x:
            return mid
        
        if xs[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return left if left < len(xs) and xs[left] == x else -1 