#ifndef __LINKEDLIST_HPP
#define __LINKEDLIST_HPP

#include <iostream>
#include <vector>

struct Node {
  int value;
  Node* previous = nullptr;
  Node* next = nullptr;
};

class LinkedList
{
  private:
    Node *_head = nullptr;
    Node *_tail = nullptr;
    unsigned int _length;

  public:
    LinkedList ();
    LinkedList (std::vector<int>);
    ~LinkedList ();
    int length ();
    void append (int);
    void remove (int);
    int &operator[] (int);
    void print ();
    void insert (int, int);
    int pop (int);
    int pop();
};

#endif
