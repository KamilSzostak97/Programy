#ifndef STUDENTSARRAY_H
#define STUDENTSARRAY_H

#include "Student.h"

namespace app{
class StudentsArray
{
    Student* Informatyka;
    int size;

    public:
        StudentsArray();
        ~StudentsArray();

    static void create(Student* &s, int N);
    static void usun(Student* &s);
    void add(Student const& s);
    void create(int n);
    void AddMultiple(int n);
    bool Delete(Student const& s);
    bool Delete(int k);
    void DeleteAll();
    bool Check() const;
    int SizeOfArray() const;

    Student* operator[](int i);
    void operator+=(Student const& s);
    StudentsArray& operator=(StudentsArray const& other);
    friend ostream& operator<<(ostream& os, StudentsArray const& sa);
};
ostream& operator<<(ostream& is, StudentsArray const& sa);


}
#endif // STUDENTSARRAY_H
