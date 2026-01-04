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

"""GalaxyRend - Blender addon for the GalaxyRend distributed render network."""

bl_info = {
    "name": "GalaxyRend",
    "author": "RichoKD",
    "description": "Blender addon for the GalaxyRend distributed render network",
    "blender": (2, 80, 0),
    "version": (1, 0, 0),
    "location": "View3D > Sidebar > GalaxyRend",
    "category": "Render",
}

import bpy

from .operators import GalaxyRend_OT_create_workspace, GalaxyRend_OT_submit
from .panels import GalaxyRend_PT_main_panel
from .preferences import GalaxyRendPreferences
from .properties import GalaxyRendProperties

# List of classes to register
classes = (
    GalaxyRendProperties,
    GalaxyRendPreferences,
    GalaxyRend_OT_submit,
    GalaxyRend_OT_create_workspace,
    GalaxyRend_PT_main_panel,
)


def register():
    """Register all classes and properties."""
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.galaxyrend_props = bpy.props.PointerProperty(type=GalaxyRendProperties)


def unregister():
    """Unregister all classes and properties."""
    del bpy.types.Scene.galaxyrend_props

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
