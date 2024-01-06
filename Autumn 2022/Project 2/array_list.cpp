#include "array_list.hpp"


ArrayList::ArrayList () : _length(0), _capacity(1)
{
  _data = new int[_capacity];
}


ArrayList::ArrayList (std::vector<int> v) : _length(v.size())
{
  _capacity = 1;
  while (_capacity < v.size())
    _capacity *= 2;
  _data = new int[_capacity];
  for (size_t i=0; i<length(); i++)
    _data[i] = v[i];
}


ArrayList::~ArrayList () { delete[] _data; }


size_t ArrayList::length () { return _length; }


void ArrayList::append (int n)
{
  if (length() == _capacity)
    _resize();
  _data[_length] = n;
  _length++;
}


void ArrayList::_resize ()
{
  int *new_data = new int[2*_capacity];
  for (size_t i=0; i<_capacity; i++)
    new_data[i] = _data[i];
  delete[] _data;
  _data = new_data;
  _capacity *= 2;
}


void ArrayList::print ()
{
  using namespace std;
  cout << "[ ";
  for (size_t i=0; i<length(); i++)
    cout << _data[i] << " ";
  cout << "]" << endl;
}


int& ArrayList::operator[] (int idx)
{
  if ((idx < 0) || (idx >= (int) length()))
    throw std::range_error(
        "Index " + std::to_string(idx)
        + " out of range for array of length " + std::to_string(length())
    );
  return _data[idx];
}


void ArrayList::insert (int val, int idx)
{
  if ((idx < 0) || (idx > (int) length()))
    throw std::range_error(
      "Insert index " + std::to_string(idx)
      + " out of range for array of length " + std::to_string(length())
    );
  else if (idx == (int) length())
    append(val);
  else {
    int old_last_element = _data[length() - 1];
    for (size_t i=length() - 1; (int) i>idx; i--)
      _data[i] = _data[i-1];
    _data[idx] = val;
    append(old_last_element);
  }
}


void ArrayList::remove(int idx)
{
  if ((idx < 0) || (idx >= (int) length()))
    throw std::range_error(
        "Index " + std::to_string(idx)
        + " out of range for array of length " + std::to_string(length())
    );
  for (size_t i=idx; i<length() - 1; i++)
    _data[i] = _data[i+1];
  _length--;
  if ((length() / (double) capacity()) < 0.25)
    _shrink_to_fit();
}


int ArrayList::pop (int idx)
{
  const int val = _data[idx];
  remove(idx);
  return val;
}


int ArrayList::pop () { return pop(length() - 1); }


void ArrayList::_shrink_to_fit ()
{
  unsigned int new_capacity = 1;
  while (new_capacity < length())
    new_capacity *= 2;
  int *new_data = new int[new_capacity];
  for (size_t i=0; i<length(); i++)
    new_data[i] = _data[i];
  delete[] _data;
  _data = new_data;
  _capacity = new_capacity;
}


int ArrayList::capacity () { return _capacity; }
