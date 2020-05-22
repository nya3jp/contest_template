package(default_visibility=["//sum:__subpackages__"])

py_binary(
    name = "python",
    srcs = ["python.py"],
    srcs_version = "PY3",
)

solution_test(
    name = "python_test",
    solution = ":python",
    judge = "//sum/judge",
)
