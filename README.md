<a href=/cmda/><p align=center><img width=90 src=https://user-images.githubusercontent.com/2152766/115344277-0e81de80-a1a5-11eb-92ba-e580d91537da.png></p></a>

<p align=center>a.k.a. "Maya Python API 3.0"</p>

<br>

An alternative set of bindings for the C++ API of Maya 2018-2022.

**Why?**

- What if Maya's Python bindings were open source?
- What if whenever Maya crashed, you'd get more than an opaque stack trace?
- What if you were able to see why a crash occurred, and what line it occurred on?
- What if you could address bugs in the bindings yourself?
- What if you could *add* missing members yourself?
- What if there were bindings for Maya that made it impossible to crash Maya from Python?
- What if setting up code completion and type checking was easy?

That's what this repository is for.

<br>

### Example

The bindings should aim to match Maya Python API 2.0 as closely as possible, with the exception of being open source and to *never* allow Maya to crash as a result of calling any function or method.

```py
import cmdc

typ = cmdc.TypeId(16)

mat4 = cmdc.Matrix()
mat4 *= cmdc.Matrix().inverse()

vec3 = cmdc.Vector()
vec3.x = 6

quat = cmdc.Quaternion(angle=0.5, axis=cmdc.Vector(1, 0, 0))
mat4 *= quat

# No need for MString
string = str()

# Modify the Maya scene graph
from maya import standalone
standalone.initialize()
fn = cmdc.FnDependencyNode()
r = fn.create("reverse", name="myReverse")
print(fn.name())

# This next line really shouldn't work, should require MFnDagNode
t = fn.create("transform", name="myTransform")
print(fn.name())

print("Success")
```

**Code completion working in Visual Studio Code with Pylance**

<img width=500 src=https://user-images.githubusercontent.com/3117205/121947966-f7034400-cd56-11eb-85ad-5b1d9aac091d.gif>

**Type Checking working in Visual Studio Code with Pylance**

<img width=500 src=https://user-images.githubusercontent.com/3117205/121947972-f8347100-cd56-11eb-8782-3d5fcd6c4376.gif>

<br>

### Goal

`cmdc` should have the same advantages over 1.0 as 2.0, and more.

- Array types are full Python sequences, including slice support.
- Methods which take Maya array parameters will *always* also take native Python sequences, such as arrays and tuples.
- The outputs of methods are *always* returned in their return values, not through their parameter lists.
- Methods which return multiple values (e.g. MFnFluid.getResolution) return them as a tuple or list, eliminating the need for MScriptUtil.
- Object attributes are preferred over rather than set/get methods. For example you can now write array.sizeIncrement=64.
- There are more types of exceptions used when methods fail. Not everything is a RuntimeError, as was the case in the old API.
- `cmdc` should be faster or as fast as API 2.0
  > [Reference](https://help.autodesk.com/view/MAYAUL/2020/ENU/?guid=__py_ref_index_html)
- `cmdc` comes with fully type annotated stubs, making it easy to set up code completion as well as type checking.

<br>

### Status

![](https://img.shields.io/badge/prototype-0.1-brightgreen)

It'll work, but won't have half the things you'll need to do anything of use in Maya. The current source is enough to illustrate (1) how to expose types, (2) how to expose function sets and (3) how to deal with passing MObject references around.

<br>

### Repository

| File | Description
|:-----|:-------------
| `cmake/`          | CMake setup for Maya and Python libraries
| `docker/`         | Docker containers for building in linux
| `os/`             | The missing Python libraries for all operating systems and Python versions
| `pyblind11/`      | The pybind11 source
| `scripts/`        | Code-generation
| `src/`            | C++ source for the pybind11 bindings
| `tests/`          | Tests for bound methods and types


<br>

### Build

Build requirements:

- [CMake 3.4 or later](https://cmake.org/download/)
- [Maya devkit](https://www.autodesk.com/developer-network/platform-technologies/maya)
- Complier and toolchain requirements listed in Maya's API documentation

```
cmake -B ./build -DCMAKE_BUILD_TYPE=Release -DMAYA_VERSION=2020 -DMAYA_DEVKIT_ROOT="path/to/devkit"
cmake --build ./build --config Release
```

This should build on any platform, for any Maya with Python available. Including 2023.

<br>

### Contributing

Interested in helping out? Here's how to do it.

1. Get a free compiler, like [Visual Studio 2019](https://visualstudio.microsoft.com/vs/community/) for Windows
1. Download and unzip a [Maya devkit](https://www.autodesk.com/developer-network/platform-technologies/maya) (scroll down)
2. Clone this repository
3. Write your header file
4. Submit a pull-request
5. Profit

**FAQ**

> Do I need to know C++?

Not really! What we're doing here is mostly busy-work, filling in the many functions exposed by the Maya API. Most if not all trickery has already been done in other functions, so copy/paste is a valid option.

> I don't have any other questions?

Great, then here's what's next.

```bash
# Tell cmdc about where your devkit is
$env:DEVKIT_LOCATION="C:\maya-devkit"

# Clone the big jeeves out of this repository
git clone https://github.com/mottosso/cmdc.git

cd cmdc

# Either write your own header from scratch..
# ..or generate some boiler plate of your favourite header!
mayapy ./scripts/parse_header.py MFnDagNode.h
```

From here, you'll have a freshly generated header file, ready to fill in. As you fill things in, see [build](#build) above for how to iterate and once you're happy you're welcome to submit a Pull Request!
