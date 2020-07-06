#include "StudentsArray.h"

app::StudentsArray::StudentsArray()
{
    Informatyka=NULL;
    size= 0;
}

app::StudentsArray::~StudentsArray()
{
    usun(Informatyka);
}

void app::StudentsArray::create(Student* &s, int N)
{
    s = new class Student[N];
}

void app::StudentsArray::usun(Student* &s){
delete[] s;
s = NULL;
}


void app::StudentsArray::add(Student const& s){
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


app::Student* app::StudentsArray::operator[](int i){
    if (i < 0 || i >= size)
        return NULL;
    else
        return &Informatyka[i];
}


void app::StudentsArray::operator+=(Student const& s){
    add(s);
}


app::StudentsArray& app::StudentsArray::operator=(StudentsArray const& other){
    usun(Informatyka);
    create(Informatyka, other.size);
    size = other.size;
    for (int i=0;i<size;++i){
        Informatyka[i] = other.Informatyka[i];
    }
}


bool app::StudentsArray::Delete(int k){
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


void app::StudentsArray::DeleteAll(){
    usun(Informatyka);
    size = 0;
}


bool app::StudentsArray::Check() const{
    return size == 0;
}


int app::StudentsArray::SizeOfArray() const{
    return size;
}


void app::StudentsArray::AddMultiple(int n){
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


ostream& app::operator<<(ostream& os, app::StudentsArray const& sa){
    for(int i = 0; i < sa.size; i++){
        os << sa.Informatyka[i];
    }
}

