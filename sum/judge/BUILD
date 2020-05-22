package(default_visibility=["//visibility:public"])

simple_judge(
    name = "judge",
    dataset = ":dataset",
)

sample_test(
    name = "sample_test",
    files = glob(["*.out"]),
    judge = ":judge",
)

dataset_derive(
    name = "dataset",
    exec = "//sum/cpp",
    dataset = ":input",
)

dataset_merge(
    name = "input",
    files = glob(["*.in"]),
    datasets = [":input_generated"],
)

dataset_generate(
    name = "input_generated",
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
