#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int size;
	int *arr;
	srand(time(0));

	printf("Enter the size of the array: \n");
	scanf("%d", &size);
	getchar();

	arr = (int *)malloc(sizeof(int) * size);

	for (int i = 0; i <= size; i++)
	{
		arr[i] = (rand() % 2001) - 1000;
		printf("%d ", arr[i]);
	}

	for (int i = 0; i < size; i++)
	{
		for (int j = 0; j < size - i; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				int copy = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = copy;
			}
		}
	}

	printf("\n");

	for (int i = 0; i <= size; i++)
	{
		printf("%d ", arr[i]);
	}

	getchar();
	return 0;
}
