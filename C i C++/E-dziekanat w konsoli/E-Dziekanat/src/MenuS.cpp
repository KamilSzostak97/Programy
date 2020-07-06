#include "MenuS.h"
#include "GFX.h"

void app::menu::UserMenu::ustawZalogowanego(Osoba* o){
    zalogowany = o;
}

void app::menu::UserMenu::Wyloguj(){
    zalogowany = nullptr;
}


void app::menu::UserMenu::Interfejs()
{
    int U, j=1;
    system("cls");
    zalogowany->wyswietlMenu();
    while(j){
        cout<<endl;
        cout<< "podaj Nr czynnosci ktora chcesz wykonac"<<endl;
        cin>> U;
        if(zalogowany->poprawnyWybor(U))
        {
            if (U == 0)
                return;
            zalogowany->akcja(U);
        }
        else{
            cout<<"Podana Liczba Nie Ma Przypisanego Zadania"<<endl;
        }
    }
}
