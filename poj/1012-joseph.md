# 1012 Joseph

```cpp
#include <iostream>
using namespace std;


int main()
{
    int Joseph[14] = { 0 };  // k

    int k;
    while (cin >> k && k != 0)
    {
        if (Joseph[k])
        {
            cout << Joseph[k] << endl;
            continue;
        }

        int n = 2 * k; // 总人数
        int ans[30] = { 0 };

        int m = k + 1;
        for (int i = 1; i <= k; i++)  // 轮数
        {
            ans[i] = (ans[i - 1] + m - 1) % (n - i + 1);   // n-i为剩余的人数
            if (ans[i] < k)  // 把好人杀掉了
            {
                i = 0;
                m++;
            }
        }
        Joseph[k] = m;
        cout << m << endl;
    }
    return 0;
}
```

## Ref

* [POJ1012-Joseph](https://blog.csdn.net/lyy289065406/article/details/6648444)
* [POJ1012 – Joseph](http://exp-blog.com/2018/06/23/pid-945/)

