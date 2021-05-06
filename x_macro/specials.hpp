#pragma once

#define SPECIALS \
    SPECIAL(MARGHARITA, 3) \
    SPECIAL(BBQ_CHICKEN, 5) \
    SPECIAL(WHITE_CLAM, 6) \
    SPECIAL(PESTO_FETA, 9) \
    SPECIAL(STEAK_N_CHEESE, 13) \
    SPECIAL(GARDEN_VEGGIE, 19)

#define SPECIAL(name, ID) name=ID,
enum specials_t {
    SPECIALS
};
#undef SPECIAL

void print_all_specials();