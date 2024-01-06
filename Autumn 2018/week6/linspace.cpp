#include <iostream>
#include <vector>
#include <cmath>
#include <cassert>

#define PI std::acos(-1)

std::vector<double> linspace(double a, double b) {
  std::vector<double> points;
  double spacing = (b - a)/49;
  for (int i=0; i<50; i++) {
    points.push_back(a + i*spacing);
  }
  return points;
}

std::vector<double> linspace(double a, double b, int n) {
  std::vector<double> points;
  double spacing = (b - a)/(n - 1);
  for (int i=0; i<n; i++) {
    points.push_back(a + i*spacing);
  }
  return points;
}

void test_linspace() {
  auto vec = linspace(1, 50);
  assert(vec[0] == 1);
  assert(vec[vec.size()-1] == 50);
  assert(vec.size() == 50);

  vec = linspace(0, PI, 1000);
  assert(vec[0] == 0);
  assert(vec[vec.size()-1] == PI);
  assert(vec.size() == 1000);
}

int main() {
  // std::cout << linspace(0.5, 100, 200)[49] << std::endl;

  test_linspace();

  return 0;
}

