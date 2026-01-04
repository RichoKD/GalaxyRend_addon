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

"""UI panels and layout for GalaxyRend addon."""

from bpy.types import Panel

from .config import ADDON_NAME
from .utils import get_galaxyrend_props


class GalaxyRend_PT_main_panel(Panel):
    """Main panel in the sidebar."""

    bl_label = ADDON_NAME
    bl_idname = "GalaxyRend_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = ADDON_NAME

    def draw(self, context):
        layout = self.layout
        props = get_galaxyrend_props(context)

        # Create workspace button
        layout.operator("galaxyrend.create_workspace", icon="WORKSPACE")

        layout.separator()

        # Text field
        if props is not None:
            layout.prop(props, "input_text", text="")

        # Submit button
        layout.operator("galaxyrend.submit", icon="CHECKMARK")
