#ifndef MENUS_H
#define MENUS_H
#include <cstdlib>
#include <iostream>
#include "Student.h"
#include "StudentsArray.h"

namespace app{
    namespace menu{
        class UserMenu
        {
            Osoba* zalogowany;
        public:
            void ustawZalogowanego(Osoba* o);
            void Wyloguj();
            virtual void Interfejs();
        };
    }
}
#endif // MENUS_H
