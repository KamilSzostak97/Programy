#ifndef STUDENT_H
#define STUDENT_H

#include <string>
#include <vector>
#include <iostream>
#include "Osoba.h"

using namespace std;
namespace app{
    class Student : public Osoba {
    public:

    private:
        static int lastId;
        int id;
        char Klasa;
        vector<float> oceny;
        void wyswietlOceny() const;
    public:
       Student(Student const& other);
       Student();
       ~Student();
       Student(int id, char klasa);
       Student& operator=(Student const& other);
        void add(int id,char Klas);
        virtual void wypis() const override;
        int getid() const;
        char getKlasa() const;
        void dodajOcene(float ocena);
        virtual void ustawDane() override;
        virtual void wyswietlMenu() const override;
        virtual void akcja(int wybor) override;
        virtual bool poprawnyWybor(int wybor)const override;
        friend ostream& operator<<(ostream& os, Student const& s);
        friend ostream& operator>>(istream& os, Student& s);
    };

    ostream& operator<<(ostream& os, Student const& s);
    ostream& operator>>(istream& os, Student& s);
}

#endif // STUDENT_H
