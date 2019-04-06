# Algorithms

[TOC]

```c++
int n1 = pow(10, 2); // 99
int n2 = pow(10.0, 2); // 100
char c = (char)33; // c = '!';
char c = (char)48; // c = '0';
char c = (char)65; // c = 'A';
char c = (char)97; // c = 'a';

```

## Output an integer

| Integer | Output  |
| :-----: | :-----: |
|    0    |    0    |
|   035   |  3, 5   |
|   305   | 3, 0, 5 |

## Stack

- pop series: $\frac{C^{n}_{2n}}{n+1}$

## Find Rules

- [CSL 的神奇序列](https://ac.nowcoder.com/acm/contest/551/F)

```c++
#include <iostream>
using namespace std;
typedef long long ll;
const int MAX_N = 1e6 + 5;
const int MOD = 998244353;

int a[MAX_N];

void pre() {
	a[1] = 1;
	for (int i = 2; i < MAX_N; i++) {
		a[i] = (ll)a[i - 1] * (2 * i - 1) % MOD;
	}
}

int main() {
	pre();
	int w, q, n, ans;
	cin >> w >> q;
	for (int i = 1; i <= q; i++) {
		cin >> n;
		ans = (ll)a[n] * w % MOD;
		cout << ans << endl;
	}
	return 0;
}

```

## Minimum Value of $a^Tb$

- [CSL 的魔法](https://ac.nowcoder.com/acm/contest/551/E)

```c++
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef pair<int, int> pii;
#define ff first
#define ss second

int main() {
	int n;
	cin >> n;
	vector<pii> ab(n);
	vector<int> next(n);
	vector<bool> vis(n, false);
	// input
	for (int i = 0; i < n; ++i) cin >> ab[i].ff;
	for (int i = 0; i < n; ++i) cin >> ab[i].ss;
	// solve
	sort(ab.begin(), ab.end()); // sort by ab.ff
	for (int i = 0; i < n; ++i) {
		ab[i].ff = i;
	}
	sort(ab.begin(), ab.end(), [](const pii& x, const pii& y) { return x.ss > y.ss; });
	for (int i = 0; i < n; ++i) {
		next[i] = ab[i].ff;
	}
	int res = 0;
	for (int i = 0; i < n; ++i) {
		if (!vis[i]) {
			++res;
			while (!vis[i]) {
				vis[i] = true;
				i = next[i];
			}
		}
	}
	// output
	cout << n - res << endl;
}
```

## 
