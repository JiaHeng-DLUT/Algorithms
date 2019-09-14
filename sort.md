# Sorting algorithm

## 0 Sorting algorithm table 

| Name | Best | Average | Worst | Memory | Stable | Method | Other notes |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Bubble Sort | $$O(n^2)$$  | $$O(n^2)$$  | $$O(n^2)$$  | $$O(1)$$  | 稳定 | Exchanging |  |
| Improved Bubble Sort | $$O(n)$$  | $$O(n^2)$$  | $$O(n^2)$$  | $$O(1)$$  | 稳定 | Exchanging |  |
| Quick Sort | $$O(n\log n)$$  | $$O(n\log n)$$ | $$O(n^2)$$  | Average $$O(\log n)$$. Worst $$O(n)$$. Non-recursive: $$O(1)$$.  | Typical in-place sort is not stable; stable versions exist. | Partitioning | Quick sort is usually done in-place with $$O(\log n)$$ stack space. |
| Straight Insertion Sort | $$O(n)$$ | $$O(n^2)$$  | $$O(n^2)$$  | $$O(1)$$ | 稳定 | Insertion |  |
| Binary Insertion Sort | $$O(n\log n)$$ | $$O(n^2)$$  | $$O(n^2)$$  | $$O(1)$$ | 稳定 | Insertion |  |
| Shell's Sort | $$O(n\log n)$$ | Depends on gap sequence | Depends on gap sequence; best known is $$n^{4/3}$$  | $$O(1)$$ | 不稳定 | Insertion |  |
| Selection Sort | $$O(n^2)$$  | $$O(n^2)$$  | $$O(n^2)$$  | $$O(1)$$ | 不稳定 | Selection | Stable with $$O(n)$$ extra space or when using linked lists. |
| Heap Sort | $$O(n)$$ If all keys are distinct, $$O(n\log n)$$ | $$O(n\log n)$$ | $$O(n\log n)$$ | $$O(1)$$ | 不稳定 | Selection |  |
| Merge Sort | $$O(n\log n)$$ | $$O(n\log n)$$ | $$O(n\log n)$$ | $$O(n)$$. Non-recursive: $$O(1)$$.  | 稳定 | Merge |  |
| Radix Sort \(基数排序\) |  | $$O(d(n+r_d))$$  |   | $$O(r_d)$$  | 稳定 |  |  |

| n | d | r\_d |
| :---: | :---: | :---: |
| 序列中关键字数 | 关键字位数 \( $$930, d=3$$ \) | 构成关键字的符号数 \( $$r_d=10$$ \) |

## 1 Swap

### 1.1 Bubble Sort

```cpp
void bubbleSort(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}
```

### 1.2 Improved Bubble Sort

```cpp
void bubbleSort(int *arr, int n) {
    bool isEnd = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                isEnd = false;
            }
        }
        if (isEnd) {
            return;
        }
    }
}
```

### 1.3 Quick Sort

```cpp
void quickSort(int arr[], int low, int high) {
    int temp;
    int l = low, r = high;
    if (low < high) {
        temp = arr[low];
        while (l < r) {
            while (arr[r] >= temp && l < r) {
                r--;
            }
            if (l < r) {
                arr[l] = arr[r];
                l++;
            }
            while (arr[l] <= temp && l < r) {
                l++;
            }
            if (l < r) {
                arr[r] = arr[l];
                r--;
            }
        }
        arr[l] = temp;
        quickSort(arr, low, l);
        quickSort(arr, l + 1, high);
    }
}
```

## 2 Insertion

### 2.1 Straight Insertion Sort

```cpp
void insertionSort(int* arr, int n) {
    int i, j;
    for (i = 1; i < n; i++) {
        int temp = arr[i];
        for (j = i - 1; j >= 0; j--) {
            if (arr[j] > temp) {
                arr[j + 1] = arr[j];
            }
            else {
                break;
            }
        }
        arr[j + 1] = temp;
    }
}
```

### 2.2 Binary Insertion Sort

```cpp
void binaryInsertionSort(int* arr, int n) {
    for (int i = 1; i < n; i++) {
        int temp = arr[i];
        int low = 0, high = i - 1;
        while (low <= high) {
            int m = (low + high) / 2;
            if (arr[m] <= temp) {
                low = m + 1;
            }
            else {
                high = m - 1;
            }
        }
        for (int j = i; j > low; j--) {
            arr[j] = arr[j - 1];
        }
        arr[low] = temp;
    }
}
```

### 2.3 Shell's Sort

```cpp
void shellInsert(int array[], int n, int dk) {
    int i, j, temp;
    for (i = dk; i < n; i++) {
        temp = array[i];
        for (j = i - dk; (j >= i % dk) && array[j] > temp; j -= dk) {
            array[j + dk] = array[j];
        }
        array[j + dk] = temp;
    }
}

void shellSort(int array[], int n) {
    int t = (int)(log(n - 1) / log(2));
    for (int i = 1; i < t; i++) {
        int dk = (int)((1 << (t - i)) + 1);
        shellInsert(array, n, dk);
    }
    shellInsert(array, n, 1);
}
```

## 3 Selection

### 3.1 Selection Sort

```cpp
void selectionSort(int* arr, int n) {
    for (int i = n - 1; i > 0; i--) {
        int pos = 0;
        for (int j = 1; j <= i; j++) {
            if (arr[j] > arr[pos]) {
                pos = j;
            }
        }
        swap(arr[pos], arr[i]);
    }
}
```

### 3.2 Heap Sort

```cpp
void sift(int arr[], int low, int high) {
    int i = low, j = 2 * i + 1;
    int temp = arr[i];
    while (j <= high) {
        if (j < high && arr[j] < arr[j + 1]) {
            ++j;
        }
        if (temp < arr[j]) {
            arr[i] = arr[j];
            i = j;
            j = 2 * i + 1;
        }
        else {
            break;
        }
    }
    arr[i] = temp;
}

void heapSort(int arr[],int n) {
    for (int i = n / 2 - 1; i >= 0; --i) {
        sift(arr, i, n);
    }
    for (int i = n - 1; i >= 1; --i) {
        swap(arr[0], arr[i]);
        sift(arr, 0, i - 1);
    }
}
```

## 4 Merge Sort

```cpp
void merge(int arr[], int low, int m, int high) {
    int i = low, j = m + 1;
    while (i <= m && j <= high) {
        if (arr[i] <= arr[j]) {
            i++;
        }
        else {
            int temp = arr[j];
            for (int k = j; k > i; --k) {
                arr[k] = arr[k - 1];
            }
            arr[i] = temp;
            j++;
        }
    }
}

void mergeSort(int arr[], int low, int high) {
    if (low < high) {
        int m = (low + high) / 2;
        mergeSort(arr, low, m);
        mergeSort(arr, m + 1, high);
        merge(arr, low, m, high);
    }
}
```

## References

> 1. 天勤计算机考研高分笔记系列2020版数据结构
> 2. [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)

