package(default_visibility = ["//sqrt:__subpackages__"])

load("@rules_contest//contest:defs.bzl", "solution_test")

py_binary(
    name = "python",
    srcs = ["python.py"],
    python_version = "PY3",
    srcs_version = "PY3",
)

solution_test(
    name = "python_test",
    judge = "//sqrt/judge",
    solution = ":python",
)
