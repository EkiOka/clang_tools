/**
 * @file rtmc.c
 * @brief rtmc(real time measurement component) 公開インターフェース定義
 * 
 * @copyright copyright (c) 2023 EkiOka
 * 
 */
#define COMPONENT_ID 0x75FEF39E
#include "rtmc.h"

void rtmc_initialize(void)
{
    
}





const rtmc_if rtmc = {
    &rtmc_initialize, /* event_reset */
    &rtmc_initialize, /* event_restart */
};
