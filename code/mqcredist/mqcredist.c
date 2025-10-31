#include <Python.h>
/* This does nothing. Here to trigger building binary wheels. */

/* Module initialization */
static PyMethodDef module_methods[] = {
    {NULL}  /* Sentinel */
};

PyMODINIT_FUNC PyInit_mqcredist(void)
{
    static struct PyModuleDef moduledef = {
        PyModuleDef_HEAD_INIT, "mqcredist", "Noop module", -1, module_methods,
    };
    return PyModule_Create(&moduledef);
}
