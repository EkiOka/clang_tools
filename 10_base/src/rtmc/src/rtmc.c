/**
 * @file rtmc.c
 * @brief rtmc(real time measurement component) 公開インターフェース定義
 *
 * @copyright copyright (c) 2023 EkiOka
 *
 */
#define COMPONENT_ID 0x75FEF39E
#define MODULE_ID    0xC2025068
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
#include "statistics.h"

/* 自ファイルのinclude */
#include "rtmc.h"

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
    static const variable
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function
*/
/* ------------------------------------------- */

/**
 * @brief rtmc 初期化
 */
static void initialize(void)
{
    statistics.init();
}

/**
 * @brief rtmc 高優先度タスク開始時処理
 */
static void high_task_start(void)
{
}

/**
 * @brief rtmc 中優先度タスク開始時処理
 */
static void mid_task_start(void)
{
    statistics.start(0);
}

/**
 * @brief rtmc 低優先度タスク開始時処理
 */
static void low_task_start(void)
{
}

/**
 * @brief rtmc 高優先度タスク終了時処理
 */
static void high_task_end(void)
{
}

/**
 * @brief rtmc 中優先度タスク終了時処理
 */
static void mid_task_end(void)
{
    statistics.end(0);
    statistics.calc(0);
}

/**
 * @brief rtmc 低優先度タスク終了時処理
 */
static void low_task_end(void)
{
}

/* ------------------------------------------- */
/*
    public function table
*/
/* ------------------------------------------- */

const rtmc_if rtmc = {
    &initialize,      /* event_reset */
    &initialize,      /* event_restart */
    &high_task_start, /* event_high_task_start */
    &mid_task_start,  /* event_mid_task_start */
    &low_task_start,  /* event_low_task_start */
    &high_task_end,   /* event_high_task_end */
    &mid_task_end,    /* event_mid_task_end */
    &low_task_end,    /* event_low_task_end */
};
