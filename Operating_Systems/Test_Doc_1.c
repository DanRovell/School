#include <stdio.h>
#include <pthread.h>

#define MAXSIZE 100
#define ITERATIONS 1000                                  

int buffer[MAXSIZE];
int count=0;                                     

pthread_mutex_t mutex= PTHREAD_MUTEX_INITIALIZER;  

pthread_cond_t signal_c= PTHREAD_COND_INITIALIZER;

pthread_cond_t signal_p= PTHREAD_COND_INITIALIZER;

void printfunction(void * ptr)
{
	
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

  while (count<MAXSIZE)
  {
    pthread_mutex_lock(&mutex);
    count ++;
    printf("Producer : %d\n", count);
    
    pthread_cond_signal(&signal_c);
    
    if (count != MAXSIZE)
      pthread_cond_wait(&signal_p, &mutex);

    pthread_mutex_unlock(&mutex);

    if (count == MAXSIZE)
    {
      printf("Producer done.. !!\n");
      break;
    }
  }
}

void *consumer(void *ptr)
{
  int printed= 0;
	
	do
	{
  		while (count>0)
  		{	
    			pthread_mutex_lock(&mutex);
    		
    			pthread_cond_signal(&signal_p);
    		
    			pthread_cond_wait(&signal_c, &mutex);
    		
    			printf("Consumer : %d\n", count);
    		
    			pthread_mutex_unlock(&mutex);
		
    			if (count == MAXSIZE)
    			{
    		 		printf("Consumer done.. !!\n");
    		  		break;
    			}
  		}
	}
	while(count>=0);
}

void main()
{
  	count= 0;

	pthread_t pro, con;
	
  	pthread_create(&pro, NULL, producer, &count);
	pthread_create(&con, NULL, consumer, &count);

	pthread_join(pro, NULL);
	pthread_join(con, NULL);
	
	printfunction(&count);
}
