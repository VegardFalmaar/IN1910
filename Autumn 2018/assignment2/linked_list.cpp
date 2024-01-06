#include "iostream"
#include "stdexcept"
#include "vector"

// This exercise is solved with doubly linked lists

struct Node {
  int value;
  Node* next;
  Node* previous;

  Node (int val, Node* n, Node* p) {
    value = val;
    next = n;
    previous = p;
  }
};

class LinkedList {
private:
  Node* head;
  Node* tail;
  int size;

public:
  LinkedList () {
    head = nullptr;
    tail = nullptr;
    size = 0;
  }

  ~LinkedList () {
    Node* current;
    current = head;
    while (current->next != nullptr) {
      Node* next = current->next;
      delete[] current;
      current = next;
    }
    delete[] current;
  }

  int length () {
    return size;
  }

  void append(int val) {
    if (head == nullptr) {
      head = new Node(val, nullptr, nullptr);
      tail = head;
    } else if (head == tail) {
      tail = new Node(val, nullptr, head);
      head->next = tail;
    } else {
      Node* prev_tail;
      prev_tail = tail;
      tail = new Node(val, nullptr, prev_tail);
      prev_tail->next = tail;
    }
    size += 1;
  }

  void print () {
    Node* current;
    current = head;
    std::cout << "[";
    while (current->next != nullptr) {
      std::cout << current->value << ", ";
      current = current->next;
    }
    std::cout << current->value << "]" << std::endl;
  }

  int& operator[] (int n) {
    std::cout << "[] called" << std::endl;
    if (n < 0 or n >= size) {
      throw std::range_error("IndexError: Index is out of range");
    }
    Node* current = head;
    for (int i=0; i<n; i++) {
      current = current->next;
    }
    return current->value;
  }

  void insert (int val, int index) {
    if (index < 0 or index > size) {
      throw std::range_error("IndexError: Index out of range");
    } else if (index == 0) {
      Node* oldhead = head;
      head = new Node(val, oldhead, nullptr);
      oldhead->previous = head;
    } else if (index == size) {
      append(val);
    } else {
      Node* old = head;
      for (int i=0; i<index; i++) {
        old = old->next;
      }
      Node* previous_node = old->previous;
      Node* new_node = new Node(val, old->next, old->previous);
      previous_node->next = new_node;
      old->previous = new_node;
    }
    size += 1;
  }

  void remove (int index) {
    std::cout << "Remove called" << std::endl;
    if (index < 0 or index >= size) {
      throw std::range_error("IndexError: Index out of range");
    } else if (index == 0) {
      Node* old_head = head;
      head = head->next;
      head->previous = nullptr;
      delete[] old_head;
    } else if (index == size-1) {
      Node* old_tail = tail;
      tail = tail->previous;
      tail->next = nullptr;
      delete[] old_tail;
    } else {
    Node* current = head;
    for (int i=0; i<index; i++) {
      current = current->next;
    }
    Node* previous_node = current->previous;
    Node* next_node = current->next;
    previous_node->next = next_node;
    next_node->previous = previous_node;
    delete[] current;
    }
    size -= 1;
  }

  int pop (int index) {
    int value = operator[](index);
    remove(index);
    return value;
  }

  int pop () {
    pop(size-1);
  }

  LinkedList (std::vector<int> input) {
    head = new Node(input[0], nullptr, nullptr);
    tail = head;
    size = 1;
    for (int i=1; i<input.size(); i++) {
      append(input[i]);
    }
  }
};

void test_append_length_print_operator () {
  LinkedList list;
  list.append(5);
  std::cout << list.length() << std::endl;
  list.print();

  list.append(10);
  std::cout << list.length() << std::endl;
  list.print();

  list.append(15);
  std::cout << list.length() << std::endl;
  list.print();

  list.append(20);
  std::cout << list.length() << std::endl;
  list.print();

  std::cout << "list[0] = " << list[0] << std::endl;
  list[0] = 17;
  std::cout << "command: list[0] = " << list[0] << std::endl;
  list.print();

  std::cout << list[5] << std::endl;
}

void test_insert () {
  LinkedList list;
  list.append(5);
  list.append(10);
  list.append(15);
  list.append(20);
  list.print();
  std::cout << std::endl;

  list.insert(2, 0);
  list.insert(7, 2);
  list.print();
  list.insert(22, 6);
  list.print();
}

void test_remove () {
  LinkedList list;
  list.append(5);
  list.append(10);
  list.append(15);
  list.append(20);
  list.print();
  std::cout << list.length() << std::endl;

  list.remove(2);
  list.print();
  std::cout << list.length() << std::endl;
}

void test_pop () {
  LinkedList list;
  list.append(5);
  list.append(10);
  list.append(15);
  list.append(20);
  list.print();

  std::cout << list.pop(2) << std::endl;
  list.print();
  std::cout << list.pop(0) << std::endl;
  list.print();

  std::cout << list.pop() << std::endl;
  list.print();
}

void test_list_construct () {
  std::vector<int> input{5, 10, 15, 20};
  std::cout << "Vector created" << std::endl;
  LinkedList list(input);
  std::cout << "List created" << std::endl;
  list.print();
  std::cout << list.pop(2) << std::endl;
  list.print();
}

int main () {
  //test_pop();
  //LinkedList list;
  //list.append(5);
  //list.append(10);
  //list.print();
  //list.remove(1);
  //list.print();
  //test_remove();
  test_list_construct();
  
  //LinkedList list1({5, 10, 15, 20});
  //LinkedList list2;
  //list2.append(5);
  //list2.append(10);
  //list2.append(15);
  //list2.append(20);

  //list1.print();
  //list2.print();

  //std::cout << list1.pop(2) << " " << list2.pop(2) << std::endl;
  //list1.print();
  //list2.print();
  return 0;
}
