from __future__ import annotations

from dataclasses import dataclass, fields
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bpy.types import Armature

    from io_scene_ueformat.op.settings import UFSettings


@dataclass(slots=True)
class UEFormatOptions:
    link: bool = True
    scale_factor: float = 0.01

    @classmethod
    def from_settings(cls, settings: UFSettings) -> UEFormatOptions:
        field_names = {field.name for field in fields(cls)}
        return cls(**{k: v for k, v in settings.get_props().items() if k in field_names})


@dataclass(slots=True)
class UEModelOptions(UEFormatOptions):
    bone_length: float = 4.0
    reorient_bones: bool = False
    import_collision: bool = False
    import_sockets: bool = True
    import_morph_targets: bool = True
    import_lods: bool = False
    import_virtual_bones: bool = False


@dataclass(slots=True)
class UEAnimOptions(UEFormatOptions):
    rotation_only: bool = False
    override_skeleton: Armature | None = None