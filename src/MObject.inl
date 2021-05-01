py::class_<MObject>(m, "Object")
    .def(py::init<>())
    .def(py::init<const MObject &>())

    .def("isNull", &MObject::isNull, 
        R"pbdoc(Return True if the internal Maya Object does not exist.)pbdoc")
    .def("hasFn", [](MObject& self, MFn::Type type) -> bool {
        return self.hasFn(type);
    }, R"pbdoc(Return True if the internal Maya Object is compatible with the given Function Type.)pbdoc",
        py::arg("type"))
    .def("apiType", [](MObject& self) -> MFn::Type {
        return self.apiType();
    }, R"pbdoc(Return the exact type of the internal Maya Object.)pbdoc")
    .def("apiTypeStr", [](MObject& self) -> std::string {
        return self.apiTypeStr();
    }, R"pbdoc(Return the type name of the internal Maya Object.)pbdoc")

    .def("__eq__", [](MObject& self, const MObject& other) -> bool{
        return (self == other);
    }, R"pbdoc(Returns true if both MObjects refer to the same Maya object.)pbdoc")

    .def("__repr__", [](const MObject &self) {
        std::string ret = "<cmdc.Object(";
        ret += self.apiTypeStr();
        ret += ")>";
        return ret;
    }
);