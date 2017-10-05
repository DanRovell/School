#include <stdio.h>
#include <stdbool.h>
 
int main()
{
    int p, r, c, d, processNum;
	int count;
	bool safe = false;
  	printf("Enter the number of Processes and Resources\n");
    scanf("%d%d", &p, &r);
	int max[p][r];
	int allocation[p][r];
	int need[p][r];
	int running[p];
	int max_res[p];
	int alloc[p];
	int available[r];

	for(c = 0; c < p; c++)
	{
		running[c] = 1;
		count++;
	} 

	printf("\nEnter Claim Vector: ");
    for (c = 0; c < r; c++)
	{
        scanf("%d", &max_res[c]);
	}

	printf("Enter the elements of Max matrix\n");
 
	for (c = 0; c < p; c++)
	{
    	for (d = 0 ; d < r; d++)
		{
        	scanf("%d", &max[c][d]);
		}
	}
 
    printf("Enter the elements of Allocation matrix\n");
 
    for (c = 0; c < p; c++)
	{
    	for (d = 0; d < r; d++)
		{
        	scanf("%d", &allocation[c][d]);
		}
	} 	
    
	printf("Need Matrix:\n");
 
    for (c = 0; c < p; c++) 
	{
    	for (d = 0; d < r; d++) 
		{
        	need[c][d] = max[c][d] - allocation[c][d];
        	printf("%d\t",need[c][d]);
     	} 
      	printf("\n");
    }
	
	printf("Total Allocated resources: \n");
	for(c = 0; c < p; c++)
	{
        for (d = 0; d < r; d++)
		{
            alloc[d] += allocation[c][d];
		}
	}
	for (c = 0; c < r; c++)
	{
        printf("%d ", alloc[c]);
	}
	printf("\n");

	printf("Available resources: \n");
	for (c = 0; c < r; c++)
	{
        available[c] = max_res[c] - alloc[c];	
	}
	for (c = 0; c < r; c++)
	{
        printf("%d ", available[c]);
	}
    printf("\n");
	/*
	while(count != 0)
	{
		safe = false;
		for (c = 0; c < p; c++)
		{
			if(running[c])
			{
				processNum = 1;
				
			}
		}
	}
 */
    return 0;
}
