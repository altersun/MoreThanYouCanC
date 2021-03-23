#include <iostream>
#include <vector>
#include <string>
#include "toppings.hpp"

namespace { // Anonymous namespace! Everything it wraps is functionally 'static'
#define TOPPING(topping) #topping,
    const std::vector<std::string> toppings {
        TOPPINGS
    };
#undef TOPPING
}

/* 
 The X Macro still works much the same in C++ as it did in C. The only real difference 
 is how we make use of other language features. We COULD still make an array of char*, 
 but with C++ why not a std::vector of std::string? Instead of static, why not an 
 anonymous namespace?

 Because a vector supports the random access operator [], it can be used like an array 
 and still keeps the X macro property where the value of an enum looks up its string form.
*/

void print_all_toppings()
{
    std::cout << "Toppings:" << std::endl;
    for (auto topping=0; topping<toppings.size(); ++topping) {
        std::cout << toppings[topping] << std::endl;
    }
}
