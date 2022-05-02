#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a python list
 * @p: Python list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject	*plist;
	PyObject		*item;
	long	i, size;

	if (!PyList_Check(p))
		return;
	size = PyList_Size(p);
	plist = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", plist->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
