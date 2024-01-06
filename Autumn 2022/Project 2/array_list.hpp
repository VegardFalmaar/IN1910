#ifndef __ARRAYLIST_HPP
#define __ARRAYLIST_HPP

#include <iostream>
#include <stdexcept>
#include <vector>

class ArrayList
{
  private:
    size_t _length;
    int *_data;
    size_t _capacity;
    void _resize ();
    void _shrink_to_fit ();

  public:
    ArrayList ();
    ArrayList (std::vector<int>);
    ~ArrayList ();
    size_t length ();
    void append (int);
    void print ();
    int &operator[] (int);
    void insert (int, int);
    void remove(int);
    int pop (int);
    int pop ();
    int capacity ();
};

#endif
