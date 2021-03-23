#include <stdio.h>
#include "sizes.h"


#define PIZZA_SIZE(size) #size, // Stringifier macro! See below for more info
static const char* pizza_sizes[] = {
    PIZZA_SIZES
};
#undef PIZZA_SIZE

/*
 Here's where the X Macro starts to shine. First, let's unroll the above:

static const char* pizza_sizes[] = {
    PIZZA_SIZE(PERSONAL) 
    PIZZA_SIZE(SMALL)
    PIZZA_SIZE(MEDIUM)
    PIZZA_SIZE(LARGE)
    PIZZA_SIZE(XTRALARGE)
    PIZZA_SIZE(JUMBO)
};

 PIZZA_SIZE still appends a comma, but now it also uses the stringifier macro!
 The single pound sign (or hashtag symbol) # is a built-in macro in most compilers 
 (certainly gcc). From the gcc manual:

 "When a macro parameter is used with a leading ‘#’, the preprocessor replaces it 
 with the literal text of the actual argument, converted to a string constant."

 Search the gcc manual for "Stringification" for more info. What it does for us here 
 is preprocess our array to the following:

static const char* pizza_sizes[] = {
    "PERSONAL", 
    "SMALL",
    "MEDIUM",
    "LARGE",
    "XTRALARGE",
    "JUMBO",
}

 ...leaving us an array of string forms of our enums from sizes.h. Further, the array lookup
 links the enum values to their string forms! For example:

printf("%s\n", pizza_sizes[PERSONAL]);  // prints "PERSONAL"
printf("%s\n", pizza_sizes[XTRALARGE]); // prints "XTRALARGE"

See print_all_sizes() below for the full example.
*/

void print_all_sizes() 
{
    printf("Sizes:\n");
    for (pizza_size_t size=PERSONAL; size<=JUMBO; ++size) {
        printf("%s\n", pizza_sizes[size]);
    }
}