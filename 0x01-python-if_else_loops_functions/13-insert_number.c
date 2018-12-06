#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in list
 * @head: address of head pointer
 * @number: data to store in list
 * Return: address or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *curr = *head, *tmp = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (head == NULL)
		return (NULL);
	if (curr == NULL)
	{
		curr = new;
		new->next = NULL;
		return (new);
	}
	if ((curr->next == NULL) && (curr->n > number)) /* 1st beginning case */
	{
		tmp = curr;
		curr = new;
		new->next = tmp;
		return (new);
	}
	while (curr->next)
	{
		if (curr->next->n >= number) /* middle case */
		{
			tmp = curr->next;
			curr->next = new;
			new->next = tmp;
			return (new);
		}
		curr = curr->next;
	}
	curr->next = new;
	new->next = NULL;
	return (new);
}
