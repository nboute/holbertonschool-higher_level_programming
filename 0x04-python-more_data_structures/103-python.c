#include "Python.h"
#include <stdio.h>

/**
 * print_python_list - Prints information about a python list
 * @p: Python list
 */
void print_python_list(PyObject *p)
{
	PyListObject	*plist;
	PyObject		*item;
	long	i, size;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
		return;
	plist = (PyListObject *)p;
	size = PyList_GET_SIZE(plist);
	printf("[*] Size of the Python List = %ld\n",
		((PyVarObject *)plist)->ob_size);
	printf("[*] Allocated = %ld\n", plist->allocated);
	for (i = 0; i < size; i++)
	{
		item = plist->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}


/**
 * print_python_bytes - Prints bytes of a python bytes object
 * @p: Python bytes object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject	*bytes;
	long	i, size;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;
	size = ((PyVarObject *)bytes)->ob_size;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);
	printf("  first %ld bytes:", size + 1 > 10 ? 10 : size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" ");
		printf("%2.2x", (char)(bytes->ob_sval[i]) & 0xFF);
	}
	printf("\n");
}
