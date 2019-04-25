# Sort

|                          Name                           |                     Best                      |         Average         |                      Worst                       |                            Memory                            |                           Stable                            |    Method    |                         Other notes                          |
| :-----------------------------------------------------: | :-------------------------------------------: | :---------------------: | :----------------------------------------------: | :----------------------------------------------------------: | :---------------------------------------------------------: | :----------: | :----------------------------------------------------------: |
|             [Bubble Sort](#1.1 Bubble Sort)             |                   $O(n^2)$                    |        $O(n^2)$         |                     $O(n^2)$                     |                            $O(1)$                            |                            稳定                             |  Exchanging  |                                                              |
|    [Improved Bubble Sort](#1.2 Improved Bubble Sort)    |                    $O(n)$                     |        $O(n^2)$         |                     $O(n^2)$                     |                            $O(1)$                            |                            稳定                             |  Exchanging  |                                                              |
|              [Quick Sort](#1.3 Quick Sort)              |                 $O(nlog_2n)$                  |      $O(nlog_2n)$       |                     $O(n^2)$                     |              Average $O(log_2n)$  Worst $O(n)$               | Typical in-place sort is not stable; stable versions exist. | Partitioning | Quicksort is usually done in-place with *O*(log *n*) stack space. |
| [Straight Insertion Sort](#2.1 Straight Insertion Sort) |                    $O(n)$                     |        $O(n^2)$         |                     $O(n^2)$                     |                            $O(1)$                            |                            稳定                             |  Insertion   |                                                              |
|   [Binary Insertion Sort](#2.2 Binary Insertion Sort)   |                 $O(nlog_2n)$                  |        $O(n^2)$         |                     $O(n^2)$                     |                            $O(1)$                            |                            稳定                             |  Insertion   |                                                              |
|            [Shell's Sort](#2.3 Shell's Sort)            |                   $nlog_2n$                   | Depends on gap sequence | Depends on gap sequence; best known is $n^{4/3}$ |                            $O(1)$                            |                           不稳定                            |  Insertion   |                                                              |
|          [Selection Sort](#3.1 Selection Sort)          |                   $O(n^2)$                    |        $O(n^2)$         |                     $O(n^2)$                     |                            $O(1)$                            |                           不稳定                            |  Selection   |  Stable with $O(n)$ extra space or when using linked lists.  |
|               [Heap Sort](#3.2 Heap Sort)               | $O(n)$ If all keys are distinct, $O(nlog_2n)$ |      $O(nlog_2n)$       |                   $O(nlog_2n)$                   |                            $O(1)$                            |                           不稳定                            |  Selection   |                                                              |
|               [Merge Sort](#4 Merge Sort)               |                 $O(nlog_2n)$                  |      $O(nlog_2n)$       |                   $O(nlog_2n)$                   | $O(n)$ A hybrid [block merge sort](https://en.wikipedia.org/wiki/Block_sort) is $O(1)$ mem. |                            稳定                             |    Merge     |                                                              |
|                  Radix Sort(基数排序)                   |                                               |     $$O(d(n+r_d))$$     |                                                  |                          $$O(r_d)$$                          |                            稳定                             |              |                                                              |

|      $n$       |         $d$          |            $r_d$             |
| :------------: | :------------------: | :--------------------------: |
| 序列中关键字数 | 关键字位数(930, d=3) | 构成关键字的符号数($r_d=10$) |

## 1 Swap

### 1.1 Bubble Sort

```c++
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

[**Back to Top**](#Sort)

### 1.2 Improved Bubble Sort

```c++
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

[**Back to Top**](#Sort)

### 1.3 Quick Sort

```c++
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

[**Back to Top**](#Sort)

----

## 2 Insertion

### 2.1 Straight Insertion Sort

```c++
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

[**Back to Top**](#Sort)

### 2.2 Binary Insertion Sort

```c++
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

[**Back to Top**](#Sort)

### 2.3 Shell's Sort

``` c++
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

[**Back to Top**](#Sort)

----

## 3 Selection

### 3.1 Selection Sort

```c++
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

[**Back to Top**](#Sort)

### 3.2 Heap Sort

```c++
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

[**Back to Top**](#Sort)

---

## 4 Merge Sort

```c++
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

[**Back to Top**](#Sort)

## References

> 1. 天勤计算机考研高分笔记系列2020版数据结构
> 2. [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)

