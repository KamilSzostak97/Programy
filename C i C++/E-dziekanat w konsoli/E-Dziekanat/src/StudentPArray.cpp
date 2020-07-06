#include "StudentPArray.h"

//Pointer Array

app::StudentsPArray::StudentsPArray()
{
    Informatyka=NULL;
    size= 0;
}

app::StudentsPArray::~StudentsPArray()
{
    usun(Informatyka);
}

void app::StudentsPArray::create(Student* &s, int N)
{
    s = new class Student[N];
}

void app::StudentsPArray::usun(Student* &s){
delete[] s;
s = NULL;
}

void app::StudentsPArray::add(Student const& s){
    Student* temp = NULL;
    create(temp, (size+1));
    for(int i = 0; i < size; i++){
        temp[i] = Informatyka[i];
    }
    temp[size] = s;
    usun(Informatyka);
    size++;
    Informatyka = temp;
}

bool app::StudentsPArray::Delete(int k){
    int j = 0;
    Student* temp = NULL;
    create(temp, (size-1));
    for(int i = 0; i < size; i++){
        if((k-1) != i){
            temp[j]= Informatyka[i];
            j++;
        }
    }
    usun(Informatyka);
    size--;
    Informatyka = temp;
}


void app::StudentsPArray::DeleteAll(){
    usun(Informatyka);
    size = 0;
}


bool app::StudentsPArray::Check() const{
    return size == 0;
}


int app::StudentsPArray::SizeOfArray() const{
    return size;
}


void app::StudentsPArray::AddMultiple(int n){
    usun(Informatyka);
    create(Informatyka, n);
    int id;
    char Klasa;
    size = n;
    for (int i = 0; i < size; i++) {
        cout << "klasa: ";
        cin >> Informatyka[i];
        Informatyka[i].ustawDaneLogowania();

    }
}

app::Student* app::StudentsPArray::operator[](int i){
    if (i < 0 && i >= size)
        return NULL;
    else
        return &Informatyka[i];
}


void app::StudentsPArray::operator+=(Student const& s){
    add(s);
}


app::StudentsPArray& app::StudentsPArray::operator=(StudentsPArray const& other){
    usun(Informatyka);
    create(Informatyka, other.size);
    size = other.size;
    for (int i=0;i<size;++i){
        Informatyka[i] = other.Informatyka[i];
    }
}

ostream& app::operator<<(ostream& os, app::StudentsPArray const& sa){
    for(int i = 0; i < sa.size; i++){
        os << sa.Informatyka[i];
    }
}

//Pointer Array


