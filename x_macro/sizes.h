#pragma once

#define PIZZA_SIZES \
    PIZZA_SIZE(PERSONAL) \
    PIZZA_SIZE(SMALL) \
    PIZZA_SIZE(MEDIUM) \
    PIZZA_SIZE(LARGE) \
    PIZZA_SIZE(XTRALARGE) \
    PIZZA_SIZE(JUMBO)

#define PIZZA_SIZE(size) size,
typedef enum {
    PIZZA_SIZES
} pizza_size_t;
#undef PIZZA_SIZE


/*
 The above enum is expanded to the following (line breaks added
 for clarity):

typedef enum {
    PIZZA_SIZE(PERSONAL) 
    PIZZA_SIZE(SMALL)
    PIZZA_SIZE(MEDIUM)
    PIZZA_SIZE(LARGE)
    PIZZA_SIZE(XTRALARGE)
    PIZZA_SIZE(JUMBO)
} pizza_size t;

 ...which, since PIZZA_SIZE has been defined to merely take its 
 included string and append a comma, becomes:

typedef enum {
    PERSONAL,
    SMALL
    MEDIUM,
    LARGE,
    XTRALARGE,
    JUMBO,
} pizza_size t;

 Which just looks like a normal enum, so why the trouble? The
 real value shows itself the next step, where we make an array
 of the string form of the names of enums with only one extra #define!
 See sizes.c for that.
*/

// Because I plan on having a C++ file call the declared function(s),
// I need to protect them from "name-mangling" 
#ifdef __cplusplus
extern "C" {
#endif

void print_all_sizes(void);

#ifdef __cplusplus
}
#endif
