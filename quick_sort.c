/* C implementation QuickSort */
#include<stdio.h> 
  
// A utility function to swap two elements 
void swap(int* a, int* b) 
{ 
    int t = *a; 
    *a = *b; 
    *b = t; 
} 
  
/* This function takes last element as pivot, places 
   the pivot element at its correct position in sorted 
    array, and places all smaller (smaller than pivot) 
   to left of pivot and all greater elements to right 
   of pivot */
int partition (int arr[], int low, int high) 
{ 
    int pivot = arr[high];    // pivot 
    int i = (low - 1);  // Index of smaller element 
  
    for (int j = low; j <= high- 1; j++) 
    { 
        // If current element is smaller than the pivot 
        if (arr[j] < pivot) 
        { 
            i++;    // increment index of smaller element 
            swap(&arr[i], &arr[j]); 
        } 
    } 
    swap(&arr[i + 1], &arr[high]); 
    return (i + 1); 
} 
  
/* The main function that implements QuickSort 
 arr[] --> Array to be sorted, 
  low  --> Starting index, 
  high  --> Ending index */
void quickSort(int arr[], int low, int high) 
{ 
    if (low < high) 
    { 
        /* pi is partitioning index, arr[p] is now 
           at right place */
        int pi = partition(arr, low, high); 
  
        // Separately sort elements before 
        // partition and after partition 
        quickSort(arr, low, pi - 1); 
        quickSort(arr, pi + 1, high); 
    } 
} 
  
/* Function to print an array */
void printArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        printf("%d ", arr[i]); 
    printf("\n"); 
} 
  
// Driver program to test above functions 
int main() 
{ 
    int arr[] = {10, 7, 8, 9, 1, 5, 97, 6, 92}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    quickSort(arr, 0, n-1); 
    printf("Sorted array: \n"); 
    printArray(arr, n); 
    return 0; 
} 
/*
My Version, for some reason, it produces stack smashing error

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
		partition(arr, l, pivot-1);
		partition(arr, pivot+1, h);
	}
}

int main() {
	int tmp[] = {1, 8, 3, 10, 4, 11, 92};
	quick_sort(tmp, 0, 6);
	for (int i = 0; i < 7; ++i) {
		printf("%d ", tmp[i]);
	}
	return 0;
}
*/
