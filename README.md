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

-----

# ACM

[TOC]

## 位运算



Given an array of intergers, every element appears `k` (`k > 1`) times except for one, which appears `p` times (`p >= 1, p % k != 0`)Find that single one.

- 要求：**线性时间复杂度，不适用额外空间**

Example

|      Input      | Output |
| :-------------: | :----: |
|    [2, 2, 1]    |   1    |
| [4, 1, 2, 1, 2] |   4    |

References

1. [Detailed explanation and generalization of the bitwise operation method for single numbers](https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers)
2. 

------



vector matrix

```c++
#include <iostream>
#include <vector>
#define row	3
#define col	4
using namespace std;

int main()
{
	/* 二维数组的 vector 定义 */
	vector<vector<int> > v( row );

	/*
	 * init a matrix of (3,4)
	 * i*row+j+1
	 */
	for ( int i = 0; i < v.size(); i++ )
	{
		for ( int j = 0; j < col; j++ )
		{
			v[i].push_back( i * row + j + 1 );
		}
	}

	/*
	 * add one row
	 * 5
	 */
	vector<int> temp;
	v.push_back( temp );
	int pos = v.size() - 1;
	v[pos].push_back( 5 );
	v[pos].push_back( 5 );
	v[pos].push_back( 5 );
	v[pos].push_back( 5 );

	/*
	 * add one col
	 * 6
	 */
	pos = v.size();
	for ( int i = 0; i < pos; i++ )
	{
		v[i].push_back( 6 );
	}

	/* 打印“二维数组” */
	for ( int i = 0; i < v.size(); i++ )
	{
		for ( int j = 0; j < v[0].size(); j++ )
		{
			cout << v[i][j] << "  ";
		}
		cout << endl;
	}
}


/*
 * ---------------------
 * 作者：Tattoo_Welkin
 * 来源：CSDN
 * 原文：https://blog.csdn.net/liushengxi_root/article/details/78945677
 * 版权声明：本文为博主原创文章，转载请附上博文链接！
 */
```

string

```c++
#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

vector<string> split(const string& str, const string& delim) {  
	vector<string> res;  
	if("" == str) return res;  
	//先将要切割的字符串从string类型转换为char*类型  
	char * strs = new char[str.length() + 1] ; //不要忘了  
	strcpy(strs, str.c_str());   
 
	char * d = new char[delim.length() + 1];  
	strcpy(d, delim.c_str());  
 
	char *p = strtok(strs, d);  
	while(p) {  
		string s = p; //分割得到的字符串转换为string类型  
		res.push_back(s); //存入结果数组  
		p = strtok(NULL, d);  
	}  
 
	return res;  
} 

int main(){
    string s = "abc def g";
    vector<string> v;
    v = split(s, " ");
    for (int i=0;i<v.size();i++){
        cout<<v[i]<<endl;
    }
}
```





