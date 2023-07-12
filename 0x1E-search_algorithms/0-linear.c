#include "search_algos.h"

/**
* linear_search - a function that searches an array to find a matchindex
* @array: pointer to first element of the array to search in
* @size: the length of the array
* @value: the value to search for
* Return: the index matching the array
*/

int linear_search(int *array, size_t size, int value)
{
	unsigned int i;

	if (array == NULL)
	{
		return (-1);
	}

	for (i = 0; i < size; i++)
	{

		printf("Value checked array[%d] = [%d]\n", i, array[i]);
		if (array[i] == value)
		{
		return (array[i]);
		}
	}
	return (-1);

}
