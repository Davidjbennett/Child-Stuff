#ifndef VECTOR_H
#define VECTOR_H

#include <iostream>
#include <cstddef>
#include <stdexcept>
using std::size_t;
using std::range_error;

template<typename T>
class Vector {
    enum {CHUNK = 10};
    T* data_ptr;      // Pointer to the heap array
    size_t capacity;    // Size of the current array allocation (total number of ints, in use or not)
    size_t n_elems;     // Number of int spaces currently in use, starting from position 0
    void grow(){
        this->capacity = ((this->capacity*16)/10);
        T* temp = new T[this->capacity];
        for (int x =0; x < this->n_elems; x++){
            temp[x] = data_ptr[x];
        }
        delete[] this->data_ptr;
        this->data_ptr = temp;
    };
public:
    // Object Mgt.
    Vector(){
        data_ptr = new T[CHUNK];
        capacity = CHUNK;
        n_elems = 0;
    };

    // Copy constructor
    Vector(const Vector& v){
        this->capacity = v.capacity;
        this->data_ptr = new T[this->capacity];
        this->n_elems = v.n_elems;
        for(int i = 0;i<v.n_elems;i++){
            this->data_ptr[i] = v.at(i);
        }
    };

    // Copy assignment operator
    Vector& operator=(const Vector& v){
        this->capacity = v.capacity;
        this->data_ptr = new T[this->capacity];
        this->n_elems = v.n_elems;
        for(int i = 0;i<v.n_elems;i++){
            this->data_ptr[i] = v.at(i);
        }
        return (*this);
    }; 

    ~Vector(){
        delete[] data_ptr;
    };

    // Accessors
    // Return the int in position 0, if any
    T front() const{
        if (this-> n_elems == 0){
            throw range_error("out of bounds");
        }else {
            return this->data_ptr[0];
        }
    };

    // Return last element (position n_elems-1)                  
    T back() const{
        if (this->n_elems == 0){
            throw range_error("out of bounds");
        }else{
            return this->data_ptr[n_elems-1];
        }
    };  

    // Return element in position "pos" (0-based)                 
    T at(size_t pos) const{
        if (this->n_elems == 0){
            throw range_error("out of bounds");
        }else if (pos <= 0 && pos >= this->n_elems){
            throw range_error("out of bounds");
        }else{
            return this->data_ptr[pos];
        }
        
    };

    // Return n_elems
    size_t size() const{
        return (size_t)this->n_elems;
    };

    // Return n_elems == 0                
    T empty() const{
        return this->n_elems == 0;
    };                 

    // Mutators
    // Same as at but no bounds checking
    T& operator[](size_t pos){
        return this->data_ptr[pos];
    };

    // Append a new element at the end of the array        
    void push_back(T item){
        if (this->n_elems < this->capacity){
            this->data_ptr[n_elems++] = item;
        }else{
            this->capacity = ((this->capacity*16)/10);
            T* temp = new T[this->capacity];
            for (int x =0; x < this->n_elems; x++){
                temp[x] = data_ptr[x];
            }
            delete[] this->data_ptr;
            this->data_ptr = temp;
            this->data_ptr[n_elems] = item;
            n_elems++;
        }
    }; 

    // --n_elems (nothing else to do; returns nothing)          
    void pop_back(){
        if(n_elems==0){
            throw range_error("Out of bound");
        }else{
            n_elems--;
        }
    };  

    // Remove item in position pos and shuffles following items left                  
    void erase(size_t pos){
        if (pos < this->n_elems){
            for(int x = pos; x < this->n_elems; x++){
                data_ptr[x] = data_ptr[x+1];
            }
            n_elems--;
        }else{
            throw range_error("out of bounds");
        }
    }; 

    // Shuffle items right to make room for a new element            
    void insert(size_t pos, T item){ 
        if(capacity==n_elems){
            capacity = (capacity*16)/10;
            T* temp_ptr = new T[capacity];
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
    };

    // n_elems = 0 (nothing else to do; keep the current capacity)  
    void clear(){
        delete[] data_ptr;
        data_ptr = new T[CHUNK];
        capacity = CHUNK;
        n_elems = 0;
    };                       

    // Iterators
    T* begin(){
        if(n_elems==0)return NULL;
        return &data_ptr[0];
    };                       // Return a pointer to 1st element, or nullptr if n_elems == 0
    T* end(){
        if(n_elems==0)return NULL;
        return &data_ptr[n_elems];
    };                         // Return a pointer to 1 past last element, or nullptr if n_elems == 0

    // Comparators
    bool operator==(const Vector& v) const{
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
    };
    bool operator!=(const Vector& v) const{
        return !(operator==(v));
    };
};

#endif