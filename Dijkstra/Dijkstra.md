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
#include <vector>
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
// d: distance
vector<int> d;

void dijkstra(int start) {
	for (int i = 0; i < n; i++) {
		d.push_back(g[start][i]);
	}
	vector<bool> v(n, false); // v: visited
	v[start] = 1;


	for (int i = 0; i < n; i++) {
		int closest = INF, toVisit = -1;
		for (int j = 0; j < n; j++) {
			if (d[j] < closest && v[j] == 0) {
				closest = d[j];
				toVisit = j;
			}
		}
		if (toVisit != -1) {
			cout << "New Vertex: V" << toVisit << endl;
			v[toVisit] = true;
			for (int j = 0; j < n; j++) {
				if (v[j] == 0 && d[toVisit] + g[toVisit][j] < d[j]) {
					cout << "V0 --> V" << toVisit << " --> V" << j << " : " << d[toVisit] + g[toVisit][j] << endl;
					d[j] = d[toVisit] + g[toVisit][j];
				}
			}
		}
	}
}

int main() {
	// solve
	dijkstra(0);
	// output
	cout << "Path length: ";
	for (int i = 1; i < n; i++) {
		cout << d[i] << " ";
	}
	cout << endl;
}

/*
 * 12 10 50 30 60
 */

```

## References

1. [数据结构、算法及应用](https://book.douban.com/subject/19960783/)

