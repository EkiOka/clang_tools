/**
 * @file rtmc.h
 * @copyright copyright (c) 2023 EkiOka
 * @brief rtmc(real time measurement component) 公開ヘッダ
 * @details
 * 標準型の定義も行うため内部からもincludeされます。
 */
#ifndef __75FEF39E_RTMC_H__

/* ------------------------------------------- */
/*
    include
*/
/* ------------------------------------------- */
#include <stdbool.h>
#include <stdint.h>

/* ------------------------------------------- */
/*
    define
*/
/* ------------------------------------------- */

/* standard types */
#define RTMC_UINT      uint_fast16_t
#define RTMC_UINT_MAX  uintmax_t
#define RTMC_CUINT     const uint_fast16_t
#define RTMC_CUINT_MAX const uintmax_t

/* ------------------------------------------- */
/*
    struct
*/
/* ------------------------------------------- */

/**
 * @struct rtm_if
 * @brief rtmの外部公開インターフェース
 *
 */
typedef struct tag_rtmc_if {
    /**
     * @brief rtmcへ電源ONのリセットを通知
     */
    void (*event_reset)(void);
    /**
     * @brief rtmcへ省電力モードからの復帰を通知
     */
    void (*event_restart)(void);
    /**
     * @brief rtmcへ高優先度タスクの開始を通知
     */
    void (*event_high_task_start)(void);
    /**
     * @brief rtmcへ中優先度タスクの開始を通知
     */
    void (*event_mid_task_start)(void);
    /**
     * @brief rtmcへ低優先度タスクの開始を通知
     */
    void (*event_low_task_start)(void);
    /**
     * @brief rtmcへ高優先度タスクの終了を通知
     */
    void (*event_high_task_end)(void);
    /**
     * @brief rtmcへ中優先度タスクの終了を通知
     */
    void (*event_mid_task_end)(void);
    /**
     * @brief rtmcへ低優先度タスクの終了を通知
     */
    void (*event_low_task_end)(void);
} rtmc_if;

/* ------------------------------------------- */
/*
    public function and variable
*/
/* ------------------------------------------- */
extern const rtmc_if rtmc;

#endif /* __75FEF39E_RTMC_H__ */
