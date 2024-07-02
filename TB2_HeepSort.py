import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import easygui
import time

def heapify(arr, n, i, steps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps.append(arr.copy())
        heapify(arr, n, largest, steps)

def heap_sort_visualized(arr, steps):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, steps)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps.append(arr.copy())
        heapify(arr, i, 0, steps)

def update_fig(arr, rects, texts, start_time):
    elapsed_time = time.time() - start_time
    for rect, val, text in zip(rects, arr, texts):
        rect.set_height(val)
        text.set_text(val)
        text.set_y(val + 1)
    ax.set_title(f"Visualisasi Heap Sort | Waktu berlalu: {elapsed_time:.2f} detik", fontsize=20, color='white')

num_indices = int(easygui.enterbox("Masukkan jumlah indeks yang akan diacak:"))
value_range = int(easygui.enterbox("Masukkan batasan nilai maksimum indeks:"))

arr = random.sample(range(1, value_range + 1), num_indices)

start_time = time.time()
steps = []
heap_sort_visualized(arr, steps)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Waktu yang dibutuhkan untuk proses sorting: {elapsed_time:.4f} detik")

plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 8))

colors = [plt.cm.viridis(i / len(arr)) for i in range(len(arr))]

rects = ax.bar(range(len(arr)), steps[0], align="edge", color=colors)

texts = [ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height(), str(rect.get_height()),
                 ha='center', va='bottom', color='white') for rect in rects]

ax.set_xlim(0, len(arr))
ax.set_ylim(0, int(1.1 * max(arr)))

ani = animation.FuncAnimation(
    fig, update_fig, frames=steps, fargs=(rects, texts, start_time), interval=50, repeat=False
)

plt.show()
