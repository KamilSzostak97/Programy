#include "Nauczyciel.h"
#include "Student.h"
#include "StudentsArray.h"
#include "GFX.h"
#include <iostream>

using namespace std;

app::Nauczyciel::Nauczyciel(TablicaOsob* osoby)
{
    this->osoby=osoby;
}

app::Nauczyciel::~Nauczyciel()
{
    //dtor
}

void app::Nauczyciel::wyswietlMenu() const {
    GFX::nauczycielMenu();
}

void app::Nauczyciel::akcja(int wybor){
    switch(wybor){
        case 1:
        cout << adresUczelni;
        break;
    case 2:
        wypis();
        break;
    case 3:
        interfejsDodajOcene();
        break;
    case 4:
        interfejsDodajStudenta();
        break;
    }
}

bool app::Nauczyciel::poprawnyWybor(int wybor)const{
    return wybor >=0 && wybor <= 4;
}

void app::Nauczyciel::dodajStudenta(Student* s){
    if (s != nullptr)
        studenci.push_back(s);
}

void app::Nauczyciel::interfejsDodajOcene(){
    string nazwisko;
    cout << "Podaj nazwisko: ";
    cin >> nazwisko;
    Student* znaleziona = nullptr;
    for (Osoba* o : *osoby){
        if (o->getName() == nazwisko){
            znaleziona = dynamic_cast<Student*>(o);
            if (znaleziona != nullptr)
                break;
        }
    }
    if (znaleziona != nullptr){
        float ocena;
        cout << "Podaj ocene: ";
        cin >> ocena;
        znaleziona->dodajOcene(ocena);
    }
    else{
        cout << "Nie znaleziono podanej osoby\n";
    }
}


void app::Nauczyciel::interfejsDodajStudenta(){
    string nazwisko;
    cout << "Podaj nazwisko: ";
    cin >> nazwisko;
    Student* znaleziona = nullptr;
    for (Osoba* o : *osoby){
        if (o->getName() == nazwisko){
            znaleziona = dynamic_cast<Student*>(o);
            if (znaleziona != nullptr)
                break;
        }
    }
    if (znaleziona != nullptr){
        dodajStudenta(znaleziona);
    }
    else{
        cout << "Nie znaleziono podanej osoby\n";
    }
}

void app::Nauczyciel::ustawDane(){
    Osoba::ustawDane();
    cout << "Podaj wydzial: ";
    cin >>wydzial;
    cout <<"Podaj budynek: ";
    cin>>budynek;
    cout <<"Podaj pokoj: ";
    cin >>pokoj;
}

void app::Nauczyciel::wypis() const{
    cout<<"Dane Nauczyciela"<<endl;
    Osoba::wypis();
    cout << "Wydzial: " <<wydzial << endl;
    cout << "Budynek: " << budynek <<endl;
    cout << "Pokoj: " << pokoj << endl;
    cout<<" "<<endl;
}
