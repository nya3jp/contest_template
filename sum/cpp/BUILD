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
