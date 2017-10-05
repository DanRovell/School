#include <stdio.h>
#define NUM_LOOPS 500000

long long sum = 0;

void counting_function(void *ptr)
{
	int offset =*(int *) ptr;
	for(int i=0; i<NUM_LOOPS; i++)
	{
		sum=sum+offset;
	}
}

int main(void)
{
	int offset1 = 100;
	counting_function(&offset1);
	printf("Sum = %lld\n", sum);
	return 0;
}
