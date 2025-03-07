import random
import time
import sys

# Ensure UTF-8 encoding for Windows consoles
sys.stdout.reconfigure(encoding='utf-8')

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def measure_time(sort_function, arr):
    start_time = time.perf_counter()
    sort_function(arr.copy())
    end_time = time.perf_counter()
    return end_time - start_time

# Generate random datasets
small_dataset = [random.randint(1, 1000) for _ in range(50)]
large_dataset = [random.randint(1, 10000) for _ in range(1000)]

# Measure performance
bubble_time_small = measure_time(bubble_sort, small_dataset)
selection_time_small = measure_time(selection_sort, small_dataset)
bubble_time_large = measure_time(bubble_sort, large_dataset)
selection_time_large = measure_time(selection_sort, large_dataset)
built_in_time_large = measure_time(sorted, large_dataset)

# Print results
print("\n[INFO] Small Dataset (50 product weights):")
print(f"✅ Bubble Sort took {bubble_time_small:.6f} seconds.")
print(f"✅ Selection Sort took {selection_time_small:.6f} seconds.")

print("\n[INFO] Large Dataset (1000 product weights):")
print(f"⚠️ Bubble Sort took {bubble_time_large:.6f} seconds.")
print(f"✅ Selection Sort took {selection_time_large:.6f} seconds.")
print(f"🚀 Python Built-in Sort took {built_in_time_large:.6f} seconds.")
