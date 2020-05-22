package(default_visibility=["//sum:__subpackages__"])

cc_binary(
    name = "cpp_WA",
    srcs = ["cpp_WA.cc"],
)

solution_test(
    name = "cpp_WA_test",
    solution = ":cpp_WA",
    judge = "//sum/judge",
    judge_args = ["--expect=reject_any"]
)
