#ifndef STUDENTSARRAY_H
#define STUDENTSARRAY_H

#include "Student.h"

class StudentsPArray
{
    Student** Elektronika;
    int size;

    public:
        StudentsPArray();
        ~StudentsPArray();

    static void create(Student** &s, int N);
    static void usun(Student** &s);
    void add(Student const& s);
    void create(int n);
    void AddMultiple(int n);
    bool Delete(Student const& s);
    bool Delete(int k);
    void DeleteAll();
    bool Check() const;
    int SizeOfArray() const;

    Student* operator[](int i);
    friend ostream& operator<<(ostream& os, StudentsPArray const& sa);
    void operator+=(Student const& s);
    StudentsPArray& operator=(StudentsPArray const& other);
};
ostream& operator<<(ostream& is, StudentsPArray const& sa);

}
#endif // STUDENTSARRAY_H
