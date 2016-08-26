/*

Clock Tick counter for sum and sub instructions
Author Dario Clavijo 2016
GPLv3

*/

#include <time.h>

void test_clock(){
	clock_t start, end;
	int cpu_time_used;

	start = clock();
	/* Do the work. */

	end = clock();
	cpu_time_used = ((double) (end - start));
	
	printf("Clocks: %d\n",cpu_time_used);
}

#define STEP 65535
#define MAX_ITER CLOCKS_PER_SEC * 1000

int test_sum(){
        clock_t start, end;
        int cpu_time_used;

	unsigned int j=0;
        start = clock();
        /* Do the work. */

	for(int i=0;i<=MAX_ITER;i++){
		j+=STEP;
	}
        end = clock();
        cpu_time_used = ((double) (end - start));

        printf("sum clocks: %d\n",cpu_time_used);

	return cpu_time_used;
}

int test_sub(){
        clock_t start, end;
        int cpu_time_used;

	unsigned int j=MAX_ITER;
        start = clock();
        /* Do the work. */

	for(int i=0;i<=MAX_ITER;i++){
		j-=STEP;
	}
        end = clock();
        cpu_time_used = ((double) (end - start));

        printf("sub clocks: %d\n",cpu_time_used);

	return cpu_time_used;

}


int main(){
	printf("clocks per sec: %d\n",CLOCKS_PER_SEC);
	printf("Max Iterations: %d\n",MAX_ITER);
	printf("step: %d\n",STEP);

	int t1 = test_sum();
	int t2 = test_sub();
	printf("diff: %d\n",(t1-t2));
}
