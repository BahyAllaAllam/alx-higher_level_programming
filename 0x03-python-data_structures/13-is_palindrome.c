#include "lists.h"
/**
 * reverseList - reverseList
 * @head: head
 * Return: listint_t
*/
listint_t* reverseList(listint_t* head)
{
	listint_t *prev = NULL, *curr = head, *next = NULL;
	while (curr != NULL) 
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return prev;
}

/**
 * is_palindrome - is_palindrome
 * @head: head
 * Return: int
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev_slow = *head;
	listint_t *second_half, *mid = NULL;
	int isPalindrome = 1;
	
	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		
		if (fast != NULL)
		{
			mid = slow;
			slow = slow->next;
		}
		
		second_half = slow;
		prev_slow->next = NULL;
		second_half = reverseList(second_half);

		while (*head != NULL && second_half != NULL)
		{
			if ((*head)->n != second_half->n)
			{
				isPalindrome = 0;
				break;
			}
			*head = (*head)->next;
			second_half = second_half->next;
		}
		second_half = reverseList(second_half);
		if (mid != NULL)
		{
			prev_slow->next = mid;
			mid->next = second_half;
		}
		else
			prev_slow->next = second_half;
	}

	return isPalindrome;
}
