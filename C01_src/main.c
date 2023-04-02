#include <stdio.h>
#include <stdlib.h>

void hello();
int main(void);
const int abcd_res = 1;
static char array[5]={1,2,3,4,5};

/**
 * @brief aaaa
 * 
 * @return int bbbb 
 */
int main(void)
{
    const int res = 0;
    hello();
    return res;
}
void hello(void)
{
    printf("hello world?");
}
int abcd( int xxx, const int yyy, char* zzz)
{
    return abcd_res;
}
