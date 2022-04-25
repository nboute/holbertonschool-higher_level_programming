#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: Pointer to linked list
 * Return: 1 if it has a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t	*slow, *fast = NULL;

	slow = list;
	if (list && list->next)
		fast = list->next->next;
	while (slow && fast)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next;
		if (fast)
			fast = fast->next;
	}
	return (0);
}
