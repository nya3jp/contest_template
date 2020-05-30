package(default_visibility = ["//sqrt:__subpackages__"])

py_binary(
    name = "python",
    srcs = ["python.py"],
    srcs_version = "PY3",
)

solution_test(
    name = "python_test",
    judge = "//sqrt/judge",
    solution = ":python",
)
