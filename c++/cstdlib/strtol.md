# strtol

```cpp
#include <stdlib.h>     /* strtol */

int main () {
    char szNumbers[] = "101 23";
    char* pEnd;
    long int li1, li2;
    li1 = strtol(szNumbers, &pEnd, 2); // li1 = 1*4+0*2+1*1 = 5
    li2 = strtol(pEnd, NULL, 10); // li = 23
    return 0;
}
```

