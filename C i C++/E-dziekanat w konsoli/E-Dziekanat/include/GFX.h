#ifndef GFX_H
#define GFX_H
#include <cstdlib>
#include <iostream>

using namespace std;

namespace app{
    class GFX
    {
        public:
           static void mainMenu();
           static void adminMenu();
           static void dodawanieMenu();
           static void usuwanieMenu();
           static void studentMenu();
           static void nauczycielMenu();
    };
}
#endif // GFX_H
