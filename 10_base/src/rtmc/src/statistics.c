
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
#include <limits.h>

/* OS / 基盤ソフトのinclude */

/* システム共通ライブラリのinclude */

/* 他コンポーネントのinclude */

/* 自コンポーネントのinclude */
#include "adp_reg.h"

/* 自ファイルのinclude */
#include "statistics.h"
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
    const variable
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function
*/
/* ------------------------------------------- */

/**
 * @brief Construct a new statistics initialize object
 */
static statistics_initialize(void)
{
    RTMC_UINT        i;
    statistics_data* p_data;
    for (i = 0; i < self.data_cnt; i++) {
        p_data = &self.data[i];

        p_data->max = 0;
        p_data->min = ULONG_MAX;
        p_data->cnt = 0;
        p_data->sum = 0;
    }
    return;
}

/**
 * @brief レジスタのカウント値を測定開始時間として設定する
 * @param no 測定番号
 */
static void start(RTMC_CUINT no)
{
    if (no < self.data_cnt) {
        self.data[no].start_time = adp_reg.get_time();
    } else {
        /* do nothing */
    }
}

/**
 * @brief レジスタのカウント値を測定終了時間として設定する
 * @param no 測定番号
 */
static void end(RTMC_CUINT no)
{
    if (no < self.data_cnt) {
        self.data[no].end_time = adp_reg.get_time();
    } else {
        /* do nothing */
    }
}

/**
 * @brief 統計値の演算を行います。
 * @param no 測定番号
 */
static void calc(RTMC_CUINT no)
{
    statistics_data* p_data;
    RTMC_UINT_MAX    value;

    if (no < self.data_cnt) {
        /* 経過時間算出 */
        p_data = &self.data[no];
        value  = p_data->end_time - p_data->start_time;

        /*
            合計・件数追加
            平均値の計算はデータダンプ後などでも可能なため行わない。
        */
        p_data->sum += value;
        p_data->cnt++;

        /* 最大値・最小値 */
        if (value > p_data->max) {
            p_data->max = value;
        }
        if (value < p_data->min) {
            p_data->min = value;
        }

        /* ヒストグラム算出 */
        if (value < p_data->hst_min) {
            p_data->hst_under++;
        } else if (value > p_data->hst_max) {
            p_data->hst_over++;
        } else {
            p_data->hst_buf_top[(value - p_data->hst_min) / p_data->hst_coef]++;
        }

    } else {
        /* do nothing */
    }
}

/* ------------------------------------------- */
/*
    function table
*/
/* ------------------------------------------- */
statistics_if statistics = {
    &statistics_initialize, /* init */
    &start,                 /* start */
    &end,                   /* end */
    &calc,                  /* calc */
};
