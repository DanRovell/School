#include <stdio.h>
#include <pthread.h>
#define NUM_LOOPS 500000

long long sum = 0;

void* counting_function(void *ptr)
{
	int offset =*(int *) ptr;
	for(int i=0; i<NUM_LOOPS; i++)
	{
		sum=sum+offset;
	}
	pthread_exit(NULL);
}

int main(void)
{
	int offset1 = 100;
	pthread_t id1;

	pthread_create(&id1, NULL, counting_function, &offset1);

	pthread_join(id1, NULL);	

	printf("Sum = %lld\n", sum);
	return 0;
}
