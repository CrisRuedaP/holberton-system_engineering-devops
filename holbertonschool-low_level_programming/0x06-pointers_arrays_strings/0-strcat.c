#include "holberton.h"

/**
 * _strcat - concatenate two strings
 * @dest: string
 * @src: string
 * Return: resulting string dest.
 */

char *_strcat(char *dest, char *src)
{
int i, j;

i = 0;
while (dest[i] != '\0')
{
i++;
}

j = 0;
while (src[j] != '\0')
{
dest[i++] = src[j];
src++;
}

dest[i] = '\0';
return (dest);
}
