package(default_visibility=["//visibility:public"])

markdown(
    name = "statement",
    src = ":statement_subst",
)

jinja2_template(
    name = "statement_subst",
    srcs = ["statement.md"],
    files = ["//sum/judge:sample_outputs"],
    vars = ["constraints.yaml"],
    dataset = "//sum/judge:dataset",
)

py_yaml_library(
    name = "constraints_py",
    src = "constraints.yaml",
)
