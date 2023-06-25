/**
 * @file statistics_cfg.h
 * @copyright Copyright (c) 2023 EkiOKa
 * @brief 統計値算出コンフィグ
 */
#ifndef __75FEF39E_STATISTICS_CFG_H__

/* ------------------------------------------- */
/*
    include guard
*/
/* ------------------------------------------- */

/*
    モジュール外部からのinclude防止用ガード処理
*/

#ifdef MODULE_ID
#if COMPONENT_ID == 0xC4777AD6
#else
#error this header will be used inside the module.
#endif
#else
#error undefined MODULE_ID.
#endif

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

/**
 * @brief 統計データ数
 */
#define STATISTICS_DATA_COUNT (1U)

/**
 * @brief 間隔データ型
 *
 */
#define INTERVAL_DATA_TYPE RTMC_UINT

/**
 * @brief 間隔データの合計値の型
 *
 */
#define INTERVAL_DATA_SUM_TYPE RTMC_UINT_MAX

/* ------------------------------------------- */
/*
    typedef
*/
/* ------------------------------------------- */

/**
 * @brief 統計値データ型
 */
typedef struct tag_statistics_data {

    RTMC_UINT_MAX start_time;   /** 測定開始時間*/
    RTMC_UINT_MAX end_time;     /** 測定終了時間*/

    INTERVAL_DATA_TYPE     max; /** 最大値 */
    INTERVAL_DATA_TYPE     min; /** 最小値 */
    INTERVAL_DATA_SUM_TYPE sum; /** 合計値 */
    RTMC_UINT_MAX          cnt; /** データ件数 */

    RTMC_UINT_MAX  hst_under;   /**ヒストグラム下限値未満件数*/
    RTMC_UINT_MAX* hst_buf_top; /**ヒストグラム範囲内・バッファ先頭データ*/
    RTMC_CUINT_MAX hst_buf_len; /**ヒストグラム範囲内・バッファサイズ*/
    RTMC_CUINT_MAX hst_max;     /**ヒストグラム範囲最大値 */
    RTMC_CUINT_MAX hst_min;     /**ヒストグラム範囲最小値 */
    RTMC_CUINT_MAX hst_coef;    /**ヒストグラム係数 */
    RTMC_UINT_MAX  hst_over;    /**ヒストグラム上限値超え件数*/
} statistics_data;

/**
 * @struct statistics_var
 * @brief statisticsモジュール変数
 */
typedef struct tag_statistics_var {
    RTMC_CUINT      data_cnt;                    /** 統計データ数 */
    statistics_data data[STATISTICS_DATA_COUNT]; /** 統計データ */
} statistics_var;

/* ------------------------------------------- */
/*
    function and variable
*/
/* ------------------------------------------- */

extern statistics_var self; /**モジュール内変数*/

#endif                      /* __75FEF39E_STATISTICS_CFG_H__ */
