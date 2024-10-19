def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1



def test_binary_search_found():
    arr = [1, 2, 3,4, 5, 6]
    target = 5
    result = binary_search(arr, target)
    assert result == 4, f"Valor Esperado 4, resultado {result}"

def test_binary_search_invalidparameter():
    arr = [1, 3, 5, 7, 9, 11]
    target = "a"
    result = binary_search(arr, target)
    assert type(result) is int, f"Valor esperado inteiro, no entanto {target}"

# You can call the test functions to run them
test_binary_search_found()
test_binary_search_invalidparameter()
