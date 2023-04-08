#include<stdio.h> 

int main()
{
    int num,i,f,end;
    printf("Enter an Integer : ");
    scanf("%d",&num);
    

    f=1;
    end=num/2;
    for(i=2;i<=end;i++)
    {
        if(num%i==0)
        {
          f=0;
          break;
        }
            
    }

    if(f==1)
        printf("%d is a Prime Number.",num);
    else
        printf("%d isn't a Prime Number.",num);

        return 0;
}