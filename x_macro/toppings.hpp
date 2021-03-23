#pragma once

#define TOPPINGS \
    TOPPING(PEPPERONI) \
    TOPPING(SAUSAGE) \
    TOPPING(MEATBALLS) \
    TOPPING(GRILLED_CHICKEN) \
    TOPPING(MUSHROOMS) \
    TOPPING(PEPPERS) \
    TOPPING(ONIONS) \
    TOPPING(FRESH_RICCOTA)

#define TOPPING(topping) topping,
enum toppings_t {
    TOPPINGS
};

/* 
 The x Macro works just as well in C++. The only difference 
 is the enum syntax.
*/


void print_all_toppings();
