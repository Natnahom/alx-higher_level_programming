#include "lists.h"

/**
 * check_cycle - checks the cycle
 *
 * @list: integer list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	int *node1, *node2;

	if (head == NULL)
		return (0);
	while (head != NULL)
	{
		node1 = (int *)&head;
		node2 = (int *)&head->next;
		if (head->next == NULL)
			return (0);

		if (*node1 - *node2 <= )
			return (1);

		head = head->next;
	}
	return (0);
}
