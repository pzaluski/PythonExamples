def test_args_kwargs(*args, **kwargs):
    if kwargs:
        for kwarg in kwargs:
            print(kwarg)
    else:
        for arg in args:
            print(arg)

args = ["two", 3, 5]
test_args_kwargs(*args)
kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(**kwargs)