// fizzbuzz.c

#include <stdio.h>
#include <stdlib.h>

int len(int num){
    int len = 0;
    do{ 
        num /= 10;
        len++;
    }while(num != 0);
    return len;
}
int is_in(int n, int num){
  int* num_splited;
  num_splited = malloc(sizeof(int)*len(num));
  int i;
  int aux = num;
  for (i=len(num)-1;i>=0; i--){
      num_splited[i]=aux%10;
      aux /= 10;
  } 
  //~ printf("\nlen of num is: %d", len(num));
  //~ printf("\n num splited = ");
  //~ for (i=0; i<len(num); i++){
    //~ printf(" %d ", num_splited[i]);
  //~ }
  for (i=0; i<len(num); i++){
    if (n == num_splited[i]) return 1;
  }
  
  return 0;
}
    
void fizzbuzz(int num){
  int i;
  
  for (i=1; i<=num; i++){
      int ok = 0;
      if (i%3==0 || is_in(3,i)){
          printf("Fizz");
          ok=1;
      }
      if(i%5==0 || is_in(5,i)){
          printf("Buzz");
          ok=1;
      }
      if ( !ok) {
            printf("%d", i);
      }
      printf("\n");
    }
}
int main(int argc, char **argv){
   if (argc < 2) {
       printf("\nshould pass a number as argument\n\n");
       return -1;
   }
   
   int num = atoi(argv[1]);
   printf("\nthe number is: %d \n", num);
   
   fizzbuzz(num);
    //printf("is in: %d", is_in(3,13));
   return 0;
}
