#ifndef OSOBA_H
#define OSOBA_H

#include <string>
#include <memory>
using namespace std;

namespace app{


    class Adres{
    public:
        string miasto;
        string ulica;
        int numer;
    };

    ostream& operator<<(ostream& os, Adres const& a);

class Osoba
{
    public:
        class DaneLogowania{
            friend class Osoba;
            string login;
            string haslo;
            mutable int nieprawidloweHasla;

        public:
            DaneLogowania();
            DaneLogowania(string const& login, string const& haslo);
        };
        Osoba();
        virtual ~Osoba();
        void ustawDaneLogowania();
        bool sprawdzDaneLogowania(string const& login, string const& haslo) const;
        virtual void wypis() const;
        virtual void ustawDane();
        virtual void wyswietlMenu() const = 0;
        virtual void akcja(int wybor) = 0;
        virtual bool poprawnyWybor(int wybor)const = 0;
        static Adres const& getAdresUczelni();
        bool operator==(DaneLogowania const& login) const;
        string getName() const;
    protected:
        static Adres adresUczelni;
        string name;
    private:
        shared_ptr<DaneLogowania> danelog;
};
}

#endif // OSOBA_H
