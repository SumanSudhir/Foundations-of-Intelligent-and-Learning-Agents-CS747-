#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

int main(int argc, char *argv[]){

  //  std::cout << argv[1] << ", " << argv[2] << "\n";
  std::ifstream f1;
  f1.open(argv[1]);

  std::ifstream f2;
  f2.open(argv[2]);

  unsigned int n = 0;
  double x = 0;
  double y = 0;
  double d = 0;
  
  while(f1 >> x){
    f2 >> y;

    n += 1;
    d += (x - y) * (x - y);
  }
  
  std::cout << d << "\n";
  
  f1.close();
  f2.close();

  
  return 0;
}
