#include <pybind11/pybind11.h>
#include <pybind11/operators.h>
#include <pybind11/stl.h>

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>

// Types
#include <maya/MAngle.h>
#include <maya/MColor.h>
#include <maya/MDagModifier.h>
#include <maya/MDagPath.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MDistance.h>
#include <maya/MDGModifier.h>
#include <maya/MEulerRotation.h>
#include <maya/MFn.h>
#include <maya/MIntArray.h>
#include <maya/MMatrix.h>
#include <maya/MNodeClass.h>
#include <maya/MObjectHandle.h>
#include <maya/MPoint.h>
#include <maya/MPlug.h>
#include <maya/MPlugArray.h>
#include <maya/MPxData.h>
#include <maya/MQuaternion.h>
#include <maya/MSelectionList.h>
#include <maya/MString.h>
#include <maya/MStringArray.h>
#include <maya/MTime.h>
#include <maya/MTypeId.h>
#include <maya/MVector.h>
#include <maya/MUuid.h>
#include <maya/MBoundingBox.h>
#include <maya/MDagPathArray.h>  // MFnDagNode
#include <maya/MObjectArray.h>  // MFnDagNode

// Function sets
#include <maya/MFnDagNode.h>
#include <maya/MFnTransform.h>
#include <maya/MFnDependencyNode.h>

#include "util/atov.hpp"
#include "util/plug.hpp"
#include "util/obj.hpp"

#include "fn/init.h"
#include "math/init.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)
#define CHECK_STATUS(status) if (!status) { throw std::runtime_error(status.errorString().asChar());}

namespace py = pybind11;

void init_types(py::module_ &);
void init_MObject(py::module_ &);
void init_MBoundingBox(py::module_ &);
void init_MDagModifier(py::module_ &);
void init_MDGModifier(py::module_ &);
void init_MPlug(py::module_ &);
void init_MSelectionList(py::module_ &);
void init_MDagPath(py::module_ &);

PYBIND11_MODULE(cmdc, m) {
    m.doc() = R"pbdoc(
        cmdc
        ----

        .. currentmodule:: cmdc

        .. autosummary::
           :toctree: _generate

    )pbdoc";

    #include "ForwardDeclarations.inl"
    #include "MFn.inl"

    init_types(m);
    init_MObject(m);
    init_MDagPath(m);
    init_MPlug(m);
    init_MBoundingBox(m);
    init_MDGModifier(m);
    init_MDagModifier(m);
    init_MSelectionList(m);
    init_math_classes(m);
    init_fn_classes(m);
    

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}