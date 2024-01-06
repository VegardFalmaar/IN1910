#include <iostream>

struct Point {
  double x;
  double y;
};

class AffineTransform {
private:
  double a;
  double b;
  double c;
  double d;
  double e;
  double f;

public:
  AffineTransform(double _a, double _b, double _c, double _d, double _e=0, double _f=0) {
    a = _a;
    b = _b;
    c = _c;
    d = _d;
    e = _e;
    f = _f;
  }

  Point evaluate (const Point& p) {
    double xval = a*p.x + b*p.y + e;
    double yval = c*p.x + d*p.y + f;
    return {xval, yval};
  }
};

int main () {
  AffineTransform aff{1, 3, 2, 4};
  Point p{1, 2};
  Point q = aff.evaluate(p);
  std::cout << q.x << std::endl
            << q.y << std::endl;
  return 0;
}
