#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print_python_bytes
 * @p: p
 * Return: void
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *buffer;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	buffer = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", buffer);
	printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
	for (i = 0; i < size + 1 && i < 10; ++i)
	{
		printf("%02x", (unsigned char)buffer[i]);
		if (i < size && i + 1 < 10)
			printf(" ");
	}
	printf("\n");
}
/**
 * print_python_list - print_python_list
 * @p: p
 * Return: Void
*/
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, i;
	PyObject *element;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; ++i)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
		if (strcmp(Py_TYPE(element)->tp_name, "bytes") == 0)
			print_python_bytes(element);
	}
}
