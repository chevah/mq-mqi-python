import os
from setuptools import setup, Extension

#
# This only supports Windows X64 and Linux GLIBC X64.
#

# Used to distribute the IBM MQ shared libraries with the wheel.
data_files = []
mq_file_path = os.environ.get('MQ_FILE_PATH', '')

# To help do some testing on Linux:
# $ TARGET_OS_NAME=nt python -m build --wheel code/mqcredist
target_os = os.environ.get('TARGET_OS_NAME', os.name).lower()

if target_os == 'nt':
    data_files = [
        ('ibm-mq/', [
            mq_file_path + '/bin64/mqe.dll',
            mq_file_path + '/bin64/mqm.dll',
            ]),
        ('ibm-mq/conv', [
            mq_file_path + '/conv/ccsid.tbl',
            mq_file_path + '/conv/ccsid_part2.tbl',
            ]),
        ('ibm-mq/bin64', [
            mq_file_path + '/bin64/libcurl.dll',
            ]),
        ('ibm-mq/gskit8/lib64/', [
            mq_file_path + '/gskit8/lib64/capicmd_res.dll',
            mq_file_path + '/gskit8/lib64/gsk8acmeidup_64.dll',
            mq_file_path + '/gskit8/lib64/gsk8cms_64.dll',
            mq_file_path + '/gskit8/lib64/gsk8dbfl_64.dll',
            mq_file_path + '/gskit8/lib64/gsk8iccs_64.dll',
            mq_file_path + '/gskit8/lib64/gsk8kicc_64.dll',
            mq_file_path + '/gskit8/lib64/gsk8km_64.dll',
            mq_file_path + '/gskit8/lib64/gsk8p11_64.dll',
            mq_file_path + '/gskit8/lib64/gsk8ssl_64.dll',
            mq_file_path + '/gskit8/lib64/gsk8sys_64.dll',
            mq_file_path + '/gskit8/lib64/gsk8valn_64.dll',
            # VC++ 2015 runtime dependencies.
            'c:/windows/system32/vcruntime140.dll',
            ]),
        ('ibm-mq/gskit8/lib64/N/icc/icclib', [
            mq_file_path + '/gskit8/lib64/N/icc/icclib/ICCSIG.txt',
            mq_file_path + '/gskit8/lib64/N/icc/icclib/icclib085.dll',
            ]),
    ]
else:
    data_files = [
        ('lib/ibm-mq/lib', [
            mq_file_path + '/lib/ccsid.tbl',
            mq_file_path + '/lib/ccdt_schema.json',
            mq_file_path + '/lib/ccsid_part2.tbl',
            ]),
        ('lib/ibm-mq/lib64', [
            mq_file_path + '/lib64/libmqe_r.so',
            mq_file_path + '/lib64/libmqm_r.so',
            mq_file_path + '/lib64/libcurl.so',
            ]),
        ('lib/ibm-mq/gskit9/lib64', [
            mq_file_path + '/gskit9/lib64/libgsk9acmeidup_64.so',
            mq_file_path + '/gskit9/lib64/libgsk9cms_64.so',  # curl
            mq_file_path + '/gskit9/lib64/libgsk9dbfl_64.so',
            mq_file_path + '/gskit9/lib64/libgsk9drld_64.so',
            mq_file_path + '/gskit9/lib64/libgsk9kicc_64.so',
            mq_file_path + '/gskit9/lib64/libgsk9km_64.so',
            mq_file_path + '/gskit9/lib64/libgsk9p11_64.so',
            mq_file_path + '/gskit9/lib64/libgsk9ssl_64.so',  # curl
            mq_file_path + '/gskit9/lib64/libgsk9valn_64.so',
            mq_file_path + '/gskit9/lib64/libickcs_64.so',
            ]),
        ('lib/ibm-mq/gskit9/lib64/N/icc/icclib', [
            mq_file_path + '/gskit9/lib64/N/icc/icclib/ICCSIG.txt',
            mq_file_path + '/gskit9/lib64/N/icc/icclib/libicclib085.so',  # curl
            ]),
    ]

if not mq_file_path and os.environ.get('CI', '') == '':
    raise Exception(
        "Use the MQ_FILE_PATH environment variable to identify "
        "the path where IBM MQ C redistributables are located.")

if not mq_file_path:
    # We are in the CI environment, so just build a noop package.
    setup()
else:
    setup(
        data_files=data_files,
        ext_modules=[Extension(
            "mqcredist",
            sources=["mqcredist.c"],
            define_macros=[("Py_LIMITED_API", "0x03090000")],
            py_limited_api=True,
        )],
        options={"bdist_wheel": {"py_limited_api": "cp39"}},
    )
