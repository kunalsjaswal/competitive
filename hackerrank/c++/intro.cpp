#include <iostream>
#include <sstream>
using namespace std;

// intro Q1
class forloop{
    public: 
    int a;
    int b;
    void method1(){
    cin>>a;
    cin>>b;
        
    for (int i=a; i<=b; i++) {
        if(i<=9){
            switch (i) {
            case 1:
            cout<<"one\n";
            break;
            case 2:
            cout<<"two\n";
            break;
            case 3:
            cout<<"three\n";
            break;
            case 4:
            cout<<"four\n";
            break;
            case 5:
            cout<<"five\n";
            break;
            case 6:
            cout<<"six\n";
            break;
            case 7:
            cout<<"seven\n";
            break;
            case 8:
            cout<<"eight\n";
            break;
            case 9:
            cout<<"nine\n";
            break;
            }
        }
        else{
            if(i%2==0){
                cout<<"even\n";
            }
            else {
                cout<<"odd\n";
            }
        }
    
      }
    }
};

// Q2: max of 4 

int max_of_four(int a,int b,int c,int d){
    if(a>b){
        if(a>c){
            if(a>d){
                return a;
            }
            else{
                return d;
            }
        }
        else{
            if(c>d){
                return c;
            }
            else{
                return d;
            }
        }
    }
    else{
        
        if(b>c){
            if(b>d){
                return b;
            }
            else{
                return d;
            }
        }
        else{
            if(c>d){
                return c;
            }
            else{
                return d;
            }

        }
    }
}

// Q3 pointers 
void update(int *a,int *b) {
    int temp=*a;
    *a=*a + *b;
    *b=abs(temp-*b);
       
}





int main() {

/*
// Q1
    // forloop Q1;
    // Q1.method1();

// Q2
    int a, b, c, d;
    cin>>a>>b>>c>>d;
    int ans = max_of_four(a, b, c, d);
    cout<<ans;

//Q3
    int a, b;
    int *pa = &a, *pb = &b;
    cin>>a>>b;
    update(pa, pb);

    cout<<a<<"\n"<<b;
    return 0;

//Q4 arrays

int size;
cin>>size;
int arrs[size];
for (int i = 0; i < size; i++)
{
    cin>>arrs[i];
}
for (int i = size-1; i >=0; i--)
{

    cout<<arrs[i]<<" ";
}
*/

string inp;
cin>>inp;
stringstream ss(inp);
string a,b,c;
char ch;
ss>>a>>ch>>b>>ch>>c;
cout<<a;





}
