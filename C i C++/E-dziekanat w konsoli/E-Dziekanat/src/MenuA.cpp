#include "MenuA.h"

////////
void app::menu::MenuA::dane(string dane, int &N){
    cout << dane;
    cin >> N;
}
void app::menu::MenuA::dane2(string dane, char &N){
    cout << dane;
    cin >> N;
}
////////


//S2.Start
void app::menu::MenuA::create(Student** &s, int N)
{
    s = new Student*[N];
    for (int i = 0; i < N; i++) {
        s[i] = new Student[N];
    }
}

void app::menu::MenuA::usun(Student** &s, int N){
for (int i = 0; i < N; i++) {
    delete[] s[i];
}
delete[] s;
s = NULL;
}

void app::menu::MenuA::add(Student** s, int N,char S){
    int id;
    char Klasa;
    for (int i = 0; i < N; i++) {
        dane ("Numer ID   : ", id);
        dane2("Klasa (A-Z): ",Klasa);
        s[i]->ustawDaneLogowania();
        s[i]->add(id,Klasa);


    }
}

void app::menu::MenuA::wypis(Student** s,int N){
    for (int i = 0; i < N; i++) {
        s[i]->wypis();
    }
}

void app::menu::MenuA::AddNext(Student** &s, int &N, int id, char Klasa){
    Student** temp = NULL;
    create(temp, (N+1));
    for(int i = 0; i < N; i++){
        *temp[i] = *s[i];
    }
    temp[N]->add(id,Klasa);
    temp[N]->ustawDaneLogowania();
    usun(s, N);
    N++;
    s = temp;
}

void app::menu::MenuA::usunWyb(Student** &s, int &N, int k){
    int j = 0;
    Student ** temp = NULL;
    create(temp, (N-1));
    for(int i = 0; i < (N); i++){
        if((k-1) != i){
            temp[j]->add(s[i]->getid(),s[i]->getKlasa());
            j++;
        }
    }
    usun(s, N);
    N--;
    s = temp;
}
