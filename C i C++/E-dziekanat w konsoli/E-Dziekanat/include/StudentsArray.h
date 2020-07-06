#ifndef OsobaSARRAY_H
#define OsobaSARRAY_H

#include "Osoba.h"

namespace app{
class TablicaOsob
{
    Osoba** osoby;
    int size;

    public:
        TablicaOsob();
        ~TablicaOsob();

    static void create(Osoba** &s, int N);
    static void usun(Osoba** &s);
    void add(Osoba* o);
    void create(int n);
    //bool Delete(Osoba* s);
    bool Delete(int k);
    void DeleteAll();
    bool Empty() const;
    int SizeOfArray() const;
    Osoba** begin();
    Osoba** end();
    Osoba* operator[](int i);
    void operator+=(Osoba* s);
    TablicaOsob& operator=(TablicaOsob const& other);
    friend ostream& operator<<(ostream& os, TablicaOsob const& sa);
};
ostream& operator<<(ostream& is, TablicaOsob const& sa);
}
#endif // OsobaSARRAY_H
