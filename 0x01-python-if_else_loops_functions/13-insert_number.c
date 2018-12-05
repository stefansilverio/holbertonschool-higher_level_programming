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
	listint_t *new = NULL;
	listint_t *slow = NULL;
	listint_t *fast = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = new;
		new->n = number;
		new->next = NULL;
		return (new);
	}
	slow = fast = *head;
	fast = slow->next;
	while (slow)
	{
		if (fast == NULL)
		{
			if (slow->n < number) /* check where new node must be inserted */
			{
				slow->next = new;
				new->n = number;
				new->next = NULL;
				return (new);
			}
			else
			{
				slow = new;
				new->n = number;
				new->next = fast;
				return (new);
			}
		}
		if (fast->n > number)
		{
			slow->next = new;
			new->next = fast;
			new->n = number;
			return (new);
		}
		else
			fast = slow = slow->next;
	}
	return (new);
}
