# Lexicographical order

* Problem: [CSL 的字符串](https://ac.nowcoder.com/acm/contest/551/D)

```cpp
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;
const int MAX_N = 1e5 + 10;


char s[MAX_N], ans[MAX_N];
int cnt[MAX_N], vis[MAX_N];


int main() {
    // input
    cin >> s;
    // init
    memset(cnt, 0, sizeof(cnt));
    memset(ans, 0, sizeof(ans));
    int len=strlen(s), t=0;
    // solve
    for(int i=0; i<len; i++) {
        cnt[s[i]]++;
    }
    for(int i=0; i<len; i++) {
        cnt[s[i]]--;
        if(!vis[s[i]]) {
            while(t&&ans[t]>s[i]&&cnt[ans[t]]>0) {
                vis[ans[t]] = 0;
                t--;
            }
            t++;
            ans[t] = s[i];
            vis[s[i]] = 1;
        }
    }
    // output
    for(int i=1; i<=t; i++) {
        printf("%c",ans[i]);
    }
    printf("\n");
}
```

