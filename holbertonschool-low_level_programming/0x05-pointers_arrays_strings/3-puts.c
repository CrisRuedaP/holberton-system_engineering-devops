#include "holberton.h"

/**
 * _puts - prints a string
 *
 * @str: a pointer to string
 *
 * Return: Always 0.
 */
void _puts(char *str)
{
while (*str != '\0')
{
_putchar(*str);
str++;
}
_putchar('\n');
}
