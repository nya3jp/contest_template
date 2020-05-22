package(default_visibility=["//visibility:public"])

simple_judge(
    name = "judge",
    dataset = ":dataset",
    comparator = ":comparator",
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

dataset_derive(
    name = "dataset",
    exec = "//sqrt/python",
    dataset = ":inputs",
)

dataset_merge(
    name = "inputs",
    files = glob(["*.in"]),
    datasets = [":inputs_generated"],
)

dataset_generate(
    name = "inputs_generated",
    exec = ":generator",
)

py_binary(
    name = "generator",
    srcs = ["generator.py"],
    deps = ["//sqrt:constraints_py"],
)

py_binary(
    name = "validator",
    srcs = ["validator.py"],
    deps = ["//sqrt:constraints_py"],
)

py_binary(
    name = "comparator",
    srcs = ["comparator.py"],
    deps = ["//sqrt:constraints_py"],
)

dataset_test(
    name = "dataset_test",
    exec = ":validator",
    dataset = ":dataset",
)
