#include <iostream>
#include <map>
#include <cmath>
#include <sstream>
#include <regex>
#include <string>

class Polynomial {
private:
  std::map<int, double> coeffs;

public:
  inline Polynomial (std::map<int, double> input): coeffs{input} {}

  double operator () (double x) {
    double sum = 0;
    for (std::pair<int, double> element: coeffs) {
      sum += element.second*std::pow(x, element.first);
    };
    return sum;
  }

  void print() {
    std::ostringstream stream;
    // A map is default sorted ascending. We therefore
    // traverse the liste backward, hence rbegin and rend, instead
    // of begin and end. We replace std::map<int, double>::reverse_iterator
    // with auto.
    for (auto pair = coeffs.rbegin(); pair != coeffs.rend(); ++pair) {
        stream << pair->second << "x^" << pair->first << " + ";
    }
    std::string result = stream.str();

    // Fix up uglyness (not important)
    result = std::regex_replace(result, std::regex{" \\+ -"}, " - ");
    result = std::regex_replace(result, std::regex{"x\\^0"}, "");
    result = std::regex_replace(result, std::regex{"1x"}, "x");

    // Remove last ' + '
    result = result.substr(0, result.size()-3);

    std::cout << result << std::endl;
  }
};

int main () {
  std::map<int, double> coeffs;
  coeffs[10] = 1;
  coeffs[5] = -5;
  coeffs[0] = 1;
  Polynomial f{coeffs};
  //alternativt Polynomial f{{{10, 1}, {5, -5}, {0, 1}}};
  f.print();
  std::cout << f(-2) << std::endl
            << f(0) << std::endl
            << f(2) << std::endl;
  return 0;
}
