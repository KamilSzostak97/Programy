#include "Application.h"
#include "Student.h"
#include "Nauczyciel.h"

app::Application::Application()
{

}


app::Osoba* app::Application::interfejsStworzOsobe(){
    char type;
    do{
        cout << "s - Student, n - Nauczyciel: ";
        cin >> type;
    } while (type != 's' && type != 'n');
    return stworzOsobe(type);
}

app::Osoba* app::Application::stworzOsobe(char typ){
    if (typ == 's')
        return new Student;
    else if (typ == 'n')
        return new Nauczyciel(&osoby);
    else
        return nullptr;
}

void app::Application::operator()(){
    MainMenu();
}

app::Osoba* app::Application::Login(string login, string pass) {
    for (int i=0;i<osoby.SizeOfArray();++i){
        Osoba* o = osoby[i];
        if (*o == Osoba::DaneLogowania{login, pass}){
            menu.ustawZalogowanego(o);
            return o;
        }
    }
    return NULL;
}


void app::Application::MainMenu()
{
    int M, j=1;
    while(j!=0){
        system("cls");
        GFX::mainMenu();
        cout<<endl;
        cout<< "podaj Nr czynnosci ktora chcesz wykonac"<<endl;
        cin>> M;
        while (M < 1 && M > 3){
            cout<<"Podana Liczba Nie Ma Przypisanego Zadania"<<endl;
            cout<< "podaj Nr czynnosci ktora chcesz wykonac"<<endl;
            cin >> M;
        }
        switch(M){
        case 1:
            AdminMenu();
            break;
        case 2:{
            string Login, Pass;
            int wydzial;
            system("cls");
            cout<<"1. Wydzial Informatyki"<<endl;
            //cout<<"2. Wydzial Elektroniki"<<endl;
            cout<<endl;

            cout<<"Liczba niepoprawnych logowan"<<endl;
            if(!osoby.Empty()){
                cout<<endl;

                cout<<"podaj Wydzial"<<endl;
                cin>>wydzial;
                if(wydzial==1){
                    cout<<"Podaj Login"<<endl;
                    cin>>Login;
                    cout<<"Podaj Haslo"<<endl;
                    cin>>Pass;
                    this->Login(Login, Pass);
                    menu.Interfejs();
                }
            }
            else{
                cout<<endl;
                cout<<"brak urzytkownikow"<<endl;
                cout<<"Kliknij dowolny przycisk aby kontynuowac"<<endl;
                char L;
                cin>>L;
            }

            break;
        }
        case 3:
            exit(0);
            break;
        }

    }
}

void app::Application::AdminMenu()
{
    int U, j=1;
    system("cls");
    GFX::adminMenu();
    while(j){
    cout<<endl;
    cout<< "podaj Nr czynnosci ktora chcesz wykonac"<<endl;
    cin>> U;
    if(U<6 && U>0)
    {
        switch(U){
    case 1:
       AddMenu();
        break;
    case 2:
        DeleteMenu();
        break;
    case 3:
    if(osoby.Empty())
    {
        cout<<"Lista Jest Pusta"<<endl;
    }else{
    cout<<endl;
    cout<<"Wydzial Informatyki:"<<endl;
    cout << osoby;
    cout<<endl;
    };
        break;
    case 4:
       MainMenu();
        break;
    case 5:
        exit(0);
        break;

        }
    }else{cout<<"Podana Liczba Nie Ma Przypisanego Zadania"<<endl;}
    }
}



void app::Application::DeleteMenu()
{
    int U, j=1;
    system("cls");
    GFX::usuwanieMenu();
    while(j){
    cout<<endl;
    cout<< "podaj Nr czynnosci ktora chcesz wykonac"<<endl;
    cin>> U;
    if(U<4 && U>0)
    {
        switch(U){
    case 1:
        osoby.DeleteAll();
        break;
    case 2:
        int s;
        cout<<"czy chcesz zobaczyc liste osob"<<endl;
        cout<<"tak[1] / Nie[0] ";
        cin>>s;
        if(s==1)
        {
            cout<<" "<<endl;
            cout<<"Wydzial Informatyki:"<<endl;
            cout << osoby;
            cout<<" "<<endl;
        }
        int k;
        cout<<" == Wydzial Informatyki =="<<endl;
        cout<<"Ktory element chcesz usunac"<<endl;
        cin>>k;
        osoby.Delete(k);
        break;
    case 3:
        AdminMenu();
        break;

        }
    }else{cout<<"Podana Liczba Nie Ma Przypisanego Zadania"<<endl;}
    }
}
void app::Application::AddMenu()
{
    int U, j=1;
    system("cls");
    GFX::dodawanieMenu();
    while(j){
    cout<<endl;
    cout<< "podaj Nr czynnosci ktora chcesz wykonac"<<endl;
    cin>> U;
    if(U<5 && U>0)
    {
        switch(U){
     case 1:
        cout<<"Lista Dla Wydzialu Informatyki"<<endl;
        cout<<"podaj liczbe osob ktorych chesz dodac"<<endl;
        cin>>N1;
        AddMultiple(N1);
        cout<<" "<<endl;
        break;

    case 2:{
        Osoba* o = interfejsStworzOsobe();
        o->ustawDane();
        osoby += o;
       break;
    }
    case 3:
        AdminMenu();
        break;
        }
    }else{cout<<"Podana Liczba Nie Ma Przypisanego Zadania"<<endl;}
    }
}



void app::Application::AddMultiple(int n){
    for (int i = 0; i < n; i++) {
        Osoba* o = interfejsStworzOsobe();
        o->ustawDane();
        osoby += o;
    }
}

