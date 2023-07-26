

# include <bits/stdc++.h>
using namespace std;

/// You're able to define a data type structure

struct Books
{
  char Title[20];
  char Author[20];
  int ID;
  float price;
}book1;

// book1 as global variable

// To access any member of a structure, we must use
// the member access operator dot.

int main ()
{
  book1.ID = 10;
  book1.price = 13.67;

  // Put strings
  strcpy(book1.Title, "Data structures");
  strcpy(book1.Author, "Mark");

  // Print with cout

  // Parece uma concatenação, uma atribuição louca de parametros
  // Para resultar no cout
  cout<<"Book1 title is: "<<book1.Title<<"\n";

  cout<<"Book1 ID is "<<book1.ID<<"\n";

  cout<<"ID: "<<book1.ID<<" and the price:"<<book1.price<<"\n";

  // Declare book2 as local var:
  // Datatype Books created with struct is here called
  Books book2;

  book2.ID = 100;
  cout<<book2.ID<<"\n";
}
