#include "holberton.h"
#include <stdio.h>
/**
 * print_diagsums - sum of two diagonals of integers.
 * @a: array
 * @size: size
 * Return: sum
 */

void print_diagsums(int *a, int size)
{
int i, j, sum = 0;

for (i = 0; i < size; i++)
{
for (j = 0; j < size; j++)
{
if (i == j)
{
sum = sum + a[i][j];
}
printf("%d", sum);
}
}
}
