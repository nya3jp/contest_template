package(default_visibility=["//visibility:public"])

simple_judge(
    name = "judge",
    dataset = ":dataset",
)

dataset_derive(
    name = "dataset",
    exec = "//sum/cpp",
    dataset = ":dataset_merged",
    input_extension = "in",
    output_extension = "diff",
)

dataset_merge(
    name = "dataset_merged",
    files = glob(["*.in", "*.diff"]),
    datasets = [":dataset_generated"],
)

dataset_generate(
    name = "dataset_generated",
    exec = ":generator",
)

py_binary(
    name = "generator",
    srcs = ["generator.py"],
    deps = ["//sum:constraints_py"],
)

py_binary(
    name = "validator",
    srcs = ["validator.py"],
    deps = ["//sum:constraints_py"],
)

dataset_test(
    name = "dataset_test",
    exec = ":validator",
    dataset = ":dataset",
)
