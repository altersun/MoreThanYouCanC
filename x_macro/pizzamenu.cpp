#include <iostream>
#include "sizes.h"
#include "toppings.hpp"
#include "specials.hpp"

using namespace std;

int main()
{
    cout << endl << "!WELCOME TO PIZZATOWN USA!" << endl << endl;
    print_all_sizes();
    cout << endl;
    print_all_toppings();
    cout << endl;
    print_all_specials();
    return 0;
}