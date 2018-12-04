#include "lists.h"

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	while (list)
	{
		if (list->next > list)
			return (1);
		else
			list = list->next;
	}
	return (0);
}
