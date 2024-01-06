#include <iostream>

using namespace std;

int triangle(int n) {
  int sum = 0;
  for (int i=1; i<=n; i++) {
    sum += i;
  }
  return sum;
}

int main() {
  // for (int i=1; i<=5; i++) {
  //   cout << triangle(i) << endl;
  // }
  // return 0;

  // int n = 761;
  // cout  << "Function: "
  //       << triangle(n)
  //       << ", Exact: "
  //       << n*(n+1)/2
  //       << endl;

  int n;
  cout << "Please enter a number n: ";
  cin >> n;
  cout << "triangle(n): " << triangle(n) << endl;
}