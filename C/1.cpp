#include<bits/stdc++.h>
using namespace std;
class Student{
    private:
    int admno;
    char Name[20];
    float marksEng;
    float marksMaths;
    float marksSci;
    float total;
    public:
    void readData(){
        cout<<"Enter the data"<<endl;
        cin>>admno>>Name>>marksEng>>marksMaths>>marksSci;
    }
    void compute(){
        total=marksEng+marksSci+marksMaths;
    }
    void showData(){
        cout<<"Admno:"<<admno<<" Name:"<<Name<<" marksEng:"<<marksEng<<" marksSci:"<<marksSci<<" total:"<<total<<endl;
    }
};

int main(){
    Student st;
    st.readData();
    st.compute();
    st.showData();
    return 0;
}

