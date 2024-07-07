  # BIG ASSIGNMENT 2 DATA STRUCTURES | COMPARING SORT METHODS

## Visualized Bubble Sort Code Explanation: `TB2_BubbleSort.py`

### Import Module
- `import random`: Imports the `random` module to generate random data.
- `import matplotlib.pyplot as plt`: Imports `pyplot` from `matplotlib` for data visualization.
- `import matplotlib.animation as animation`: Imports `animation` from `matplotlib` to animate the visualization.
- `import easygui`: Imports `easygui` to create a simple GUI that allows users to enter data.
- `import time`: Imports the `time` module to measure execution time.

### Visualized Bubble Sort Function
- Defines the function `bubble_sort_visualized(arr)` which accepts an array `arr` as parameter:
  - `n = len(arr)`: Gets the length of the array.
  - `steps = []`: Initialize a list to store the sorting steps.
  - Outer looping `for i in range(n)`: Accesses each element of the array.
  - Inner looping `for j in range(0, n-i-1)`: Compares array elements.
  - `if arr[j] > arr[j+1]`: If the current element is greater than the next element, swap the elements.
  - `steps.append(arr.copy())`: Adds a copy of the current array into `steps`.
  - `return steps`: Returns the sorting steps.

### Update Fig Function
- Defines the function `update_fig(arr, rects, texts, start_time)` to update the visualization at each frame:
  - `elapsed_time = time.time() - start_time`: Calculates the elapsed time.
  - Looping to update the height and texts of each bar on the graph.
  - `ax.set_title(...)`: Updates the chart title with the elapsed time.

### User Interaction and Random Array Creation
- `num_indices = int(easygui.enterbox(...))`: Prompts the user to enter the number of indices.
- `value_range = int(easygui.enterbox(...))`: Prompts the user to enter the maximum value range.
- `arr = random.sample(range(1, value_range + 1), num_indices)`: Generates a random array based on user input.

### Time Measurement and Visualization
- `start_time = time.time()`: Stores the start time.
- `steps = bubble_sort_visualized(arr)`: Performs bubble sort while visualizing it.
- `end_time = time.time()`: Stores the end time.
- `elapsed_time = end_time - start_time`: Calculates the time taken for the sorting process.
- `print(...)`: Prints the time taken.

### Visualization Setup
- `plt.style.use('dark_background')`: Sets the visualization theme to dark background.
- `fig,ax = plt.subplots(...)`: Create subplots for the visualization.
- `colors = [plt.cm.viridis(i / len(arr)) for i in range(len(arr))]`: Set the color of the bar.
- `rects = ax.bar(...)`: Creates a bar on the chart based on the first step of sorting.
- `texts = [ax.text(...) for rect in rects]`: Adds text to each bar.
- `ax.set_xlim(0, len(arr))`, `ax.set_ylim(0, int(1.1 * max(arr)))`: Set the x and y limits on the graph.

### Animation and Display
- `ani = animation.FuncAnimation(...)`: Creates an animation by updating the graph at each frame.
- `plt.show()`: Display the visualization.


## Visualized Heap Sort Code Explanation: `TB2_HeepSort.py`

### Import Module
- `import random`: Imports the `random` module to generate random data.
- `import matplotlib.pyplot as plt`: Imports `pyplot` from `matplotlib` for data visualization.
- `import matplotlib.animation as animation`: Imports `animation` from `matplotlib` to animate the visualization.
- `import easygui`: Imports `easygui` to create a simple GUI that allows users to enter data.
- `import time`: Imports the `time` module to measure execution time.

### Heapify function
- `def heapify(arr, n, i, steps)`: Defines the `heapify` function to reset the heap.
  - `largest = i`: Sets the start index as the largest element.
  - `left = 2*i+1`: Calculates the left child index of the current element.
  - `right = 2 * i + 2`: Calculates the right child index of the current element.
  - `if left < n and arr[left] > arr[largest]`: If the left child is larger than the current largest element, update `largest`.
  - `if right < n and arr[right] > arr[largest]`: If the right child is larger than `largest`, update `largest`.
  - `if largest != i`: If `largest` is not the current element, swap and perform `heapify` recursion.

