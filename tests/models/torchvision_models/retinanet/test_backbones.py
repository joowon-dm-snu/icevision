import pytest
from icevision.all import *
from icevision.models.torchvision import retinanet


@pytest.mark.skip
@pytest.mark.parametrize(
    "model_name",
    (
        "resnet101_fpn",
        "resnet152_fpn",
        "resnext101_32x8d_fpn",
        "wide_resnet101_2_fpn",
    ),
)
def test_retinanet_fpn_backbones_large(model_name):
    backbone_fn = getattr(models.torchvision.retinanet.backbones, model_name)
    backbone = backbone_fn(pretrained=False)

    model = retinanet.model(num_classes=4, backbone=backbone)
    assert len(model.param_groups()) == 7


@pytest.mark.skip
@pytest.mark.parametrize(
    "model_name",
    (
        "resnet34_fpn",
        "resnet50_fpn",
        "resnext50_32x4d_fpn",
        "wide_resnet50_2_fpn",
    ),
)
def test_retinanet_fpn_backbones_medium(model_name):
    backbone_fn = getattr(models.torchvision.retinanet.backbones, model_name)
    backbone = backbone_fn(pretrained=False)

    model = retinanet.model(num_classes=4, backbone=backbone)
    assert len(model.param_groups()) == 7


@pytest.mark.parametrize(
    "model_name",
    ("resnet18_fpn",),
)
def test_retinanet_fpn_backbones_small(model_name):
    backbone_fn = getattr(models.torchvision.retinanet.backbones, model_name)
    backbone = backbone_fn(pretrained=False)

    model = retinanet.model(num_classes=4, backbone=backbone)
    assert len(model.param_groups()) == 7
