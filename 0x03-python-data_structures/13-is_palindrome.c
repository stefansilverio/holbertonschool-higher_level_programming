#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 *
 */
char *helper(unsigned int count, unsigned int position, char int_array[], listint_t *curr);
int array_palindrome(int *int_array); /* determined if array returned is palindrome*/

int is_palindrome(listint_t **head)
{
	unsigned int count = 0;
	unsigned int position = 0;
	listint_t *curr = *head;
	int *int_array;

	while (curr->next)
	{
		count++;
		curr = curr->next;
	}

	curr = *head;

	int_array = helper(count, position, int_array, curr);
	return(array_palindrome(*int_array, count));
}

char *helper(unsigned int count, unsigned int position, char int_array[], listint_t *curr)
{
	if (curr->next) /* recursive case */
	{
		count += 1;
		curr = curr->next;
		helper(count, int_array, curr);
	}
	else
	{
		int_array[position] = curr->n;
		position += 1;
	}
	return (int_array);
}

int array_palindrome(int *int_array) /* determined if array returned is palindrome */
{
	int first = 0; /* first position in array */
	int split= count / 2;

	if (int_array[first] != int_array[count])
		return (0);
	else
	{
		while (split--)
		{
			if (int_array[first] == int_array[count])
			{
				count--;
				first++;
			}
			else
				return (0);
		}
	}
	return (1);
}
