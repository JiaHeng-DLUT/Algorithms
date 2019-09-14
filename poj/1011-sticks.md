# 1011 Sticks

dfs + 剪枝

```cpp
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;


#define MAX_N 64
int n, a[MAX_N], v[MAX_N]/*标记访问*/, l/*每一根的长度*/, last/*上一次访问位置*/;


bool cmp(int p, int q) {
    return p > q;
}


// p: 还剩 p 根木棍
// q: 这跟木棍缺 q
bool dfs(int p, int q) {
    if (q == 0) {
        if (p == 0) {
            return true;
        }
        else {
            q = l;
        }
    }
    int s;
    if (q == l) {
        s = 0;
    }
    else {
        s = last + 1;
    }
    for (int i = s; i < n; i++) {
        if (i > 1 && !v[i - 1] && a[i] == a[i - 1]) {
            continue;
        }
        if (!v[i] && a[i] <= q) {
            v[i] = 1;
            last = i;
            if (dfs(p - 1, q - a[i])) {
                return true;
            }
            else {
                v[i] = 0;
                // q == l -> dfs(p-1, l-a[i]): false -> 找第一根子棍失败 -> 上一次选的错误
                // q == a[i] -> dfs(p-1, 0): false -> 下一根失败 -> 上一次选的错误
                if (q == l || q == a[i]) {
                    return false;
                }
            }
        }
    }
    return false;
}


int main() {
    while (cin >> n && n != 0) {
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            v[i] = 0;
        }
        sort(a, a + n, cmp);
        int sum = accumulate(a, a + n, 0);
        int i;
        for (i = a[0]; i <= sum / 2; i++) {
            if (sum%i == 0) {
                l = i;
                if (dfs(n, l)) {
                    cout << l << endl;
                    break;
                }
            }
        }
        if (i > sum / 2) {
            cout << sum << endl;
        }
    }
    return 0;
}
```

