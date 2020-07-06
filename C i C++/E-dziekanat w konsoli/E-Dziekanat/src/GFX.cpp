#include "GFX.h"

void app::GFX::mainMenu()
{
cout<< "/====================|"<<endl;
cout<< "|     Main Menu      |" <<endl;
cout<< "|                    |" <<endl;
cout<< "|   1.Administrator  |" <<endl;
cout<< "|   2.Logowanie      |" <<endl;
cout<< "|   3.Zakoncz        |" <<endl;
cout<< "|                    |" <<endl;
cout<< "|====================/" <<endl;
}

void app::GFX::adminMenu()
{
cout<< "/====================|"<<endl;
cout<< "|     Admin Menu     |" <<endl;
cout<< "|                    |" <<endl;
cout<< "|   1.Dodawanie      |" <<endl;
cout<< "|   2.Usuwanie       |" <<endl;
cout<< "|   3.Wyswietlanie   |" <<endl;
cout<< "|   4.Powrot         |" <<endl;
cout<< "|   5.Zakoncz        |" <<endl;
cout<< "|                    |" <<endl;
cout<< "|====================/" <<endl;
}

void app::GFX::dodawanieMenu()
{
cout<< "/====================|"<<endl;
cout<< "|  1.Dodawanie       |" <<endl;
cout<< "|                    |" <<endl;
cout<< "|  1.Utworz Liste    |" <<endl;
cout<< "|  2.Dodaj osobe     |" <<endl;
cout<< "|  3.Powrot          |" <<endl;
cout<< "|                    |" <<endl;
cout<< "|====================/" <<endl;
}

void app::GFX::usuwanieMenu()
{
cout<< "/======================|"<<endl;
cout<< "|   2.Usuwanie         |" <<endl;
cout<< "|                      |" <<endl;
cout<< "|   1.Usun Wszystko    |" <<endl;
cout<< "|   2.Usun Wybrany     |" <<endl;
cout<< "|   3.Powrot           |" <<endl;
cout<< "|                      |" <<endl;
cout<< "|======================/" <<endl;
}

void app::GFX::studentMenu()
{
cout<< "/======================|"<<endl;
cout<< "|   Student Menu       |" <<endl;
cout<< "|                      |" <<endl;
cout<< "|   1.Wyswietl Adres   |" <<endl;
cout<< "|   2.Wyswietl Dane    |" <<endl;
cout<< "|   3.Sprawdz oceny    |" <<endl;
cout<< "|   0.Powrot           |" <<endl;
cout<< "|                      |" <<endl;
cout<< "|======================/" <<endl;
}

void app::GFX::nauczycielMenu()
{
cout<< "/======================|"<<endl;
cout<< "|   Nauczyciel Menu    |" <<endl;
cout<< "|                      |" <<endl;
cout<< "|   1.Wyswietl Adres   |" <<endl;
cout<< "|   2.Wyswietl Dane    |" <<endl;
cout<< "|   3.Dodaj ocene      |" <<endl;
cout<< "|   4.Dodaj studenta   |" <<endl;
cout<< "|   0.Powrot           |" <<endl;
cout<< "|                      |" <<endl;
cout<< "|======================/" <<endl;
}
