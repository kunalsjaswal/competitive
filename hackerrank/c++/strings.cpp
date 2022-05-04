#include <iostream>
using namespace std;

// Q1 

void fn1(){
    string a,b;
    cin>>a;
    cin>>b;

    string tempa=b.substr(0,1)+a.substr(1,a.length());
    string tempb=a.substr(0,1)+b.substr(1,b.length());
    
    cout<<a.length()<<" "<<b.length()<<endl;
    cout<<a+b<<endl;
    cout<<tempa<<" "<<tempb;

}


// Q2 string stream 
void fn2(){
    string s;
    cin>>s;
    for (int i = 0; i < s.length(); i++)
    {
        if(s[i]==','){
            cout<<endl;
        }
        else{
            cout<<s[i];
        }
    }
}

int main(){

    fn2();


}