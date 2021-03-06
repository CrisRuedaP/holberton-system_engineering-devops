#ifndef DOG_H_
#define DOG_H_
/**
 * struct dog - struct dog.
 * @name: dog name
 * @age: dog age
 * @owner: dog owner
 * Return: always 0.
 */
struct dog
{
char *name;
float age;
char *owner;

};

typedef struct dog dog_t;
void free_dog(dog_t *d);
dog_t *new_dog(char *name, float age, char *owner);
void print_dog(struct dog *d);
int _putchar(char c);
void print_dog(struct dog *d);
void init_dog(struct dog *d, char *name, float age, char *owner);
#endif
