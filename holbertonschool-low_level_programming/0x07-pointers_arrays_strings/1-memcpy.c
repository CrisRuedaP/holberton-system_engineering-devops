#include "holberton.h"

/**
 * _memcpy - copy memory area.
 * @dest: destiny
 * @src: memory area
 * @n: bytes
 * Return: a pointer to dest.
 */

char *_memcpy(char *dest, char *src, unsigned int n)
{
unsigned int i;

for (i = 0; i < n; i++)
dest[i] = src[i];

return (dest);
}
