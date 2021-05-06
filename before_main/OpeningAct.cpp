#include <iostream>
#include <string>


class OpeningAct {
    public:
        OpeningAct(void(*fp)(void)) {
            if (fp) {
                (*fp)();
            }
        };
};


//#define RUN_BEFORE_MAIN /


#define REQUIRE_GLOBAL_SCOPE \
#ifdef __func__ \
#error "Called outside global scope" \
#endif

const std::string funcy(__func__);

//REQUIRE_GLOBAL_SCOPE;

int main() 
{
    //REQUIRE_GLOBAL_SCOPE;
    std::cout << "whatup " << funcy <<  std::endl;
    return 0;
}