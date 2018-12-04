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
	while ((list->next != NULL) && (list->next < list))
	{
		list = list->next;
	}
	if (list->next > list)
		return (1);

	return (0);
}
