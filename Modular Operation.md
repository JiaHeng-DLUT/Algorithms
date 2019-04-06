# Modular Operation

1. $C^m_n\ \%\ 10^9$

```c++
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const long long MOD = 1e9;

// find the multiplicative inverse of a % MOD
int inv(int a){
	return a == 1 ? 1 : (ll)(MOD - MOD / a) * inv(MOD%a) % MOD;
}

ll C(ll m, ll n) {
	if (m < 0) return 0;
	if (n < m) return 0;

	if (m > n - m) m = n - m;

	ll up = 1, down = 1;
	for (ll i = 0; i < m; i++) {
		up = up * (n - i) % MOD;
		down = down * (i + 1) % MOD;
	}
	return up * inv(down) % MOD;
}

int main() {
	cout << C(3, 6) << endl; // 20
}

```

