package(default_visibility=["//sum:__subpackages__"])

py_binary(
    name = "generator",
    srcs = ["generator.py"],
    deps = ["//sum:constraints_py"],
)

dataset_generate(
    name = "inputs_generated",
    exec = ":generator",
)

dataset_merge(
    name = "inputs",
    files = glob(["*.in"]),
    datasets = [":inputs_generated"],
)

dataset_derive(
    name = "dataset",
    exec = "//sum/cpp",
    dataset = ":inputs",
)

simple_judge(
    name = "judge",
    dataset = ":dataset",
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

filegroup(
    name = "sample_outputs",
    srcs = glob(["*.out"]),
)

sample_test(
    name = "sample_test",
    files = [":sample_outputs"],
    judge = ":judge",
)
