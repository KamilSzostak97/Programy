#include "Osoba.h"
#include <iostream>

app::Adres app::Osoba::adresUczelni = {"Boston", "afrykanska", 67};

app::Osoba::Osoba()
{
    danelog=make_shared<DaneLogowania>();
}

app::Osoba::~Osoba()
{
    //dtor
}

string app::Osoba::getName() const{
    return name;
}

void app::Osoba::ustawDaneLogowania(){
    cout<<"Podaj Login : ";
    cin >> danelog->login;
    cout<<"Podaj Haslo : ";
    cin >> danelog->haslo;
}


void app::Osoba::ustawDane(){
    ustawDaneLogowania();
    cout << "Podaj nazwisko: ";
    cin>> name;
}

bool app::Osoba::operator==(DaneLogowania const& dane) const{
    return danelog->login == dane.login && danelog->haslo == dane.haslo;
}


bool app::Osoba::sprawdzDaneLogowania(string const& login, string const& haslo) const {
    if (danelog->login != login)
        return false;
    if (danelog->nieprawidloweHasla >= 3){
        return false;
    }
    if (danelog->haslo == haslo){
        danelog->nieprawidloweHasla = 0;
        return true;
    }
    else{
        danelog->nieprawidloweHasla++;
        return false;
    }
}


app::Osoba::DaneLogowania::DaneLogowania(string const& login, string const& haslo){
    this->haslo=haslo;
    this->login=login;
    nieprawidloweHasla = 0;
}

app::Osoba::DaneLogowania::DaneLogowania(){
    this->haslo="";
    this->login="";
    nieprawidloweHasla=0;
}

void app::Osoba::wypis() const {
    cout << "Nazwisko: " << name <<endl;
}



ostream& app::operator<<(ostream& os, Adres const& a){
    return os << a.miasto << ", ul " << a.ulica << " " << a.numer;
}

app::Adres const& app::Osoba::getAdresUczelni(){
    return adresUczelni;
}

