# Dijkstra

![有向无环图Example](https://i.loli.net/2019/06/08/5cfbabcfd06f958151.png)

|          |  {V0}   | {V0,V2} | {V0,V2,V1} | {V0,V2,V1,V4} | {V0,V2,V1,V4,V3}  |
| :------: | :-----: | :-----: | :--------: | :-----------: | :---------------: |
|    V1    |   12    | **12**  |            |               |                   |
|    V2    | **10**  |         |            |               |                   |
|    V3    |    ∞    |   60    |     60     |    **50**     |                   |
|    V4    |   30    |   30    |   **30**   |               |                   |
|    V5    |   100   |   100   |    100     |      90       |      **60**       |
|  新顶点  |   V2    |   V1    |     V4     |      V3       |        V5         |
| 最短路径 | V0-->V2 | V0-->V1 |  V0-->V4   | V0-->V4-->V3  | V0-->V4-->V3-->V5 |
| 路径长度 |   10    |   12    |     30     |      50       |        60         |

```c++
#include <iostream>
using namespace std;

const int n = 6;
const int INF = 10000;

int g[n][n] = {
{INF, 12, 10, INF, 30, 100},
{INF, INF, 5, INF, INF, INF},
{INF, INF, INF, 50, INF, INF},
{INF, INF, INF, INF, INF, 10},
{INF, INF, INF, 20, INF, 60},
{INF, INF, INF, INF, INF, INF}
};
/*
 * d: distance
 * v: visited
 */
int d[n], v[n], index; 

bool end() {
	for (int i = 0; i < n; i++) {
		if (v[i] == 0) {
			return false;
		}
	}
	return true;
}

int findMin() {
	int Min = INF, index = -1;
	for (int i = 0; i < n; i++) {
		if (d[i] < Min && v[i] == 0) {
			Min = d[i];
			index = i;
		}
	}
	return index;
}

void update() {
	for (int i = 0; i < n; i++) {
		if (v[i] == 0 && d[index] + g[index][i] < d[i]) {
			d[i] = d[index] + g[index][i];
		}
	}
}

int main() {
	for (int i = 0; i < n; i++) {
		d[i] = g[0][i];
		v[i] = 0;
	}
	v[0] = 1;
	while (!end()) {
		index = findMin();
		v[index] = 1;
		update();
	}
	for (int i = 1; i < n; i++) {
		cout << d[i] << " ";
	}
	cout << endl;
}

/*
 * 12 10 50 30 60 
 */

```
