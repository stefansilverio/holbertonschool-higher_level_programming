#include "lists.h"

/**
 * check_cycle - check for cycle in linked list
 * @list: pointer to head of list
 * Return: cycle status
 */
int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	while (list->next > list)
	{
		if (list == NULL)
			return (0);
		list = list->next;
	}
	return (1);
}
