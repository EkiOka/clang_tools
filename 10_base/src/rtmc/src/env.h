/**
 * @file env.h
 * @brief 開発環境
 * @copyright Copyright (c) EkiOka 2023
 *
 */
#ifndef __75FEF39E_ENV_H__

/* ------------------------------------------- */
/*
    include
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    define
*/
/* ------------------------------------------- */

/* SUPPORTED_C11 / NOT_SUPPORTED_C11 */

#if defined(__STDC__)
#if defined(__STDC_VERSION__) && (__STDC_VERSION__ >= 201112L) /* C11 */
#define SUPPORTED_C11                                          /** C11 サポート */
#else                                                          /* not C11 */
#define NOT_SUPPORTED_C11                                      /** C11 サポートしていない */
#endif
#else                                                          /* not defined __STDC__ */
#define NOT_SUPPORTED_C11                                      /** C11 サポートしていない */
#endif

/* ------------------------------------------- */
/*
    typedef
*/
/* ------------------------------------------- */

/* ------------------------------------------- */
/*
    function and variable
*/
/* ------------------------------------------- */

#endif /* __75FEF39E_ENV_H__ */
