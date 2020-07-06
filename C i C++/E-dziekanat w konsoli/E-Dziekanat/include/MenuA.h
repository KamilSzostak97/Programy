#ifndef MENUA_H
#define MENUA_H
#include <cstdlib>
#include <iostream>
#include "Student.h"

using namespace std;

namespace app{
    namespace menu{
        class MenuA
        {
            public:
        void dane(string dane, int &N);
        void dane2(string dane, char &N);
        void create(Student* &s, int N);
        void usun(Student* &s);
        void add(Student* s, int N,char S);
        void wypis(Student* s,int N);
        void AddNext(Student* &s, int &N, int id, char Klasa);
        void usunWyb(Student* &s, int &N, int k);
        void create(Student** &s, int N);
        void usun(Student** &s, int N);
        void add(Student** s, int N,char S);
        void wypis(Student** s,int N);
        void AddNext(Student** &s, int &N, int id, char Klasa);
        void usunWyb(Student** &s, int &N, int k);
        };
    }
}
#endif // MENUA_H
