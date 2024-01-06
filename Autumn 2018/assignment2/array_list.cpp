#include "iostream"
#include "vector"
#include "stdexcept"

class ArrayList {
private:
  int *data;
  int capacity;
  int size;

  void resize () {
    int *old = data;
    data = new int[capacity];
    for (int i=0; i<size; i++) {
      data[i] = old[i];
    }
    delete[] old;
  }

public:
  ArrayList () {
    capacity = 1;
    size = 0;
    data = new int[capacity];
  }

  ArrayList (std::vector<int> v) {
    size = 0;
    capacity = v.size();
    data = new int[capacity];
    for (int e: v) {
      append(e);
    }
  }

  ~ArrayList () {
    delete[] data;
  }

  int length () {
    return size;
  }

  void append (int x) {
    if (size == capacity) {
      capacity += 2;
      resize();
    }
    data[size] = x;
    size += 1;
  }

  void print () {
    std::cout << "[";
    for (int i=0; i<size-1; i++) {
      std::cout << data[i];
      std::cout << ", ";
    }
    std::cout << data[size-1] << "]" << std::endl;
  }

  int& operator[] (int index) {
    if (index < 0 or index >= size) {
      throw std::range_error("IndexError: Index is out of range.");
    }
    return data[index];
  }

  void insert(int val, int index) {
    if (index < 0 or index > size) {
      throw std::range_error("IndexError: Index is out of range.");
    } else if (index == size) {
      append(val);
      return;
    }
    int old = data[index];
    data[index] = val;
    while (index < size-1) {
      index += 1;
      val = old;
      old = data[index];
      data[index] = val;
    }
    append(old);
  }

  void remove (int index) {
    if (index < 0 or index >= size) {
      throw std::range_error("IndexError: Index is out of range.");
    } else if (index == size-1) {
      pop();
      return;
    }
    for (int i=index; i<size-1; i++) {
      data[i] = data[i+1];
    }
    size -= 1;
    shrink_to_fit_decider();
  }

  int pop () {
    int val = data[size-1];
    size -= 1;
    shrink_to_fit_decider();
    return val;
  }

  int pop (int index) {
    int val = data[index];
    remove(index);
    return val;
  }

  void shrink_to_fit () {
    std::cout << "    capacity " << capacity << std::endl;
    std::cout << "        size " << size << std::endl;
    capacity = 1;
    while (capacity < size) {
      capacity *= 2;
    }
    resize();
    std::cout << "New capacity " << capacity << std::endl;
    std::cout << "New     size " << size << std::endl;
  }

  void shrink_to_fit_decider() {
    if (size < 0.25*capacity) {
      shrink_to_fit();
    }
  }
};

bool is_prime (int n) {
  if (n == 1) {
    return true;
  }
  for (int i=2; i<=n/2; i++) {
    if (n%i == 0) {
      return false;
    }
  }
  return true;
}

int test_primes () {
  ArrayList primes;
  int i = 1;
  while (primes.length() < 10) {
    if (is_prime(i)) {
      primes.append(i);
    }
    i += 1;
  }
  primes.print();
  return 0;
}

int main() {
  // ArrayList list({1, 2, 3, 4});
  // list.append(5);
  // list.append(6);
  // list.append(7);
  // list.append(8);
  // list.append(9);
  // list.print();
  // std::cout << list[1] << std::endl;
  // list[1] = 3;
  // list.print();
  // std::cout << list[1] << std::endl;

  // list.insert(5, 3);
  // list.insert(2, 1);
  // list.print();
  // int x = list.pop();
  // list.print();
  // std::cout << x << std::endl;
  // list.remove(5);
  // list.print();
  // list.remove(1);
  // list.print();
  // int x = list.pop(0);
  // std::cout << x << std::endl;
  // list.print();
  // list.shrink_to_fit();

  ArrayList list;
  for (int i=1; i<1030; i++) {
    list.append(i);
  }
  std::cout << list.length() << std::endl;
  for (int i=1; i<4; i++) {
    for (int j=1; j<271; j++) {
      list.pop();
    }
    std::cout << list.length() << std::endl;
  }
  list.shrink_to_fit();
  return 0;
}
