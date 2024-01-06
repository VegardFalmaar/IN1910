#include <iostream>
#include <cmath>
#include <cassert>

#define PI 3.14159265

struct Cartesian {
  double x;
  double y;
};

struct Polar {
  double r;
  double theta;
};

Polar cart2polar (const Cartesian& cartp) {
  double r = std::sqrt(std::pow(cartp.x, 2) + std::pow(cartp.y, 2));
  double theta = std::atan(cartp.y/cartp.x);
  Polar sol{r, theta};
  return sol;
}

Cartesian polar2cart (const Polar& polarp) {
  double x = polarp.r*std::cos(polarp.theta);
  double y = polarp.r*std::sin(polarp.theta);
  Cartesian sol{x, y};
  return sol;
}

void test_convertion () {
  Cartesian cartp{1, 1};
  Polar polarp{1, PI/2};

  double tol = 1E-8;

  Polar actual_p = cart2polar(cartp);
  Polar expected_p{std::sqrt(2), PI/4};
  assert(std::abs(actual_p.r - expected_p.r) < tol);
  assert(std::abs(actual_p.theta - expected_p.theta) < tol);

  Cartesian actual_c = polar2cart(polarp);
  Cartesian expected_c{0, 1};
  assert(std::abs(actual_c.x - expected_c.x) < tol);
  assert(std::abs(actual_c.y - expected_c.y) < tol);

  Cartesian u{1, 3};
  Cartesian v = polar2cart(cart2polar(u));
  assert(std::abs(u.x - v.x) < tol);
  assert(std::abs(u.y - v.y) < tol);
}

Polar scale (const Polar& polarp, double scalar) {
  return {polarp.r*scalar, polarp.theta};
}

Cartesian scale (const Cartesian& cartp, double scalar) {
  return {cartp.x*scalar, cartp.y*scalar};
}

Polar rotate (const Polar& polarp, double omega) {
  return {polarp.r, polarp.theta + omega};
}

Cartesian rotate (const Cartesian& cartp, double omega) {
  double newx = std::cos(omega)*cartp.x - std::sin(omega)*cartp.y;
  double newy = std::sin(omega)*cartp.x + std::cos(omega)*cartp.y;
  return {newx, newy};
}

void test_scaling () {
  double tol = 1E-8;
  double scalar = 2;

  Cartesian cart{1, 1};
  Cartesian c_expected{2, 2};
  Cartesian c_computed = scale(cart, scalar);
  assert(std::abs(c_expected.x - c_computed.x) < tol);
  assert(std::abs(c_expected.y - c_computed.y) < tol);

  Polar pol{1, PI/4};
  Polar p_expected{2, PI/4};
  Polar p_computed = scale(pol, scalar);
  assert(std::abs(p_expected.r - p_computed.r) < tol);
  assert(std::abs(p_expected.theta - p_computed.theta) < tol);
}

void test_rotate () {
  double tol = 1E-8;
  double omega = PI/2;

  Cartesian cart{1, 1};
  Cartesian c_expected{-1, 1};
  Cartesian c_computed = rotate(cart, omega);
  assert(std::abs(c_expected.x - c_computed.x) < tol);
  assert(std::abs(c_expected.y - c_computed.y) < tol);

  Polar pol{1, PI/4};
  Polar p_expected{1, 3*PI/4};
  Polar p_computed = rotate(pol, omega);
  assert(std::abs(p_expected.r - p_computed.r) < tol);
  assert(std::abs(p_expected.theta - p_computed.theta) < tol);
}

int main () {
  double x = 1;
  double y = 1;
  Cartesian cart{x, y};
  Polar pol;
  pol = cart2polar(cart);
  std::cout << pol.r << std::endl
            << pol.theta << std::endl;
  test_convertion();
  test_scaling();
  test_rotate();
  return 0;
}
