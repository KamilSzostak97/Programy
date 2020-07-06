#ifndef APPLICATION_H
#define APPLICATION_H

#include <cstdlib>
#include <stdlib.h>
#include <string>
#include <iostream>
#include "Student.h"
#include "GFX.h"
#include "MenuA.h"
#include "MenuS.h"
#include "StudentsArray.h"


using namespace std;

namespace app{
    class Application
    {
        public:
            Application();
            //void run();
            void operator()();
        protected:
        private:
            Osoba* stworzOsobe(char typ);
            Osoba* interfejsStworzOsobe();
            void AddMultiple(int n);
            void AdminMenu();
            void AddMenu();
            void DeleteMenu();
            void MainMenu();
            Osoba* Login(string login, string pass);

            menu::UserMenu menu;

            TablicaOsob osoby;
            //TablicaOsob Elektronika;

            char S1,S2;
            int N1, N2;

    };
}

#endif // APPLICATION_H
