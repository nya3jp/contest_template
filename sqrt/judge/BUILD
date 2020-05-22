package(default_visibility=["//visibility:public"])

simple_judge(
    name = "judge",
    dataset = ":dataset",
    comparator = ":comparator",
    input_extension = "in",
    answer_extension = "golden",
)

dataset_derive(
    name = "dataset",
    exec = "//sqrt/python",
    dataset = ":dataset_merged",
    input_extension = "in",
    output_extension = "golden",
)

dataset_merge(
    name = "dataset_merged",
    files = glob(["*.in", "*.out"]),
    datasets = [":dataset_generated"],
)

dataset_generate(
    name = "dataset_generated",
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
