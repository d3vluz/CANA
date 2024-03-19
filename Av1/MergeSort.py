"""
    CÓDIGO EM PHYTON
        FEITO: EVANDRO LUZ
        ANALISADO: ?
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide a lista ao meio
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente ordena cada metade
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combina as metades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Combina as duas listas enquanto houver elementos em ambas
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adiciona os elementos restantes de left, se houver
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Adiciona os elementos restantes de right, se houver
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Caso teste.
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print("Lista ordenada:", sorted_arr)