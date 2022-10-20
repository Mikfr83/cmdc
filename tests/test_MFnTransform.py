import nose.tools

import cmdc 


def test_init_transform():
    transform = cmdc.FnTransform()


def test_create_transform():
    transform = cmdc.FnTransform()

    transformObj = transform.create()
    assert not transformObj.isNull()


def test_limits():
    transform = cmdc.FnTransform()
    transform.create()

    assert not transform.isLimited(cmdc.FnTransform.kScaleMinX)

    transform.enableLimit(cmdc.FnTransform.kScaleMinX, True)
    assert transform.isLimited(cmdc.FnTransform.kScaleMinX)


def test_scale():
    transform = cmdc.FnTransform()
    transform.create()

    transform.scaleBy([2.0, 3.0, 4.0])
    transformation = transform.transformation
    assert transformation.scale(cmdc.Space.kTransform) == [2.0, 3.0, 4.0]

    transform.setScale([4.0, 2.0, 1.0])
    transformation = transform.transformation
    assert transformation.scale(cmdc.Space.kTransform) == [4.0, 2.0, 1.0]


def test_translate():
    transform = cmdc.FnTransform()
    transform.create()

    t = cmdc.Vector(2.0, 3.0, 4.0)
    transform.translateBy(t, cmdc.Space.kTransform)
    transformation = transform.transformation
    assert transformation.translation(cmdc.Space.kTransform) == t

    t = cmdc.Vector(4.0, 2.0, 1.0)
    transform.setTranslation(t, cmdc.Space.kTransform)
    transformation = transform.transformation
    assert transformation.translation(cmdc.Space.kTransform) == t


def test_rotation():
    transform = cmdc.FnTransform()
    transform.create()