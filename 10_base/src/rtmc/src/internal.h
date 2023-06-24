/**
 * @file internal.h
 * @brief rtmc内部ヘッダ
 *
 * @copyright copyright (c) 2023 EkiOka
 *
 */
#ifndef __75FEF39E_INTERNAL_H__

/* ------------------------------------------- */
/*
    include guard
*/
/* ------------------------------------------- */

/*
    コンポーネント外部からのinclude防止用ガード処理
*/

#ifdef COMPONENT_ID
#if COMPONENT_ID == 0x75FEF39E
#else
#error this header will be used inside the component.
#endif
#else
#error undefined COMPONENT_ID.
#endif

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
#ifdef _DEBUG
#define STATIC        /** 通常時は外部参照可能なようにstaticなし */
#else
#define STATIC static /** 通常時はstatic扱い */
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

#endif /*__75FEF39E_INTERNAL_H_*/
