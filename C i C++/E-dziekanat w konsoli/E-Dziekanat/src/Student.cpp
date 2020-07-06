#include "Student.h"
#include "GFX.h"
#include <cstdlib>
#include <iostream>
using namespace std;

int app::Student::lastId = 0;

void app::Student::add(int id,char Klasa){

    this->id = id;
    this->Klasa=Klasa;

}

void app::Student::wypis() const{
    cout<< "Dane Studenta"<<endl;
    Osoba::wypis();
    cout << "Id: " << this->id << endl;
    cout << "Klasa: " << this->Klasa << endl;
    cout<< " "<<endl;
}

void app::Student::dodajOcene(float ocena){
    if (ocena < 2.0 || ocena > 5.0)
        return;
    oceny.push_back(ocena);
}

int app::Student::getid() const{
    return this->id;
}

char app::Student::getKlasa() const
{
    return this->Klasa;
}

app::Student::Student(int id, char klasa){
    this->id = id;
    this->Klasa = klasa;
}

app::Student::Student():
    Student(++lastId,0)
{
}

app::Student::~Student(){
}

app::Student::Student(app::Student const& other)
{
    this->id = other.id;
    this->Klasa = other.Klasa;
}


app::Student& app::Student::operator=(Student const& other){
    id = other.id;
    Klasa = other.Klasa;
    return *this;
}

void app::Student::ustawDane(){
    Osoba::ustawDane();
    cout << "Podaj id: ";
    cin >> id;
    cout << "Podaj klase: ";
    cin >> Klasa;
}


ostream& app::operator<<(ostream& os, app::Student const& s){
    return os << "Id: " << s.id  <<endl << "Klasa: " << s.Klasa<<endl;
}

ostream& app::operator>>(istream& is, app::Student& s){
    is >> s.Klasa;
}

void app::Student::wyswietlMenu() const {
    GFX::studentMenu();
}

void app::Student::akcja(int wybor){
    switch(wybor){
    case 1:
        cout << adresUczelni;
        break;
    case 2:
        wypis();
        break;
    case 3:
        wyswietlOceny();
        break;
    }
}

bool app::Student::poprawnyWybor(int wybor) const {
    return wybor >= 0 && wybor <= 3;
}

void app::Student::wyswietlOceny() const{
    for (float f : oceny)
        cout << f << " ";
    cout << endl;
}

