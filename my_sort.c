#include <stdio.h>

int partition(int* arr, int l, int h) {
	int pivot = *(arr + h);
	printf("Partition in progress. Pivot: %d\n", pivot);
	int i = l;
	int j = l;
	while (j < h) {
		if (*(arr + j) < pivot) {
			int tmp = *(arr + i);
			*(arr + i) = *(arr + j);
			*(arr + j) = tmp;
			++i;
		}
		++j;
	}
	*(arr + h) = *(arr + i);
	*(arr + i) = pivot;
	return i;
}

void quick_sort(int* arr, int l, int h) {
	if (l < h) {
		int pivot = partition(arr, l, h);
		printf("l: %d h: %d pivot: %d\n", l, h, pivot);
		quick_sort(arr, l, pivot-1);
		quick_sort(arr, pivot+1, h);
	}
}

int main() {
	int tmp[] = {1, 8, 3, 10, 4, 11, 92};
	quick_sort(tmp, 0, sizeof(tmp)/sizeof(tmp[0])-1);
	for (int i = 0; i < 7; ++i) {
		printf("%d ", tmp[i]);
	}
	return 0;
}
