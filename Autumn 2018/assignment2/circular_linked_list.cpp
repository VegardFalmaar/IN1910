#include "iostream"
#include "stdexcept"
#include "vector"

struct Node {
  int value;
  Node* next;

  Node (int val, Node* n) {
    value = val;
    next = n;
  }
};

class CircLinkedList {
private:
  Node* head;
  int size;

public:
  CircLinkedList () {
    head = nullptr;
    size = 0;
  }

  void append (int value) {
    if (size == 0) {
      head = new Node(value, nullptr);
      head->next = head;
    } else {
      Node* current = head;
      while (current->next != head) {
        current = current->next;
      }
      current->next = new Node(value, head);
    }
    size += 1;
  }

  int& operator[] (int index) {
    if (size == 0) {
      throw std::range_error("IndexError: List is empty");
    } else if (index < 0) {
      throw std::range_error("IndexError: Negative index");
    }
    Node* current = head;
    for (int i=0; i<index; i++) {
      current = current->next;
    }
    return current->value;
  }

  void print () {
    std::cout << "[";
    for (int i=0; i<size; i++) {
      std::cout << operator[](i) << ", ";
    }
    std::cout << "...]" << std::endl;
  }

  CircLinkedList (int n) {
    head = new Node(1, nullptr);
    head->next = head;
    for (int i=2; i<=n; i++) {
      append(i);
    }
  }

//  int pop(int index) {
//    while (index <= 0) {
//      index += size;
//    }
//    Node* previous_node = operator[](index-1);
//    Node* current = operator[](index);
//    Node* next_node = operator[](index+1);
//    if (current == head) {
//      next_node = head;
//    }
//    previous_node->next = next_node;
//    int val = current->value;
//    delete[] current;
//    size -= 1;
//    return val;
//  }

  std::vector<int> josephus_sequence(int k) {
    std::cout << "jos seq called" << std::endl;
    std::vector<int> killed;
    Node* previous_node = head;
    Node* current;
    int step;
    for (int i=1; i<size; i++) {
      if (i == 1) {
        step = k-2;
      } else {
        step = k-1;
      }
      for (int j=0; j<step; j++) {
        previous_node = previous_node->next;
      }
      current = previous_node->next;
      previous_node->next = current->next;
      int val = current->value;
      delete[] current;
      size -= 1;
      killed.push_back(val);
    }
    killed.push_back(previous_node->value);
    return killed;
  }

  ~CircLinkedList () {
    Node* current = head->next;
    while (current->next != head) {
      Node* next = current->next;
      delete[] current;
      current = next;
    }
    delete[] current;
    delete[] head;
  }
};

void test_init_append () {
  CircLinkedList list;
  list.append(2);
  list.append(4);
  list.append(6);
  std::cout << list[1] << list[4] << list[6] << std::endl;
  list.print();
}

int last_man_standing (int n, int k) {
  CircLinkedList list(n);
  return list.josephus_sequence(k).back();
}

int main () {
  // test_init_append();

  std::cout << last_man_standing(6, 2) << std::endl;
  return 0;
}
