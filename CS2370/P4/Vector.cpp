#include "Vector.h"
#include "test.h"
#include <iostream>
#include <cstddef>
#include <stdexcept>
using namespace std;
using std::size_t;

// constructor
Vector::Vector(){
    data_ptr = new int[CHUNK];
    capacity = CHUNK;
    n_elems = 0;
}
// copy constructor
Vector::Vector(const Vector &v){
    this->capacity = v.capacity;
    this->data_ptr = new int[this->capacity];
    this->n_elems = v.n_elems;
    for(int i = 0;i<v.n_elems;i++){
        this->data_ptr[i] = v.at(i);
    }
}
//equal overload
Vector& Vector::operator=(const Vector &v){
    this->capacity = v.capacity;
    this->data_ptr = new int[this->capacity];
    this->n_elems = v.n_elems;
    for(int i = 0;i<v.n_elems;i++){
        this->data_ptr[i] = v.at(i);
    }
    return (*this);
}
//destructor
Vector::~Vector(){
    delete[] data_ptr;
}
//insert int at pos 0    
int Vector::front() const{
    if (this-> n_elems == 0){
        throw range_error("out of bounds");
    }else {
        return this->data_ptr[0];
    }
}
// returns last element on array
int Vector::back() const{
    if (this->n_elems == 0){
        throw range_error("out of bounds");
    }else{
        return this->data_ptr[n_elems-1];
    }
}

// returns element at pos x
int Vector::at(size_t pos) const{
    if (this->n_elems == 0){
        throw range_error("out of bounds");
    }else if (pos <= 0 && pos >= this->n_elems){
        throw range_error("out of bounds");
    }else{
        return this->data_ptr[pos];
    }
    
}
//returns size of vector
size_t Vector::size() const{
    return (size_t)this->n_elems;
}

// returns bool on if vector is empty or not
bool Vector::empty() const{
    return this->n_elems == 0;
}
// returns vector at pos x with no bound checks
int& Vector::operator[](size_t pos){
    return this->data_ptr[pos];
}

//appends new element to end of arr
void Vector::push_back(int item){
    if (this->n_elems < this->capacity){
        this->data_ptr[n_elems++] = item;
    }else{
        this->capacity = ((this->capacity*16)/10);
        int* temp = new int[this->capacity];
        for (int x =0; x < this->n_elems; x++){
            temp[x] = data_ptr[x];
        }
        delete[] this->data_ptr;
        this->data_ptr = temp;
        this->data_ptr[n_elems] = item;
        n_elems++;
    }
}

void Vector::pop_back(){
    if(n_elems==0){
        throw range_error("Out of bound");
    }else{
        n_elems--;
    }
}
// erases item at pos x and fills in
void Vector::erase(size_t pos){
    if (pos < this->n_elems){
        for(int x = pos; x < this->n_elems; x++){
            data_ptr[x] = data_ptr[x+1];
        }
        n_elems--;
    }else{
        throw range_error("out of bounds");
    }
}
// moves elements at x and up 1 right of pos x and inserts element at pos x
void Vector::insert(size_t pos, int item){ 
    if(capacity==n_elems){
        capacity = (capacity*16)/10;
        int* temp_ptr = new int[capacity];
        for(int i=0;i<n_elems;i++){
            temp_ptr[i] = data_ptr[i];
        } 
        delete[] data_ptr;
        data_ptr = temp_ptr;
    }
    for(int i=n_elems;i>pos;i--){
        data_ptr[i] = data_ptr[i-1];
    }
    data_ptr[pos] = item;
    n_elems++;
}
// clears the vector elements
void Vector::clear(){
    delete[] data_ptr;
    data_ptr = new int[CHUNK];
    capacity = CHUNK;
    n_elems = 0;
}
// returns pointer on first element
int* Vector::begin(){
    if(n_elems==0)return NULL;
    return &data_ptr[0];
} 
// returns pointer to last element
int* Vector::end(){
    if(n_elems==0)return NULL;
    return &data_ptr[n_elems];
}   

// == operator overload
bool Vector::operator==(const Vector &v) const{
    if(this->capacity!=v.capacity){
        return false;
    }
    if(this->n_elems!=v.n_elems){
        return false;
    }
    for(int i=0;i<n_elems;i++){
        if(this->data_ptr[i]!=v.data_ptr[i]){
            return false;
        }
    }
    return true;
}
// != operator overload
bool Vector::operator!=(const Vector &v) const{
    return !(operator==(v));
}

