/**
 * @file main.c
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2023-05-01
 * 
 * @copyright Copyright (c) 2023
 * 
 */

/* --- include --- */

#include "sub.h"    /* local = yes */
#include <stdlib.h> /* local = no */
#include <stdlib.h> /* 2つめはdoxygenに現れないらしい */

static const int abcd_res;

int main(void);     /* プロトタイプ宣言はdeclline属性などに現れるが複数か？引数は一致するか？などはチェックできない */
static const int abcd_res[20] = {0}; /**< abcd response */

/**
 * @brief 関数ａｂｃｄの概要説明
 * @details 詳細説明 
 * @note ノート
 * @attention 注意事項
 * @param [in] xyz 説明ｘｙｚ
 * @note ノート2
 * @param [in] yyy 説明ｙｙｙ
 * @note ノート3
 * @param [in,out] zzz 説明ｚｚｚ
 * @note ノート4
 * @return int 戻り値の説明
 */
int abcd( int xyz, const int yyy, char* zzz);

/**
 * @brief aaaa
 * @details
 * kkkk
 * @note None
 * LLLL
 * @warning
 * 警告文
 * @remark
 * 備考
 * 備考2
 * @warning
 * 警告文
 * 警告文2
 */
int main(void)
{
    const int res = 0;
    hello();
    return abcd(1,2,0);
}

/**
 * @brief abcd function brief
 * 
 * @param xxx var name is xxx.
 * @param yyy var name is yyy.
 * @param zzz var name is zzz.
 * @return int return type is int.
 */
int abcd( int xxx, const int yyy, char* zzz)
{
    return abcd_res[0];
}
