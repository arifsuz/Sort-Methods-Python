import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import easygui
import time

def quick_sort_visualized(arr, low, high, steps):
    if low < high:
        pi = partition(arr, low, high, steps)
        quick_sort_visualized(arr, low, pi - 1, steps)
        quick_sort_visualized(arr, pi + 1, high, steps)

def partition(arr, low, high, steps):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            steps.append(arr.copy())
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps.append(arr.copy())
    return i + 1

def update_fig(arr, rects, texts, start_time):
    elapsed_time = time.time() - start_time
    for rect, val, text in zip(rects, arr, texts):
        rect.set_height(val)
        text.set_text(val)
        text.set_y(val + 1)
    ax.set_title(f"Visualisasi Quick Sort | Waktu berlalu: {elapsed_time:.2f} detik", fontsize=20, color='white')

num_indices = int(easygui.enterbox("Masukkan jumlah indeks yang akan diacak:"))
value_range = int(easygui.enterbox("Masukkan batasan nilai maksimum indeks:"))

arr = random.sample(range(1, value_range + 1), num_indices)

start_time = time.time()
steps = []
quick_sort_visualized(arr, 0, len(arr) - 1, steps)
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
