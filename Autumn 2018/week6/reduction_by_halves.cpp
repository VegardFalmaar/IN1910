#include <iostream>

using namespace std;

// int main() {
//   int n = 100;
//   while (n > 0) {
//     cout << n << endl;
//     n = n/2;
//   }
//   return 0;
// }

void reduction_by_halves(int n) {
  while (n > 0) {
    cout << n << endl;
    n = n/2;
  }
}

int main() {
  reduction_by_halves(1000);
  return 0;
}