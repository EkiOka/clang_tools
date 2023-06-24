/**
 * @file rtmc.h
 * @brief rtmc(real time measurement component) 公開ヘッダ
 * @details 標準型の定義も行うため内部からもincludeされます。
 *
 * @copyright copyright (c) 2023 EkiOka
 *
 */
#ifndef __75FEF39E_RTMC_H__

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

/* standard types */
#define RTMC_UINT8   unsigned char
#define RTMC_UINT16  unsigned short
#define RTMC_UINT32  unsigned long
#define RTMC_UINT64  unsigned long long
#define RTMC_SINT8   signed char
#define RTMC_SINT16  signed short
#define RTMC_SINT32  signed long
#define RTMC_SINT64  signed long long
#define RTMC_BOOL    __Bool
#define RTMC_CUINT8  const unsigned char
#define RTMC_CUINT16 const unsigned short
#define RTMC_CUINT32 const unsigned long
#define RTMC_CUINT64 const unsigned long long
#define RTMC_CSINT8  const signed char
#define RTMC_CSINT16 const signed short
#define RTMC_CSINT32 const signed long
#define RTMC_CSINT64 const signed long long
#define RTMC_CBOOL   const __Bool

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
typedef struct __tag_rtmc_if__ {
    /**
     * @brief rtmcへ電源ONのリセットイベントを通知
     */
    void (*event_reset)(void);
    /**
     * @brief rtmcへ省電力モードからの復帰イベントを通知
     */
    void (*event_restart)(void);
} rtmc_if;

/* ------------------------------------------- */
/*
    public function and variable
*/
/* ------------------------------------------- */
extern const rtmc_if rtmc;

#endif /* __75FEF39E_RTMC_H__ */
