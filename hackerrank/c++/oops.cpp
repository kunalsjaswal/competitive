#include <iostream>
using namespace std;

class student1{
    public:
    int age,standard;
    string fname,lname;
    
    void result(){
        cin>>age;
        cin>>fname;
        cin>>lname;
        cin>>standard;

        cout<<age<<" "<<fname<<" "<<lname<<" "<<standard;
    }

};

int main(){
    student1 obj1;
    obj1.result();
}