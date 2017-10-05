#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define MAXSIZE 100
#define ITERATIONS 100

int buffer[MAXSIZE]; // buffer
int nextp, nextc; // temporary storage
int count=0;

pthread_mutex_t mutex=PTHREAD_MUTEX_INITIALIZER;

void printfunction(void * ptr)
{
	int count = *(int *) ptr;

	if (count==0) 
	{
		printf("All items produced are consumed by the consumer \n");
	}
	else
	{
		for (int i=0; i<=count; i=i+1)
		{
			printf("%d, \t",buffer[i]);
		}
		printf("\n");
	}
}

void *producer(void *ptr) 
{
	int item, flag=0;
	int in = *(int *) ptr;

	do
	{
		item = (rand()%7)%10;
		flag=flag+1;
		nextp=item;
		buffer[in]=nextp;
		in=((in+1)%MAXSIZE);
		while(count <= MAXSIZE)
		{
			pthread_mutex_lock(&mutex);
			count=count+1;
			pthread_mutex_unlock(&mutex);
			printf("Count = %d in produced at Iteration = %d\n", count, flag);
		}
	} while (flag<=ITERATIONS);
	pthread_exit(NULL);
}

void *consumer(void *ptr) 
{
	int item, flag=ITERATIONS;
	int out = *(int *) ptr;

	do
	{
		while (count >0)
		{
			nextc = buffer[out];
			out=(out+1)%MAXSIZE;
			printf("\t\tCount = %d in consumer at Iteration = %d\n", count,flag);
			pthread_mutex_lock(&mutex);
			count = count-1;
			pthread_mutex_unlock(&mutex);
			flag=flag-1;
		}
		if (count <= 0)
		{
			printf("consumer made to wait...faster than producer.\n");
		}
	}while (flag>=0);
	pthread_exit(NULL);
}

int main(void) 
{

	int in=0, out=0; //pointers
	pthread_t pro, con;

	// Spawn threads

	pthread_create(&pro, NULL, producer, &count);
	pthread_create(&con, NULL, consumer, &count);

	/*if (rc1) 
	{
		printf("ERROR; return code from pthread_create() is %d\n", rc1);
		exit(-1);
	}
	if (rc2) 
	{
		printf("ERROR; return code from pthread_create() is %d\n", rc2);
		exit(-1);
	}*/

	// Wait for the threads to finish
	// Otherwise main might run to the end
	// and kill the entire process when it exits.

	pthread_join(pro, NULL);
	pthread_join(con, NULL);
	printfunction(&count);
}

