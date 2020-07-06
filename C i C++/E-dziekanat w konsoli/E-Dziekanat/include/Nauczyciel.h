#ifndef NAUCZYCIEL_H
#define NAUCZYCIEL_H

#include "Osoba.h"
#include <vector>

namespace app{

    class TablicaOsob;
    class Student;

class Nauczyciel : public Osoba
{
    public:
        Nauczyciel(TablicaOsob* osoby);
        virtual ~Nauczyciel();
        virtual void wypis() const override;
        virtual void ustawDane() override;
        void dodajStudenta(Student* s);
        void interfejsDodajOcene();
        void interfejsDodajStudenta();
        virtual void wyswietlMenu() const override;
        virtual void akcja(int wybor) override;
        virtual bool poprawnyWybor(int wybor)const override;
    protected:
    private:
        TablicaOsob* osoby;
        string wydzial;
        string budynek;
        int pokoj;
        vector<Student*> studenci;
};
}

#endif // NAUCZYCIEL_H
