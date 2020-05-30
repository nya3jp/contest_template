package(default_visibility = ["//sum:__subpackages__"])

cc_binary(
    name = "cpp",
    srcs = ["cpp.cc"],
)

solution_test(
    name = "cpp_test",
    judge = "//sum/judge",
    solution = ":cpp",
)
