# N-Dijkstra

## Problem

[1003 Emergency](https://pintia.cn/problem-sets/994805342720868352/problems/994805523835109376)

## Answer

```c++
#include <iostream>
#include <vector>
using namespace std;
const int MAX_N = 500+5;
const int INF = 1000000000;

int N, M, C1, C2;
int t[MAX_N];
int d[MAX_N][MAX_N];
vector<vector<int> > prevPoints;
int spn = 0, mtn = 0;

void dijkstra() {
    vector<bool> visited(N, false);
    visited[C1] = true;
    // init prevPoints
    for (int i = 0; i < N; ++i) {
        if (d[C1][i] < INF) {
            prevPoints.push_back(vector<int>(1,C1));
        } else {
            prevPoints.push_back(vector<int>(1,-1));
        }
    }

    for (int i = 0; i < N; ++i) {
        int closest = INF;
        int toVisit = -1;
        for (int j = 0; j < N; ++j) {
            if (!visited[j] && d[C1][j] < closest) {
                closest = d[C1][j];
                toVisit = j;
            }
        }
        if (toVisit != -1) {
            visited[toVisit] = true;
            for (int k = 0; k < N; k++) {
                if (d[toVisit][k]<INF && !visited[k]) {
                    if (d[C1][k] > d[C1][toVisit]+d[toVisit][k]) {
                        d[C1][k] = d[C1][toVisit] + d[toVisit][k];
                        prevPoints[k].clear();
                        prevPoints[k].push_back(toVisit);
                    } else if (d[C1][k] == d[C1][toVisit]+d[toVisit][k]) {
                        prevPoints[k].push_back(toVisit);
                    }
                }
            }
        } else {
            break;
        }
    }
}

void dfs(int p, int tn) {
    tn += t[p];
    if(p==C1) {
        spn++;
        mtn = tn>mtn ? tn:mtn;
    }
    for (unsigned int i = 0; i < prevPoints[p].size(); ++i) {
        if (prevPoints[p][i]!=-1) {
            dfs(prevPoints[p][i], tn);
        }
    }
}

int main() {
    // init
    for(int i=0; i<MAX_N; i++) {
        for(int j=0; j<MAX_N; j++) {
            d[i][j] = INF;
        }
    }
    // input
    cin >> N >> M >> C1 >> C2;
    for(int i=0; i<N; i++) {
        cin >> t[i];
    }
    for(int i=0; i<M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        d[a][b] = d[b][a] = c;
    }
    // solve
    dijkstra();
    dfs(C2, 0);
    // output
    cout << spn << " " << mtn << endl;
    return 0;
}

```

## References

1. [获取多条最短路径的Dijkstra算法](https://blog.csdn.net/u013615687/article/details/69062803)