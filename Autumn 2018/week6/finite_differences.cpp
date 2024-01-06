#include <iostream>
#include <vector>

int main() {
  std::vector<double> t(10001);
  std::vector<double> u(10001);
  double u_0 = 15.7;
  double a = 4.3;
  double dt = 0.001;
  t[0] = 0;
  u[0] = u_0;

  for (int i = 1; i < 10001; i++) {
    t[i] = (i-1)*dt;
    u[i] = u[i-1] - a*dt*u[i-1];
  }
}