#include <stdio.h>
#include <stdbool.h>
 
int main() 
{
    int allocation[5][5];						//initializing all arrays and matrices
    int max[5][5];
    int available[5];//(work)
    int resourcesUsed[5] = {0, 0, 0, 0, 0};
    int maxResources[5];
    int running[5];
	int need[5][5];
 
    int i, j, exec, r, p;						//variables that I fill be using
    int count = 0;
    bool finish = false;
 
    printf("\nEnter the number of resources: ");//asks for number of resources
    scanf("%d", &r);
 
    printf("\nEnter the number of processes: ");//asks for number of processes
    scanf("%d", &p);

    for (i = 0; i < p; i++) 
	{
        running[i] = 1;							//running is given a 1(aka true) to all spots
        count++;								//count is the number of resources
    }
 
    printf("\nEnter maximum for each resource: ");// this is the max number of each resource, i.e. first is 10,
	for (i = 0; i < r; i++)						  // second is 5, third is 7, etc..
	{
        scanf("%d", &maxResources[i]);
	}
 
    printf("\nEnter Allocation matrix: ");// user enter the Allocation matrix
    for (i = 0; i < p; i++) 
	{
        for (j = 0; j < r; j++)
		{
            scanf("%d", &allocation[i][j]);
		}
    }
 
    printf("\nEnter Max matrix: ");//user enter the Max matrix
    for (i = 0; i < p; i++) 
	{
        for (j = 0; j < r; j++)
		{
            scanf("%d", &max[i][j]);
		}
    }
 
    printf("\nThe maximum for each resource: ");//prints the maximun for each resource the user entered earlier
    for (i = 0; i < r; i++)
	{
        printf("%d ", maxResources[i]);
 	}

    printf("\nThe Allocation matrix:\n");//prints the allocation matrix that the user entered earlier
    for (i = 0; i < p; i++) 
	{
        for (j = 0; j < r; j++)
		{
            printf("\t%d", allocation[i][j]);
		}
        printf("\n");
    }
 
    printf("\nThe Max matrix:\n");//prints the max matrix that the user entered earlier
    for (i = 0; i < p; i++) 
	{
        for (j = 0; j < r; j++)
		{
            printf("\t%d", max[i][j]);
		}
        printf("\n");
    }
 	
	printf("\nThe Need matrix:\n");
    for (i = 0; i < p; i++) 		//creates the need matrix by subtracting the allocation matrix from the max
	{
        for (j = 0; j < r; j++)
		{
            need[i][j] = max[i][j] - allocation[i][j];
		}
    }
    for (i = 0; i < p; i++) 		//prints the need matrix
	{
        for (j = 0; j < r; j++)
		{
            printf("\t%d", need[i][j]);
		}
        printf("\n");
    }

    for (i = 0; i < p; i++)	//find the total of each resource in allocation matrix
	{
        for (j = 0; j < r; j++)
		{
            resourcesUsed[j] += allocation[i][j];
		}
 	}

    printf("\nTotal of each resource allocated: ");
    for (i = 0; i < r; i++)		//print the total of each resource in allocation matrix
	{
        printf("%d ", resourcesUsed[i]);
	}
	printf("\n");
    for (i = 0; i < r; i++)
	{
        available[i] = maxResources[i] - resourcesUsed[i];//finds the available resources
	}
 
    printf("\nAvailable resources: ");	//prints the available(work) resources array
    for (i = 0; i < r; i++)	
	{
        printf("%d ", available[i]);
	}
    printf("\n");
	
 	int safeSequence[p];//safe sequence array
    while (count != 0) //start of loop
	{
		int x = 0;
        finish = false;	//finish variable set to false
        for (i = 0; i < p; i++) //loop to go through process requests
		{
			
            if (running[i]) //if running at the ith spot is true(1)
			{
                exec = 1;//set to 1 to say "is executing"
                for (j = 0; j < r; j++) 
				{
                    if (need[i][j] > available[j]) //if need is greater than available
					{
						printf("Process %d is not executing.\n", i + 1);//the process will not execute
                        exec = 0;//set to 0 to say not executing
                        break;
                    }
                }
 				
                if (exec) //executing the process that meets available requirements
				{
					safeSequence[x] = i+1;
                    printf("Process %d is executing.\n", i + 1); //print that process executes
					printf("SafeSequence:%d \n", safeSequence[x] );//printing numbers in order that is safe
                    running[i] = 0;//running at spot is set to false(0), process executed
                    count--;//decrement, 1 process done
                    finish = true;// finished
                    for (j = 0; j < r; j++)//add allocated resources to available(work)
					{
                        available[j] += allocation[i][j];
					}
					x++;
                    break;	
                }		
            }
        }
 
        if (!finish) 
		{
            printf("\nThe processes did not finish.");
            break;
        }
        if (finish)
		{
            printf("The process finished.\n");
		}
        printf("\nAvailable resources: ");//print new available(work) resources
        for (i = 0; i < r; i++)
		{
            printf("%d ", available[i]);	
		}
		printf("\n");
    }
	printf("\n");
    return 0;
}


