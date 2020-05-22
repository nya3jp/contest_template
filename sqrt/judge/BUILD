package(default_visibility=["//sqrt:__subpackages__"])

py_binary(
    name = "generator",
    srcs = ["generator.py"],
    deps = ["//sqrt:constraints_py"],
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
    exec = "//sqrt/python",
    dataset = ":inputs",
)

py_binary(
    name = "comparator",
    srcs = ["comparator.py"],
    deps = ["//sqrt:constraints_py"],
)

simple_judge(
    name = "judge",
    dataset = ":dataset",
    comparator = ":comparator",
)

py_binary(
    name = "validator",
    srcs = ["validator.py"],
    deps = ["//sqrt:constraints_py"],
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
