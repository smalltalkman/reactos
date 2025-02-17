#define STANDALONE
#include <apitest.h>

extern void func_button(void);
extern void func_imagelist(void);
extern void func_propsheet(void);
extern void func_toolbar(void);

const struct test winetest_testlist[] =
{
    { "buttonv6", func_button },
    { "imagelist", func_imagelist },
    { "propsheetv6", func_propsheet },
    { "toolbarv6", func_toolbar },
    { 0, 0 }
};
