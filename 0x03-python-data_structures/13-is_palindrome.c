#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *curr = *head, *start = *head; /* count nodes */

	if ((*head == NULL) || (*head)->next == NULL)
		return (1);

	return(helper(curr, &start));
}

int helper(listint_t *curr, listint_t **start)
{
	if (curr->next) /* recursive case */
	{
		if (!helper(curr->next, start))
			return (0);
		printf("1: here:%d\n", curr->n);
		printf("1: there:%d\n", (*start)->n);
		if (curr->n != (*start)->n)
			return (0);
		*start = (*start)->next;
	}
	else
	{
		printf("2:here:%d\n", curr->n);
		printf("2:there%d\n", (*start)->n);
		if ((*start)->n != curr->n)
			return (0);
		*start = (*start)->next;
		return (1);
	}
	return (1);
}
