/**
 * @file statistics.h
 * @copyright Copyright (c) 2023
 * @brief 統計値算出
 *
 */
#ifndef __75FEF39E_STATISTICS_H__

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

/* ------------------------------------------- */
/*
    typedef
*/
/* ------------------------------------------- */

typedef struct tag_statistics_if {
    void (*init)(void);
    void (*start)(RTMC_CUINT no);
    void (*end)(RTMC_CUINT no);
    void (*calc)(RTMC_CUINT no);
} statistics_if;

/* ------------------------------------------- */
/*
    function and variable
*/
/* ------------------------------------------- */

extern statistics_if statistics;

#endif /* __75FEF39E_STATISTICS_H__ */
