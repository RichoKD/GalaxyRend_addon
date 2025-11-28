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
from bpy.props import StringProperty
from bpy.types import Operator, Panel, PropertyGroup


class FluxFrameProperties(PropertyGroup):
    """Property group for FluxFrame addon settings."""

    input_text: StringProperty(
        name="Input Text",
        description="Enter text here",
        default="",
        maxlen=1024,
    )


class FLUXFRAME_OT_submit(Operator):
    """Submit button operator."""

    bl_idname = "fluxframe.submit"
    bl_label = "Submit"
    bl_description = "Submit the input text"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        props = context.scene.fluxframe_props
        input_text = props.input_text

        if input_text:
            self.report({"INFO"}, f"Submitted: {input_text}")
        else:
            self.report({"WARNING"}, "No text entered")

        return {"FINISHED"}


class FLUXFRAME_OT_create_workspace(Operator):
    """Create a blank FluxFrame workspace."""

    bl_idname = "fluxframe.create_workspace"
    bl_label = "Create FluxFrame Workspace"
    bl_description = "Create a new blank workspace for FluxFrame"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # Check if workspace already exists
        workspace_name = "FluxFrame"
        if workspace_name in bpy.data.workspaces:
            self.report({"INFO"}, f"Workspace '{workspace_name}' already exists")
            # Switch to the existing workspace
            context.window.workspace = bpy.data.workspaces[workspace_name]
            return {"FINISHED"}

        # Duplicate the current workspace as a base
        bpy.ops.workspace.duplicate()

        # Get the newly created workspace (it's the active one after duplication)
        new_workspace = context.window.workspace

        # Rename it
        new_workspace.name = workspace_name

        self.report({"INFO"}, f"Created workspace: {workspace_name}")
        return {"FINISHED"}


class FLUXFRAME_PT_main_panel(Panel):
    """Main panel in the sidebar."""

    bl_label = "FluxFrame"
    bl_idname = "FLUXFRAME_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "FluxFrame"

    def draw(self, context):
        layout = self.layout
        props = context.scene.fluxframe_props

        # Create workspace button
        layout.operator("fluxframe.create_workspace", icon="WORKSPACE")

        layout.separator()

        # Text field
        layout.prop(props, "input_text", text="")

        # Submit button
        layout.operator("fluxframe.submit", icon="CHECKMARK")


# List of classes to register
classes = (
    FluxFrameProperties,
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
