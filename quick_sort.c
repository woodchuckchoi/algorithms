#include <stdio.h>

int partition(int* arr, int l, int h) {
	int pivot = *(arr + h);
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
		partition(arr, l, pivot-1);
		partition(arr, pivot+1, h);
	}
}

int main() {
	int tmp[22] = {1,6,4,3,4,7,9,45,2,5,7,9,3,1,92,6,9,96,5,3,3, 100};
	quick_sort(tmp, 0, 21);
	for (int i = 0; i < 22; ++i) {
		printf("%d ", tmp[i]);
	}
	return 0;
}
