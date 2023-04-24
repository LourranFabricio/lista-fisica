#include <stdio.h>

int main(){
    int base =  1;
    int num = 0;
    scanf('%d', &x);
    for(int i = 0; i < x; i++){
        if(i == 1){
            num = 1/base;
        }
        else if(i % 2 != 0 && i != 1){
            base += 2;
            num += 1/base;

        }
    }
    return 0;
}