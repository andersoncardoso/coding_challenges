//      Hoppity facebook puzzle in C


#include <stdio.h>

int main(int argc, char **argv)
{
	if (argc < 2){
        printf("Ops! need a file name argument \n\n");
        return -1;
    }
    
    FILE *f;
    char line[80];
    int num;
    
    f = fopen(argv[1], "r");
    fgets(line, 80, f);
    printf("\n%s \n\n", line);
    num =  atoi(line);
    
    int i ;
    for (i = 1; i<=num ; i++){
        if (i % 3 == 0 && i % 5 == 0)
            printf("Hop\n");
        else if (i % 5 == 0)
            printf("HopHop\n");
        else if (i % 3 == 0)
            printf("Hoppity\n"); 
    }
    
    
	return 0;
}

