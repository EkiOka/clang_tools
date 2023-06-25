/**
 * @file adp_reg.h
 * @brief rtmc レジスタアクセス中継用IFヘッダ
 * @details
 * rtmc内で使用されるレジスタへのアクセスの中継を行う関数を宣言します。
 * @attention
 * アクセスする際に型定義が必要な場合は本ファイルの.cにて内部の型に変換を行ってからコンポーネント内部に渡してください。
 * @attention
 * パフォーマンスの低下が問題となるときのみ、マクロ関数、またはインライン関数を定義してください。
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

/*
    コンポーネント内部で使用する型名

*/

#define RTMC_RT_COUNT_TYPE RTMC_CUINT_MAX

/* ------------------------------------------- */
/*
    typedef
*/
/* ------------------------------------------- */

/**
 * @struct adp_reg_if
 * @brief adp_regの外部公開インターフェース型
 */
typedef struct tag_adp_reg_if {
    /**
     * @brief 起動からの経過時間取得
     *
     * @return RTMC_RT_COUNT_TYPE
     * 起動からの経過時間(単位は参照レジスタに依存。マニュアルを参照してください。)
     */
    RTMC_RT_COUNT_TYPE(*get_time)
    (void);
} adp_reg_if;

/* ------------------------------------------- */
/*
    function and variable
*/
/* ------------------------------------------- */

/* variables */

/* functions */

/**
 * @brief adp_regの外部公開インターフェース
 */
const adp_reg_if adp_reg;

#endif /*__ADP_REG_H__*/
