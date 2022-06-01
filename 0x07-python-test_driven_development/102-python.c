#include <Python.h>
#include <stdio.h>
#include <unicodeobject.h>

/**
 * print_python_string - Prints info of a python unicode object
 * @p: Python Unicode Object
 */
void	print_python_string(PyObject *p)
{
	PyObject *obj;

	setbuf(stdout, NULL);
	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	printf("type: ");
	printf("length: %lu\n", PyUnicode_GET_LENGTH(p));
	printf("value: ");
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("compact ascii\n");
	else
		printf("compact unicode\n");
	printf("value: %ls\n", PyUnicode_AsUnicode(p));
}
