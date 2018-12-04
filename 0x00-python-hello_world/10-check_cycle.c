#include "lists.h"

/**
 * check_cycle - check for cycle
 * @list: pointer to head of list
 * Return: cycle status
 */
int check_cycle(listint_t *list)
{
	listint_t *curr = list;
	listint_t *next = list;

	if (list == NULL)
		return (0);
	while (1)
	{
		curr = curr->next;
		if (next->next != NULL)
			next = next->next->next;
		else
			return (0);
		if (curr == NULL || next == NULL)
			return (0);
		if (curr == next)
			return (1);
	}
	return (0);
}
