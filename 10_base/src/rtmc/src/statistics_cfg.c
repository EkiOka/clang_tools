/**
 * @file statistics_cfg.c
 * @copyright Copyright (c) 2023 EkiOka
 * @brief 統計情報コンフィグ設定
 */

/* ------------------------------------------- */
/*
    component infomation
*/
/* ------------------------------------------- */
#define COMPONENT_ID 0x75FEF39E
#define MODULE_ID    0xC4777AD6
#include "internal.h"

/* ------------------------------------------- */
/*
    include
*/
/* ------------------------------------------- */
/* C言語 標準型のinclude */

/* 開発基盤 標準型のinclude */

/* C言語標準ライブラリのinclude */

/* OS / 基盤ソフトのinclude */

/* システム共通ライブラリのinclude */

/* 他コンポーネントのinclude */

/* 自コンポーネントのinclude */

/* 自ファイルのinclude */
#include "statistics_cfg.h"

/* ------------------------------------------- */
/*
    define
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    typedef
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    variable
*/
/* ------------------------------------------- */

static RTMC_UINT_MAX hist1[5];

/**
 * @brief モジュール内変数
 *
 */
statistics_var self = {
    STATISTICS_DATA_COUNT,
    {
        0,                                                     /* start_time */
        0,                                                     /* end_time */
        0,                                                     /* max */
        ~0,                                                    /* min */
        0,                                                     /* sum */
        0,                                                     /* cnt */
        0,                                                     /* hst_under */
        &hist1[0],                                             /* hst_buf_top */
        sizeof(hist1) / sizeof(RTMC_UINT_MAX),                 /* hst_buf_len */
        1024,                                                  /* hst_max */
        24,                                                    /* hst_min */
        (1024 - 24) / (sizeof(hist1) / sizeof(RTMC_UINT_MAX)), /* hst_coef */
        0,                                                     /* hst_over */
    },
};
/* ------------------------------------------- */
/*
    const variable
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function prototype
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function table
*/
/* ------------------------------------------- */