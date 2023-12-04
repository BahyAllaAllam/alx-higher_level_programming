#include <Python.h>
/**
 * print_python_list_info - print_python_list_info
 * @p: object
 * Return: void
*/

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	int i, size = PyList_Size(p), allocated = list->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);
	for (i = 0; i < size; ++i)
	{
		PyObject *element = PyList_GetItem(p, i);

		printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
