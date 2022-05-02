#include "lists.h"

/**
 * is_palindrome_recurse - Checks if linked list is a palindrome
 * @left: Adress of left pointer
 * @right: right pointer
 * Return: 1 if it is a palindrome, 0 if not
 */
int		is_palindrome_recurse(listint_t **left, listint_t *right)
{
	if (!right)
		return (1);
	if (!is_palindrome_recurse(left, right->next))
		return (0);
	if ((*left)->n != right->n)
		return (0);
	*left = (*left)->next;
	return (1);
}

/**
 * is_palindrome - Checks if linked list is a palindrome
 * @head: Adress of head of linked list
 * Return: 1 if it is a palindrome, 0 if not
 */
int		is_palindrome(listint_t **head)
{
	listint_t	*left;

	if (!head || !*head)
		return (0);
	left = *head;
	return (is_palindrome_recurse(&left, left));
}
