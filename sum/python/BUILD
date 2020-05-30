package(default_visibility = ["//sum:__subpackages__"])

load("@rules_contest//contest:defs.bzl", "solution_test")

py_binary(
    name = "python",
    srcs = ["python.py"],
    srcs_version = "PY3",
)

solution_test(
    name = "python_test",
    judge = "//sum/judge",
    solution = ":python",
)
