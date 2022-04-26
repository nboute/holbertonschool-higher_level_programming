#include "lists.h"

/**
 * insert_node - Inserts node in a sorted list
 * @head: Head of linked list
 * @number: Value to insert into list
 * Return: Pointer to new node
 */
listint_t	*insert_node(listint_t **head, int number)
{
	listint_t	*ptr, *new;

	if (!head)
		return (NULL);
	new = malloc(sizeof(*new));
	if (!new)
		return (NULL);
	new->n = number;
	if (!*head || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	ptr = *head;
	while (ptr->next && ptr->next->n < number)
		ptr = ptr->next;
	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
