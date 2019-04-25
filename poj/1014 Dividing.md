# 1014 Dividing

```c++
#include <string.h>
#include <iostream>
#include <algorithm>
#include <numeric>
#define MAX_N 20001

int    num[MAX_N];
int    arr[MAX_N/200];
int    flag[MAX_N/200][MAX_N]; /* flag[i][j]=0 means dfs(i, j) return false; */
int    c1 = 0; /* num of input samples */
int    c2 = 0; /* num of total numbers */

bool dfs(int sp, int l) {
    if (l == 0) {
        return true;
    } else {
        for (; sp < c2; sp++) {
            if (arr[sp] <= l) {
                if (flag[sp + 1][l - arr[sp]] && dfs(sp + 1, l - arr[sp])) { /* trim 2 */
                    return true;
                } else {
                    flag[sp + 1][l - arr[sp]] = 0;
                    if (arr[sp + 1] == arr[sp + 2]) { /* trim 1 */
                        sp += 2;
                    }
                }
            }
        }
        return false;
    }
}


int main(int argc, const char * argv[]) {
    while (1) {
        /* init variables */
        memset(num, 0, sizeof(num));
        memset(arr, 0, sizeof(arr));
        memset(flag, 1, sizeof(flag));
        c1++;
        c2 = 0;
        /* input */
        for (int i = 1; i <= 6; i++) {
            std::cin >> num[i];
        }
        if(!num[1] && !num[2] && !num[3] && !num[4] && !num[5] && !num[6]) {
            break;
        }
        /* convert */
        for (int i = 1; i < MAX_N; i++) {
            if (num[i] > 2) {
                if (num[i] % 2 == 1) {
                    num[2 * i] += (num[i] - 1) / 2;
                    num[i] = 1;
                } else {
                    num[2 * i] += (num[i] - 2) / 2;
                    num[i] = 2;
                }
            }
        }
        int sum = 0;
        for (int i = MAX_N-1; i > 0; i--) {
            sum += num[i]*i;
            for (int j = 0; j < num[i]; j++) {
                arr[c2++] = i;
            }
        }
        /* solve */
        std::cout << "Collection #" << c1 << ":" << std::endl;
        if (sum % 2 == 1) {
            std::cout << "Can't be divided." << std::endl << std::endl;
        } else {
            if (dfs(0, sum / 2)) {
                std::cout << "Can be divided." << std::endl << std::endl;
            } else {
                std::cout << "Can't be divided." << std::endl << std::endl;
            }
        }
    }
    return 0;
}

```

