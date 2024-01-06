#include <cassert>
#include "array_list.hpp"


void test_empty_array_has_length_zero ();
void test_array_with_two_elements_appended_has_length_two ();
void test_print ();
void test_indexing_operator ();
void test_vector_constructor ();
void test_insert ();
void test_remove ();
void test_pop_at_index ();
void test_pop ();
void test_shrink_to_fit ();


int main ()
{
  std::cout << "Testing ArrayList:\n";
  test_empty_array_has_length_zero();
  test_array_with_two_elements_appended_has_length_two();
  test_print();
  test_indexing_operator();
  test_vector_constructor();
  test_insert();
  test_remove();
  test_pop_at_index ();
  test_pop();
  test_shrink_to_fit();

  std::cout << "Tests passed!\n" << std::endl;

  return 0;
}


void test_empty_array_has_length_zero ()
{
  ArrayList a;
  assert (a.length() == 0);
}


void test_array_with_two_elements_appended_has_length_two ()
{
  ArrayList a;
  a.append(9);
  a.append(8);
  assert(a.length() == 2);
}


void test_print ()
{
  ArrayList a;
  a.append(4);
  a.append(2);
  std::cout << "Printing array:\n";
  a.print();
}


void test_indexing_operator ()
{
  ArrayList a;
  a.append(4);
  a.append(2);
  a.append(3);
  assert(a[0] == 4);
  assert(a[1] == 2);
  assert(a[2] == 3);
  a[2] = 1;
  assert(a[2] == 1);

  bool exception_thrown = false;
  try {
    a[-1];
  } catch (std::range_error &e) {
    exception_thrown = true;
  }
  assert(exception_thrown);

  exception_thrown = false;
  try {
    a[3];
  } catch (std::range_error &e) {
    exception_thrown = true;
  }
  assert(exception_thrown);
}


void test_vector_constructor ()
{
  ArrayList primes({2, 3, 5, 7, 11});
  assert(primes[0] == 2);
  assert(primes[1] == 3);
  assert(primes[2] == 5);
  assert(primes[3] == 7);
  assert(primes[4] == 11);
}


void test_insert()
{
    ArrayList a{{0, 1}};
    assert(a.length() == 2);
    a.insert(42, 0);
    assert(a.length() == 3);
    assert(a[0] == 42);
    assert(a[1] == 0);
    assert(a[2] == 1);
    a.insert(43, 1);
    assert(a.length() == 4);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);
    a.insert(44, 4);
    assert(a.length() == 5);
    assert(a[0] == 42);
    assert(a[1] == 43);
    assert(a[2] == 0);
    assert(a[3] == 1);
    assert(a[4] == 44);

    bool exception_thrown = false;
    try {
      a.insert(100, -1);
    } catch (std::range_error &e) {
      exception_thrown = true;
    }
    assert(exception_thrown);

    exception_thrown = false;
    try {
      a.insert(100, 6);
    } catch (std::range_error &e) {
      exception_thrown = true;
    }
    assert(exception_thrown);
}


void test_remove ()
{
  ArrayList a({ 0, 1, 2, 3, 4 });

  a.remove(2);
  assert(a.length() == 4);
  assert(a[0] == 0);
  assert(a[1] == 1);
  assert(a[2] == 3);
  assert(a[3] == 4);

  a.remove(3);
  assert(a.length() == 3);
  assert(a[0] == 0);
  assert(a[1] == 1);
  assert(a[2] == 3);

  a.remove(0);
  assert(a.length() == 2);
  assert(a[0] == 1);
  assert(a[1] == 3);
}


void test_pop_at_index ()
{
  ArrayList a({ 0, 1, 2, 3, 4 });

  assert(a.pop(2) == 2);
  assert(a.length() == 4);
  assert(a[0] == 0);
  assert(a[1] == 1);
  assert(a[2] == 3);
  assert(a[3] == 4);

  assert(a.pop(3) == 4);
  assert(a.length() == 3);
  assert(a[0] == 0);
  assert(a[1] == 1);
  assert(a[2] == 3);

  assert(a.pop(0) == 0);
  assert(a.length() == 2);
  assert(a[0] == 1);
  assert(a[1] == 3);
}


void test_pop()
{
  ArrayList a({ 0, 1, 2, 3, 4 });

  assert(a.pop() == 4);
  assert(a.length() == 4);
  assert(a[0] == 0);
  assert(a[1] == 1);
  assert(a[2] == 2);
  assert(a[3] == 3);

  assert(a.pop() == 3);
  assert(a.length() == 3);
  assert(a[0] == 0);
  assert(a[1] == 1);
  assert(a[2] == 2);

  assert(a.pop() == 2);
  assert(a.length() == 2);
  assert(a[0] == 0);
  assert(a[1] == 1);
}


void test_shrink_to_fit ()
{
  ArrayList a;
  for (int i=0; i<700; i++)
    a.append(i);
  assert(a.capacity() == 1024);
  for (int i=0; i<650; i++)
    a.pop();
  assert(a.capacity() == 64);
}
