#include <stdio.h>
#include <stdlib.h>

void hello();
int main(void);

/**
 * @brief aaaa
 * 
 * @return int bbbb 
 */
int main(void)
{
    hello();
    return 0;
}
void hello(void)
{
    printf("hello world?");
}
int abcd( int xxx, const int yyy, char* zzz)
{
    return xxx;
}