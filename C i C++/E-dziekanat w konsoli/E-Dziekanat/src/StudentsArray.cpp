#include "StudentsArray.h"
#include <iostream>

using namespace std;

//Pojedynczy Pointer

app::TablicaOsob::TablicaOsob()
{
    osoby=NULL;
    size= 0;
}

app::TablicaOsob::~TablicaOsob()
{
    usun(osoby);
}

void app::TablicaOsob::create(Osoba** &s, int N)
{
    s = new Osoba*[N];
}

void app::TablicaOsob::usun(Osoba** &s){
delete[] s;
s = NULL;
}

void app::TablicaOsob::add(Osoba* o){
    Osoba** temp = NULL;
    create(temp, (size+1));
    for(int i = 0; i < size; i++){
        temp[i] = osoby[i];
    }
    //temp[size] = Osoba::interfejsStworzOsobe();
    //temp[size]->ustawDaneLogowania();
    temp[size] =o;
    usun(osoby);
    size++;
    osoby = temp;
}

bool app::TablicaOsob::Delete(int k){
    int j = 0;
    Osoba** temp = NULL;
    create(temp, (size-1));
    for(int i = 0; i < size; i++){
        if((k-1) != i){
            temp[j]= osoby[i];
            j++;
        }
    }
    usun(osoby);
    size--;
    osoby = temp;
}


void app::TablicaOsob::DeleteAll(){
    usun(osoby);
    size = 0;
}

app::Osoba** app::TablicaOsob::begin(){
    return osoby;
}

app::Osoba** app::TablicaOsob::end(){
    return osoby + size;
}

bool app::TablicaOsob::Empty() const{
    return size == 0;
}


int app::TablicaOsob::SizeOfArray() const{
    return size;
}


app::Osoba* app::TablicaOsob::operator[](int i){
    if (i < 0 && i >= size)
        return NULL;
    else
        return osoby[i];
}


void app::TablicaOsob::operator+=(Osoba* s){
    add(s);
}


app::TablicaOsob& app::TablicaOsob::operator=(TablicaOsob const& other){
    usun(osoby);
    create(osoby, other.size);
    size = other.size;
    for (int i=0;i<size;++i){
        osoby[i] = other.osoby[i];
    }
}

ostream& app::operator<<(ostream& os, app::TablicaOsob const& sa){
    for(int i = 0; i < sa.size; i++){
        sa.osoby[i]->wypis();
    }
}



