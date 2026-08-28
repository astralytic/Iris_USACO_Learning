//Monday to Friday

//Learning how to declare variables and compile C++ programs. 

#include <iostream>

int main() {
  
  int score = 0;
  
  std::cout << "Player score:" << score << "\n";

}

#include <iostream>

int main() {
  
  int tip = 0;
  
  std::cout << "Enter tip amount: ";
  std::cin >> tip;
  
  std::cout << "You paid " << tip << " dollars." << "\n";
  
}



#include <iostream>

int main() {
  
  double tempf = 83;
  double tempc;
  
  tempc = (tempf - 32) / 1.8;
  
  std::cout << "The temp is " << tempc << " degrees Celsius. \n";
  
  
}
//Better version below

#include <iostream>

int main() {
  
  double tempf;
  double tempc;
  
  std::cout << "Enter the temperature in Fahrenheit: ";
  
  std::cin >> tempf;
  
  
  tempc = (tempf - 32) / 1.8;
  
  std::cout << "The temp is " << tempc << " degrees Celsius.\n";
  
}
