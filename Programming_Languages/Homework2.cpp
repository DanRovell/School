/*
Author: Daniel Rovell
CSC 330
Homework 2
This code uses C++
*/

#include <iostream>

using namespace std;

void Inv1Ex1();//investigation 1 Example 1
void Inv1Ex2();//investigation 1 Example 2
void Inv2();//Investigation 2
void Inv2Value(struct Array);
void Inv2Reference(int arr[]);
void Inv3();//Investigation 3

//Investigation 1##################################################################
//Example 1------------------------------------------------------------------------
void Inv1Ex1()
{
    int x = 1;
    {
        int x = 2;
        {
            int x = 3;
            {
                x = 4;
                cout << "X = " << x << endl;
                for (int i = 0; i <= 10; i++)
                {
                    int x = i;
                }
                cout << "X = " << x << endl;
            }
            cout << "X = " << x << endl;
        }
        cout << "X = " << x << endl;
    }
    cout << "X = " << x << endl;
}

/*
Output:
X = 4
X = 4
X = 4
X = 2
X = 1

The 4 persisted until it exited the block containing the block it was assigned in.
The for loop had no effect outside of itself.
*/
//Example 2------------------------------------------------------------------------
void Inv1Ex2()
{
    int x = 1;
    {
        x = 2;
        {
            x = 3;
            {
                x = 4;
                cout << "X = " << x << endl;
                for (int i = 0; i <= 10; i++)
                {
                    x = i;
                }
                cout << "X = " << x << endl;
            }
            cout << "X = " << x << endl;
        }
        cout << "X = " << x << endl;
    }
    cout << "X = " << x << endl;
}

/*
Output:
X = 4
X = 10
X = 10
X = 10
X = 10

The 10 from the loop persisted becasue it was reassigned.
*/
/*
Conclusion:
If a variable is redeclared with the same variable name in a block below the previous
declaration, the variable is only that number in the current block.

Then, if a variable is reassigned to a new number, it is that number until the
code exits that block that contains the block it was reassigned in.

Then, if many new reassignments happen in cascading blocks, the newest change
remains.

If redeclared inside loop, the change does not continue after the loop is finished.
If reassigned inside the loop, the change persists.
*/

//Investigation 2##################################################################

struct Array { int arr[1]; };

void Inv2Value(Array x)
{
    x.arr[0] = 2;
    cout << x.arr[0] << "\tfunction" << endl;
}

void Inv2Reference(int arr[])
{
    arr[0] = 2;
    cout << arr[0] << "\tfunction" << endl;
}

void Inv2()
{
    //by value
    Array x;
    x.arr[0] = 1;
    cout << x.arr[0] << "\tbefore" << endl;
    Inv2Value(x);
    cout << x.arr[0] << "\tafter" << endl;

    cout << "-----------------" << endl;

    //by reference
    int arr[1];
    arr[0] = 1;
    cout << arr[0] << "\tbefore" << endl;
    Inv2Reference(arr);
    cout << arr[0] << "\tafter" << endl;
}
/*
Ouput:
1   before     By value: value before and after function do not change.
2   function
1   after
-------------
1   before     By reference: value stays the value specified in function.
2   function
2   after

The first function demonstrates passing an array by value. You can pass an
array by value by wrapping it in a struct.

The second demonstrates how an array is normally passed by reference.
*/

//Investigation 3##################################################################

void Inv3()
{
    int x = 5;
    for(int i = 0; i < 10; i++)
    {
        for(int j = 0;j < 10; j++)
        {
            cout << j << endl;
            if(x == j)
            {
                cout << "x is equal to j." << endl;
                goto stop;
            }
        }
    }
    stop:
    cout << "Success" << endl;
}
/*
Output:
0
1
2
3
4
5
x is equal to j.
Success

A goto staement is utilized to goto a lable. The label in the above code is stop.
Goto statements are useful for exiting nested loops.
*/

int main()
{
    cout << "Investigation 1: Example 1" << endl;
    Inv1Ex1();
    cout << "Investigation 1: Example 2" << endl;
    Inv1Ex2();
    cout << "Investigation 2:" << endl;
    Inv2();
    cout << "Investigation 3: " << endl;
    Inv3();
}
