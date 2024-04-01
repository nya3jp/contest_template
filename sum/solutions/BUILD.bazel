package(default_visibility = ["//sum:__subpackages__"])

load("@rules_contest//contest:defs.bzl", "solution_test")

cc_binary(
    name = "cpp",
    srcs = ["cpp.cc"],
)

solution_test(
    name = "cpp_test",
    judge = "//sum/judge",
    solution = ":cpp",
)

cc_binary(
    name = "cpp_WA",
    srcs = ["cpp_WA.cc"],
)

solution_test(
    name = "cpp_WA_test",
    judge = "//sum/judge",
    judge_args = ["--expect=reject_any"],
    solution = ":cpp_WA",
)

py_binary(
    name = "python",
    srcs = ["python.py"],
    python_version = "PY3",
    srcs_version = "PY3",
)

solution_test(
    name = "python_test",
    judge = "//sum/judge",
    solution = ":python",
)
