#include <bits/stdc++.h>

using namespace std;

int main(){
    long long n1,n2;
    long long p;
    while(cin>>n1>>n2){
        p=n1;
        while(1){
            if(p>=n2){
                cout<<p<<endl;
                break;
            }
            n2-=p;
            p+=1;
        }
    }
}