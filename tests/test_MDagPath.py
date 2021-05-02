import nose
import cmdc

def test_equality():
    sel = cmdc.SelectionList().add("persp")

    a = sel.getDagPath(0)
    b = sel.getDagPath(0)
    assert a == b


def test_apiType():
    sel = cmdc.SelectionList().add("persp")

    valid_dag = sel.getDagPath(0)
    assert valid_dag.apiType() == cmdc.Fn.Type.kTransform

    invalid_dag = cmdc.DagPath()
    nose.tools.assert_raises(
        RuntimeError,
        invalid_dag.apiType,
    )

def test_child():
    sel = cmdc.SelectionList().add("persp").add("perspShape")

    dag_with_child = sel.getDagPath(0)
    assert isinstance(dag_with_child.child(0), cmdc.Object)
    
    dag_without_children = sel.getDagPath(1)
    nose.tools.assert_raises(
        IndexError,
        dag_without_children.child,
        0
    )

    invalid_dag = cmdc.DagPath()
    nose.tools.assert_raises(
        RuntimeError,
        invalid_dag.child,
        0
    )

def test_childCount():
    sel = cmdc.SelectionList().add("persp").add("perspShape")

    persp = sel.getDagPath(0)
    assert persp.childCount() == 1

    persp_shape = sel.getDagPath(1)
    assert persp_shape.childCount() == 0

    invalid_dag = cmdc.DagPath()
    nose.tools.assert_raises(
        RuntimeError,
        invalid_dag.childCount,
    )

def test_exclusiveMatrix():
    sel = cmdc.SelectionList().add("persp").add("perspShape")

    persp = sel.getDagPath(0)
    assert isinstance(persp.exclusiveMatrix(), cmdc.Matrix)

    # I would have expected this to raise a RuntimeError
    invalid_dag = cmdc.DagPath()
    nose.tools.assert_raises(
        RuntimeError,
        invalid_dag.exclusiveMatrix,
    )


def test_exclusiveMatrixInverse():
    sel = cmdc.SelectionList().add("persp").add("perspShape")

    persp = sel.getDagPath(0)
    assert isinstance(persp.exclusiveMatrixInverse(), cmdc.Matrix)

    # I would have expected this to raise a RuntimeError
    invalid_dag = cmdc.DagPath()
    nose.tools.assert_raises(
        RuntimeError,
        invalid_dag.exclusiveMatrixInverse,
    )


def test_extendToShape():
    sel = cmdc.SelectionList().add("persp").add("perspShape")

    persp = sel.getDagPath(0)
    persp_shape = sel.getDagPath(1)
    persp.extendToShape()
    assert persp == persp_shape

    invalid_dag = cmdc.DagPath()
    nose.tools.assert_raises(
        RuntimeError,
        invalid_dag.extendToShape,
    )
