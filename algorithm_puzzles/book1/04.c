#include <stdio.h>

int cut(int n, int m, int cur) {
	if (cur >= n) return 0;
	
	if (cur <= m) return 1+cut(n, m, cur*2);
	else return 1+cut(n, m, cur+m);
}

int main() {
	printf("%d\n", cut(20, 3, 1));
	printf("%d\n", cut(100, 5, 1));
	return 0;
}
