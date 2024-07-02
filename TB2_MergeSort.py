import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import easygui
import time

def merge_sort_visualized(arr, steps, left=0, right=None):
    if right is None:
        right = len(arr)
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort_visualized(arr, steps, left, mid)
        merge_sort_visualized(arr, steps, mid, right)
        merge(arr, steps, left, mid, right)

def merge(arr, steps, left, mid, right):
    L = arr[left:mid]
    R = arr[mid:right]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        steps.append(arr.copy())
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        steps.append(arr.copy())
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        steps.append(arr.copy())

def update_fig(arr, rects, texts, start_time):
    elapsed_time = time.time() - start_time
    for rect, val, text in zip(rects, arr, texts):
        rect.set_height(val)
        text.set_text(val)
        text.set_y(val + 1)
    ax.set_title(f"Visualisasi Merge Sort | Waktu berlalu: {elapsed_time:.2f} detik", fontsize=20, color='white')

num_indices = int(easygui.enterbox("Masukkan jumlah indeks yang akan diacak:"))
value_range = int(easygui.enterbox("Masukkan batasan nilai maksimum indeks:"))

arr = random.sample(range(1, value_range + 1), num_indices)

start_time = time.time()
steps = []
merge_sort_visualized(arr, steps)
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
