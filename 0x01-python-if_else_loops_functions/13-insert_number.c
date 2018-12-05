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
	new->n = number;
	if (head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	slow = fast = *head;
	fast = slow->next;
	if (slow->n > number)
	{
		slow = new;
		new->next = fast;
		return (new);
	}
	while (slow)
	{
		if (fast->n >= number)
		{
			slow->next = new;
			new->next = fast;
			return (new);
		}
		fast = slow = slow->next;
	}
	return (new);
}
