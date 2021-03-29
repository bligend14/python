#include<stdio.h>
//#include<stdlib.>
int chebui(a,b,c,d){//a=int struc[0](supply),b=int struc[1](army),c=int struc[2](tech),d=int struc[3](base)
    char A[6];
    if(d==0){
            printf("you must build the base first \n");
        }else{
            printf("supply: %d army: %d tech: %d base: %d",a,b,c,d);
        }
    while(1){
        printf("what do you want to build(supply/army/tech/base)?"); 
        scanf("%s",&A);
        if(A[0]=='s' || A[0]=='S' && A[1]=='u' || A[1]=='U' && A[2]=='p' || A[2]=='P' && A[3]=='p' || A[3]=='P' && A[4]=='l' || A[4]=='L' && A[5]=='y' || A[5]=='Y'){
            if(d==1){
                printf("Supply is built \n");
                a+=1;
            }else{
                printf("base is not yet built \n");
                continue;
            }
        }else if(A[0]=='a' || A[0]=='A' && A[1]=='r' || A[1]=='r' &&A[2]=='m' || A[2]=='m' &&A[3]=='y' || A[3]=='Y'){
            if(d==1){
                printf("Army is built \n");
                b+=1;
            }else{
                printf("base is not yet built \n");
            }
        }else if(A[0]=='t' || A[0]=='T' && A[1]=='e' || A[1]=='E' && A[2]=='c' || A[2]=='C' &&A[3]=='h' || A[3]=='H'){
            if(d==1){
                printf("Tech is built \n");
                c+=1;
            }else{
                printf("base is not yet built \n");
            }
        }else if(A[0]=='b' || A[0]=='B' && A[1]=='a' || A[1]=='A' &&A[2]=='s' || A[2]=='S' &&A[3]=='e' || A[3]=='E'){
                printf("base is built \n");
                d+=1;   
        }else{
            printf("the answer is wrong try again \n");
        }
        printf("supply: %d army: %d tech: %d base: %d \n",a,b,c,d);

    }   
    return 0;
}
int chohui(a,b,c,d){
    char A[6];
    char B[8];
    printf("Choose the building");
    scanf("%s",&A);
    if(A[0]=='s' || A[0]=='S' && A[1]=='u' || A[1]=='U' && A[2]=='p' || A[2]=='P' && A[3]=='p' || A[3]=='P' && A[4]=='l' || A[4]=='L' && A[5]=='y' || A[5]=='Y'){
        printf("There are %d supply(supplies), You can produce %d units",a,a*12);        
    }else if(A[0]=='a' || A[0]=='A' && A[1]=='r' || A[1]=='r' &&A[2]=='m' || A[2]=='m' &&A[3]=='y' || A[3]=='Y'){
        printf("There are %d army(armies), produce units?(produce/pass)",b);
        scanf("%s",&B);
    }else if(A[0]=='t' || A[0]=='T' && A[1]=='e' || A[1]=='E' && A[2]=='c' || A[2]=='C' &&A[3]=='h' || A[3]=='H'){
        printf("There are %d tech(teches), research teches?(research/pass)",c);
    }else if(A[0]=='b' || A[0]=='B' && A[1]=='a' || A[1]=='A' &&A[2]=='s' || A[2]=='S' &&A[3]=='e' || A[3]=='E'){
        printf("There are %d base(bases), use skills?(use/pass)",d);
    }else{
        printf("the answer is wrong try again \n");
    }
    return 0;
}
int main()
{
    int struc[5]={0};
    char ans[4];
    printf("start the game(yes/no)?");
    scanf("%s",&ans);
    if(ans[0]=='y' && ans[1]=='e' && ans[2]=='s'){
        printf("Loading...\n");
    }
    else if(ans[0]=='n' && ans[1]=='o'){
        printf("Good Bye");
    }
    chebui(struc[0],struc[1],struc[2],struc[3]);
    return 0;
}
