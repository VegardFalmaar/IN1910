#include "linked_array_list.hpp"


int main ()
{
  ArrayListNode node({1, 2, 3}, nullptr, nullptr);
  node.value->print();

  LinkedArrayList lal{}; // Create an empty LinkedArrayList
  lal.append({1, 2});    // Append first list
  lal.append({4, 5, 6}); // Append a second list
  lal.print();           // Print the entire LinkedArrayList
  lal[0]->append(42);    // Append the number 42 to the first ArrayList
  lal.print();           // Print the entire LinkedArrayList again

  return 0;
}


LinkedArrayList::LinkedArrayList () : _length(0) {}


void LinkedArrayList::append (std::vector<int> values)
{
  ArrayListNode *new_node = new ArrayListNode(values, _tail, nullptr);
  if (_length == 0)
    _head = new_node;
  else
    _tail->next = new_node;
  _tail = new_node;
  _length++;
}


void LinkedArrayList::print ()
{
  std::cout << "[\n";
  for (int i=0; i< (int) _length; i++){
    std::cout << "  ";
    operator[](i)->print();
  }
  std::cout << "]\n";
}


std::unique_ptr<ArrayList> &LinkedArrayList::operator[] (int idx)
{
  if ((idx < 0) || (idx >= (int) _length))
    throw std::range_error(
        "Index " + std::to_string(idx)
        + " out of range for array of length " + std::to_string(_length)
    );

  ArrayListNode *node = _head;
  for (int i=0; i<idx; i++)
    node = node->next;
  return node->value;
}


LinkedArrayList::~LinkedArrayList ()
{
  if (_length == 0)
    return;

  if (_length == 1){
    delete _head;
    return;
  }

  ArrayListNode *current = _head, *next;
  for (size_t i=0; i<_length - 1; i++){
    next = current->next;
    delete current;
  }
  delete next;
}
