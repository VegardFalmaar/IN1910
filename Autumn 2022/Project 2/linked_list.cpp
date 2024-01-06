#include "linked_list.hpp"


LinkedList::LinkedList () : _length(0) {}


LinkedList::LinkedList (std::vector<int> v) : _length(0)
{
  for (auto e : v)
    append(e);
}


LinkedList::~LinkedList ()
{
  const unsigned int num_nodes_to_dealloc = _length;
  for (size_t i=0; i<num_nodes_to_dealloc; i++)
    remove(0);
}


int LinkedList::length () { return _length; }


void LinkedList::append (int val)
{
  Node *new_node = new Node;
  new_node->value = val;
  if (length() == 0)
    _head = new_node;
  else
    _tail->next = new_node;
  new_node->previous = _tail;
  _tail = new_node;
  _length++;
}


void LinkedList::remove (int idx)
{
  if ((idx < 0) || (idx >= (int) length()))
    throw std::range_error(
        "Index " + std::to_string(idx)
        + " out of range for array of length " + std::to_string(length())
    );

  if (_length == 1){
    delete _head;
    _head = nullptr;
    _tail = nullptr;
  } else if (idx == 0){
    Node *second = _head->next;
    delete _head;
    _head = second;
    _head->previous = nullptr;
  } else if (idx == length() - 1){
    Node *new_tail = _tail->previous;
    delete _tail;
    new_tail->next = nullptr;
    _tail = new_tail;
  } else {
    Node *node_before = _head;
    for (int i=0; i<idx - 1; i++)
      node_before = node_before->next;
    Node *node_to_remove = node_before->next;
    Node *node_after = node_to_remove->next;
    delete node_to_remove;
    node_before->next = node_after;
    node_after->previous = node_before;
  }
  _length--;
}


int &LinkedList::operator[] (int idx)
{
  if ((idx < 0) || (idx >= (int) length()))
    throw std::range_error(
        "Index " + std::to_string(idx)
        + " out of range for array of length " + std::to_string(length())
    );

  Node *node = _head;
  for (int i=0; i<idx; i++)
    node = node->next;
  return node->value;
}


void LinkedList::print ()
{
  using namespace std;
  cout << "[ ";
  for (size_t i=0; i<_length; i++)
    cout << operator[](i) << " ";
  cout << "]" << endl;
}


void LinkedList::insert (int val, int idx)
{
  if ((idx < 0) || (idx > (int) length()))
    throw std::range_error(
      "Insert index " + std::to_string(idx)
      + " out of range for array of length " + std::to_string(length())
    );
  else if (idx == (int) length())
    append(val);
  else if (idx == 0){
    Node *new_node = new Node;
    new_node->value = val;
    new_node->next = _head;
    _head = new_node;
    _length++;
  } else {
    Node *node_before = _head;
    for (int i=0; i<idx - 1; i++)
      node_before = node_before->next;
    Node *node_after = node_before->next;

    Node *new_node = new Node;
    new_node->value = val;
    new_node->previous = node_before;
    new_node->next = node_after;

    node_before->next = new_node;
    node_after->previous = new_node;
    _length++;
  }
}


int LinkedList::pop (int idx)
{
  const int val = operator[](idx);
  remove(idx);
  return val;
}


int LinkedList::pop () { return pop(length() - 1); }
