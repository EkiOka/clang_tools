/**
 * @file adp_reg.h
 * @brief rtmc レジスタアクセス中継用IFヘッダ
 * @details rtmc内で使用されるレジスタへのアクセスの中継を行う関数を宣言します。
 * @attention アクセスする際に型定義が必要な場合は本ファイルの.cにて内部の型に変換を行ってからコンポーネント内部に渡してください。
 * @attention パフォーマンスの低下が問題となるときのみ、マクロ関数、またはインライン関数を定義してください。
 * @copyright copyright (c) 2023 EkiOka
 * 
 */
#ifndef __ADP_REG_H__

/* ------------------------------------------- */
/*
    include
*/
/* ------------------------------------------- */

/* standard types */
#include "rtmc.h"

/* check component internal */
#include "internal.h"

/* ------------------------------------------- */
/*
    define
*/
/* ------------------------------------------- */
#define RTMC_RT_COUNT_TYPE RTMC_CUINT32

/* ------------------------------------------- */
/*
    struct
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function and variable
*/
/* ------------------------------------------- */

/* variables */

/* functions */
RTMC_RT_COUNT_TYPE get_time(void);

#endif /*__ADP_REG_H__*/
