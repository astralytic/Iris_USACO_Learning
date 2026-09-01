//Sat Aug 29, 2026

#include <iostream>
using namespace std;

int main() {
    int x;
    cout << "Enter a number: ";
    cin >> x;
    bool b;
    b = (x % 2 == 0);
  // OR
  // if (x % 2 == 1)
  //   b = true;
  // if (x % 2 == 0)
  //   b = false;

    cout << b << ", it is " << (b ? "even" : "odd") << endl;
    return 0;
}
