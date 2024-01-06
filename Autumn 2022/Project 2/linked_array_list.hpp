#ifndef __LINKEDARRAYLIST_HPP
#define __LINKEDARRAYLIST_HPP

#include <memory>
#include "array_list.hpp"

struct ArrayListNode {
  std::unique_ptr<ArrayList> value;
  ArrayListNode *previous = nullptr;
  ArrayListNode *next = nullptr;

  ArrayListNode (
      std::vector<int> values,
      ArrayListNode *prev,
      ArrayListNode *next
  ) {
    value = std::make_unique<ArrayList>(values);
  }
};

class LinkedArrayList {
  private:
    ArrayListNode *_head = nullptr;
    ArrayListNode *_tail = nullptr;
    unsigned int _length;

  public:
    LinkedArrayList ();
    void append(std::vector<int>);
    void print ();
    std::unique_ptr<ArrayList> &operator[] (int);
    ~LinkedArrayList ();
};

#endif