### Heap Sort Visualized function
- `def heap_sort_visualized(arr, steps)`: Defines the function to perform heap sort and visualization.
  - `n = len(arr)`: Get the length of the array.
  - Loop to build the heap.
  - Loop to extract elements one by one from the heap.
  - `steps.append(arr.copy())`: Adds a copy of the current array into `steps` after each exchange.

### Update Fig Function
- `def update_fig(arr, rects, texts, start_time)`: Defines a function to update the visualization at each frame.
  - `elapsed_time = time.time() - start_time`: Calculates the elapsed time.
  - Loop to update the height and text of each bar on the graph.
  - `ax.set_title(...)`: Updates the chart title with the elapsed time.

### User Interaction and Random Array Generation
- Prompts the user to input the number of indexes and the maximum index value constraint.
- Generates a random array based on user input.

### Time Measurement and Visualization
- Stores the start and end time.
- Calculates and prints the time required for the sorting process.

### Visualization Setup
- Set the visualization theme to dark background.
- Create subplots for visualization.
- Set the bar color.
- Create bars on the graph based on the first step of sorting.
- Add text to each bar.
- Set the x and y borders on the chart.

### Animation and Display
- Create an animation by updating the chart at each frame.
- Display the visualization.


## Visualized Insertion Sort Code Explanation: `TB2_InsertionSort.py`

### Import Module
- `import random`: Imports the `random` module to generate random data.
- `import matplotlib.pyplot as plt`: Imports `pyplot` from `matplotlib` for data visualization.
- `import matplotlib.animation as animation`: Imports `animation` from `matplotlib` to animate the visualization.
- `import easygui`: Imports `easygui` to create a simple GUI that allows users to enter data.
- `import time`: Imports the `time` module to measure execution time.

### Visualized Insertion Sort Function
- Defines the function `insertion_sort_visualized(arr)` which accepts an array `arr` as parameter:
  - `n = len(arr)`: Gets the length of the array.
  - `steps = []`: Initialize a list to store the sorting steps.
  - Looping `for i in range(1, n)`: Accesses each element of the array starting from the second element.
  - `key = arr[i]`: Stores the current element as the key.
  - `j = i - 1`: Initialize the variable `j` to compare the previous element.
  - Looping `while j >= 0 and key < arr[j]`: Moves the element larger than key one position forward from the current position.
  - `arr[j + 1] = key`: Places the key in the correct position.
  - `steps.append(arr.copy())`: Adds a copy of the current array into `steps`.
  - `return steps`: Returns the sorting steps.

### Update Fig Function
- Defines the function `update_fig(arr, rects, texts, start_time)` to update the visualization at each frame:
  - `elapsed_time = time.time() - start_time`: Calculates the elapsed time.
  - Looping to update the height and texts of each bar on the graph.
  - `ax.set_title(...)`: Updates the chart title with the elapsed time.

### User Interaction and Random Array Creation
- `num_indices = int(easygui.enterbox(...))`: Prompts the user to enter the number of indices.
- `value_range = int(easygui.enterbox(...))`: Prompts the user to enter the maximum value range.
- `arr = random.sample(range(1, value_range + 1), num_indices)`: Generates a random array based on user input.

### Time Measurement and Visualization
- `start_time = time.time()`: Stores the start time.
- `steps = insertion_sort_visualized(arr)`: Performs insertion sort while visualizing it.
- `end_time = time.time()`: Stores the end time.
- `elapsed_time = end_time - start_time`: Calculates the time taken for the sorting process.
- `print(...)`: Prints the time taken.

