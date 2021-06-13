import cmdc

import inspect
import pybind11_stubgen
import time

STUBS_LOCATION = "build/cmdc.pyi"

def cleanup_imports(content):
    """Remove any classes accidentally imported as modules.

    This is a fix for this bug:
    https://github.com/sizmailov/pybind11-stubgen/issues/36
    Some classes with nested classes get imported when they shouldn't, breaking
    leaving them breaks autocomplete
    """

    classes = []
    for name, obj in inspect.getmembers(cmdc, inspect.isclass):
        classes.append(name)

        # also include any class that might be defined inside of another class.
        # these are actually the ones that are causing issues.
        for sub_name, _ in inspect.getmembers(obj, inspect.isclass):
            classes.append(sub_name)

    for class_name in classes:
        content = content.replace("import {}\n".format(class_name), "")

    return content

print("Generating stubs")
t0 = time.time()

module = pybind11_stubgen.ModuleStubsGenerator(cmdc)
module.write_setup_py = False

print("(1) Parsing module..")

module.parse()

t1 = time.time()
print("(1) Finished in {0:0.3} s".format(t1-t0))
print("(1) ----------------------------")

print("(2) Generating stubs content..")

content = "\n".join(module.to_lines())
content = cleanup_imports(content)

t2 = time.time()
print("(2) Finished in {0:0.3} s".format(t2-t1))
print("(2) ----------------------------")
print("(3) Writing stubs file..")

with open(STUBS_LOCATION, "w") as handle:
    handle.write(content)

t3 = time.time()
print("(3) Finished in {0:0.3} s".format(t3-t2))
print("(3) ----------------------------")

print("Succesfully created .{0} in {1:0.3} s".format(STUBS_LOCATION, t3-t0))

