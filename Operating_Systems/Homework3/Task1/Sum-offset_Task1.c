#include <stdio.h>
#define NUM_LOOPS 500000

long long sum = 0;

void counting_function(int offset)
{
	for(int i=0; i<NUM_LOOPS; i++)
	{
		sum=sum+offset;
	}
}

int main(void)
{
	counting_function(1);
	printf("Sum = %lld\n", sum);
	return 0;
}
