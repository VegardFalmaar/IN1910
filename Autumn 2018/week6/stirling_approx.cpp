#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

double stirling(int x) {
  return x*log(x) - x;
}

int main() {
  vector<int> xs {2, 5, 10, 50, 100, 1000};

  for (int x : xs) {
    cout
        << "Computed: "
        << stirling(x)
        << ", Exact: "
        << lgamma(x+1)
        << endl;
  }
  return 0;
}