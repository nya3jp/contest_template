package(default_visibility=["//sum:__subpackages__"])

cc_binary(
    name = "cpp",
    srcs = ["cpp.cc"],
)

solution_test(
    name = "cpp_test",
    solution = ":cpp",
    judge = "//sum/judge",
)
