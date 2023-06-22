/**
 * @file adp_reg.c
 * @brief rtmc レジスタアクセス中継用処理
 * 
 * @copyright copyright (c) 2023 EkiOka
 * 
 */
#define COMPONENT_ID 0x75FEF39E


/* ------------------------------------------- */
/*
    include
*/
/* ------------------------------------------- */
#if defined (__STDC__)
#if defined(__STDC_VERSION__) && (__STDC_VERSION__ >= 201112L)  /* C11 */
#include <assert.h>
#else
#define static_assert(condition, msg)
#endif
#else
#define static_assert(condition, msg)
#endif
#include "adp_reg.h"

/* ------------------------------------------- */
/*
    define
*/
/* ------------------------------------------- */

#define STUB_GET_COUNT()    1   /**< 起動開始からのカウンター取得用APIを割り当ててください。(初期設定はダミーです。) */
#define STUB_GET_COUNT_RES_TYPE RTMC_CUINT32
static_assert(sizeof(STUB_GET_COUNT_RES_TYPE) == sizeof(RTMC_CUINT32), "un match size.");

/* ------------------------------------------- */
/*
    typedef
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function prototype
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    variable
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function table
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    static const variable
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function
*/
/* ------------------------------------------- */


RTMC_RT_COUNT_TYPE get_time(void)
{
    return ( STUB_GET_COUNT() );
}



/* ------------------------------------------- */
/*
    end of file
*/
/* ------------------------------------------- */