### Visualization Setup
- `plt.style.use('dark_background')`: Sets the visualization theme to dark background.
- `fig,ax = plt.subplots(...)`: Create subplots for the visualization.
- `colors = [plt.cm.viridis(i / len(arr)) for i in range(len(arr))]`: Set the color of the bar.
- `rects = ax.bar(...)`: Creates a bar on the chart based on the first step of sorting.
- `texts = [ax.text(...) for rect in rects]`: Adds text to each bar.
- `ax.set_xlim(0, len(arr))`, `ax.set_ylim(0, int(1.1 * max(arr)))`: Set the x and y limits on the graph.

### Animation and Display
- `ani = animation.FuncAnimation(...)`: Creates an animation by updating the graph at each frame.
- `plt.show()`: Display the visualization.


## Explanation of Merge Sort Visualized Code: `TB2_MergeSort.py`

### Import Modules
- `import random`: Imports the `random` module to generate random data.
- `import matplotlib.pyplot as plt`: Imports `pyplot` from `matplotlib` for data visualization.
- `import matplotlib.animation as animation`: Imports `animation` from `matplotlib` to create visualization animations.
- `import easygui`: Imports `easygui` for creating a simple GUI that allows the user to input data.
- `import time`: Imports the `time` module to measure execution time.

### Merge Sort Visualized Function
- `def merge_sort_visualized(arr, steps, left=0, right=None)`: Defines a function to perform merge sort and visualization.
  - `if right is None`: If `right` is not specified, set it to the length of the array.
  - `if right - left > 1`: If the sub-array has more than one element, proceed with division.
  - `mid = (left + right) // 2`: Determine the midpoint.
  - Recursively call `merge_sort_visualized` for the left and right sub-arrays.
  - Call the `merge` function to merge the sub-arrays.

### Merge Function
- `def merge(arr, steps, left, mid, right)`: Defines a function to merge two sub-arrays.
  - `L = arr[left:mid]` and `R = arr[mid:right]`: Split the array into two parts.
  - `i = j = 0` and `k = left`: Initialize indices for the left sub-array, right sub-array, and the merged array.
  - Loop to compare and merge elements from both sub-arrays.
  - Add remaining elements from the left or right sub-array if any.
  - `steps.append(arr.copy())`: Adds a copy of the current array to `steps` after each element addition.

### Update Fig Function
- `def update_fig(arr, rects, texts, start_time)`: Defines a function to update the visualization on each frame.
  - Calculate the elapsed time and update the graph's title.
  - Loop to update the height and text of each bar in the graph.

### User Interaction and Random Array Creation
- Ask the user to enter the number of indices and the maximum index value limit.
- Create a random array based on user input.

### Time Measurement and Visualization
- Store start and end times.
- Calculate and print the time taken for the sorting process.

### Visualization Setup
- Set the visualization theme to dark background.
- Create a subplot for visualization.
- Set bar colors.
- Create bars on the graph based on the first step of sorting.
- Add text to each bar.
- Set x and y limits on the graph.

### Animation and Display
- Create an animation by updating the graph on each frame.
- Display the visualization.


## Explanation of Quick Sort Visualized Code: `TB2_QuickSort.py`

### Import Modules
- `import random`: Imports the `random` module to generate random data.
- `import matplotlib.pyplot as plt`: Imports `pyplot` from `matplotlib` for data visualization.
- `import matplotlib.animation as animation`: Imports `animation` from `matplotlib` to create visualization animations.
- `import easygui`: Imports `easygui` for creating a simple GUI that allows the user to input data.
- `import time`: Imports the `time` module to measure execution time.

### Quick Sort Visualized Function
- `def quick_sort_visualized(arr, low, high, steps)`: Defines a function to perform quick sort and visualization.
  - `if low < high`: If the low index is smaller than the high index, proceed with the process.
  - `pi = partition(arr, low, high, steps)`: Call the `partition` function to get the pivot index.
  - Recursively call `quick_sort_visualized` for the left and right sub-arrays of the pivot.

