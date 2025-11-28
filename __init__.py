# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""FluxFrame - Blender addon for the FluxFrame distributed render network."""

bl_info = {
    "name": "FluxFrame",
    "author": "RichoKD",
    "description": "Blender addon for the FluxFrame distributed render network",
    "blender": (2, 80, 0),
    "version": (1, 0, 0),
    "location": "View3D > Sidebar > FluxFrame",
    "category": "Render",
}

import bpy

from .operators import FLUXFRAME_OT_create_workspace, FLUXFRAME_OT_submit
from .panels import FLUXFRAME_PT_main_panel
from .preferences import FluxFramePreferences
from .properties import FluxFrameProperties

# List of classes to register
classes = (
    FluxFrameProperties,
    FluxFramePreferences,
    FLUXFRAME_OT_submit,
    FLUXFRAME_OT_create_workspace,
    FLUXFRAME_PT_main_panel,
)


def register():
    """Register all classes and properties."""
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.fluxframe_props = bpy.props.PointerProperty(type=FluxFrameProperties)


def unregister():
    """Unregister all classes and properties."""
    del bpy.types.Scene.fluxframe_props

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
