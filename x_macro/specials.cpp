#include <iostream>
#include <map>
#include <string>
#include "specials.hpp"

namespace {
#define SPECIAL(name, ID) {ID,#name},
    const std::map<int, std::string> specials {
        SPECIALS
    };
#undef SPECIAL
}


void print_all_specials()
{
    std::cout << "Specials:" << std::endl;
    for (const auto& [ID, name] : specials) {
        //std::cout << specials[ID] << std::endl;
        // std::cout << kv.first << " " << kv.second << std::endl;
        std::cout << ID << " " << name << std::endl;
    }
}