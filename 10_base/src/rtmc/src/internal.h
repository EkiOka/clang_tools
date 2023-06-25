/**
 * @file internal.h
 * @brief rtmc内部ヘッダ
 * @details
 * コンポーネント内部のヘッダのすべてからincludeされるヘッダです。
 * include前にCOMPONENT_IDとしてrtmcのIDをincludeしていない場合はエラーとなります。
 * @copyright copyright (c) 2023 EkiOka
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
