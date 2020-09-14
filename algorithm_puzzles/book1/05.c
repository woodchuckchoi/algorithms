#include <stdio.h>
#include <stdlib.h>

int cnt = 0;
int coins[4] = {500, 100, 50, 10};

int pop(int* array) {
	int tmpIdx = 0;
	while (tmpIdx < 4) {
		if (array[tmpIdx]) {
			int out = array[tmpIdx];
			array[tmpIdx] = 0;
			return out;
		}
		tmpIdx++;
	}
	return 0;
}

int* copy(int* toCopy) {
	int* copied = malloc((&toCopy)[1] - toCopy);
	int tmpCnt = ((&toCopy)[1] - toCopy) / *toCopy;
	while (tmpCnt--) {
		*copied = *toCopy;
		toCopy++;
		copied++;
	}
	return copied;
}

void change(int target, int* kinds, int left) {
	int coin = pop(kinds);
	printf("Current status: coin %d count %d target %d left %d\n", coin, cnt, target, left);
	if (coin == 0) return;
	if (kinds[3] == 0) {
		if (target / coin <= left) cnt++;
	} else {
		for (int i = 0; i < target / coin + 1; i++) {
			change(target - coin * i, copy(kinds), left - i);
		}
	}
}

int main() {
	change(1000, coins, 15);
	printf("%d\n", cnt);
	return 0;
}