### Partition Function
- `def partition(arr, low, high, steps)`: Defines a function to partition the array.
  - `pivot = arr[high]`: Set the last element as the pivot.
  - `i = low - 1`: Initialize the index of smaller element.
  - Loop to compare each element with pivot and swap if necessary.
  - Swap the pivot element to its correct position.
  - `steps.append(arr.copy())`: Adds a copy of the current array to `steps` after each swap.
  - Return the pivot index.

### Update Fig Function
- `def update_fig(arr, rects, texts, start_time)`: Defines a function to update the visualization on each frame.
  - Calculate the elapsed time and update the graph's title.
  - Loop to update the height and text of each bar in the graph.

### User Interaction and Random Array Creation
- Ask the user to enter the number of indices and the maximum index value limit.
- Create a random array based on user input.

### Time Measurement and Visualization
- Store start and end times.
- Calculate and print the time taken for the sorting process.

### Visualization Setup
- Set the visualization theme to dark background.
- Create a subplot for visualization.
- Set bar colors.
- Create bars on the graph based on the first step of sorting.
- Add text to each bar.
- Set x and y limits on the graph.

### Animation and Display
- Create an animation by updating the graph on each frame.
- Display the visualization.


## Explanation of Visualization Code for Selection Sort: `TB2_SelectionSort.py`

### Import Modules
- `import random`: Imports the `random` module to generate random data.
- `import matplotlib.pyplot as plt`: Imports `pyplot` from `matplotlib` for data visualization.
- `import matplotlib.animation as animation`: Imports `animation` from `matplotlib` to create visualization animations.
- `import easygui`: Imports `easygui` for creating a simple GUI that allows the user to input data.
- `import time`: Imports the `time` module to measure execution time.

### Selection Sort Visualized Function
- `def selection_sort_visualized(arr)`: Defines a function to perform selection sort and visualization.
  - `n = len(arr)`: Determine the length of the array.
  - `steps = []`: Initialize a list to store visualization steps.
  - Loop for each element in the array.
    - `min_idx = i`: Set the current minimum index.
    - Second loop to find the smallest element in the remaining array.
      - If a smaller element is found, update `min_idx`.
    - Swap the current element with the smallest found element.
    - `steps.append(arr.copy())`: Adds a copy of the current array to `steps`.
  - Return `steps` containing visualization steps.

### Update Fig Function
- `def update_fig(arr, rects, texts, start_time)`: Defines a function to update the visualization on each frame.
  - `elapsed_time = time.time() - start_time`: Calculate the elapsed time.
  - Loop to update the height and text of each bar in the graph.
  - `ax.set_title(...)`: Update the graph's title with the elapsed time.

### User Interaction and Random Array Creation
- `num_indices = int(easygui.enterbox(...))`: Ask the user to enter the number of indices.
- `value_range = int(easygui.enterbox(...))`: Ask the user to enter the maximum index value limit.
- `arr = random.sample(range(1, value_range + 1), num_indices)`: Create a random array based on user input.

### Time Measurement and Visualization
- `start_time = time.time()`: Store the start time.
- `steps = selection_sort_visualized(arr)`: Perform selection sort and store visualization steps.
- `end_time = time.time()`: Store the end time.
- `elapsed_time = end_time - start_time`: Calculate the time taken for the sorting process.
- `print(...)`: Print the time taken for the sorting process.

### Visualization Setup
- `plt.style.use('dark_background')`: Set the visualization theme to dark background.
- `fig, ax = plt.subplots(...)`: Create a subplot for visualization.
- `colors = [...]`: Set bar colors based on the length of the array.
- `rects = ax.bar(...)`: Create bars on the graph based on the first step of sorting.
- `texts = [...]`: Add text to each bar.
- `ax.set_xlim(0, len(arr))` and `ax.set_ylim(0, int(1.1 * max(arr)))`: Set x and y limits on the graph.

### Animation and Display
- `ani = animation.FuncAnimation(...)`: Create an animation by updating the graph on each frame.
- `plt.show()`: Display the visualization.
