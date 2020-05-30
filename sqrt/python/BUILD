package(default_visibility = ["//sqrt:__subpackages__"])

load("@rules_contest//contest:defs.bzl", "solution_test")

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
