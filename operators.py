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

"""User actions and operations for FluxFrame addon."""

import bpy
from bpy.types import Operator

from .config import WORKSPACE_NAME
from .utils import get_fluxframe_props, get_workspace, workspace_exists


class FLUXFRAME_OT_submit(Operator):
    """Submit button operator."""

    bl_idname = "fluxframe.submit"
    bl_label = "Submit"
    bl_description = "Submit the input text"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        props = get_fluxframe_props(context)
        if props is None:
            self.report({"ERROR"}, "FluxFrame properties not available")
            return {"CANCELLED"}

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
        if workspace_exists():
            self.report({"INFO"}, f"Workspace '{WORKSPACE_NAME}' already exists")
            # Switch to the existing workspace
            context.window.workspace = get_workspace()
            return {"FINISHED"}

        # Duplicate the current workspace as a base
        bpy.ops.workspace.duplicate()

        # Get the newly created workspace (it's the active one after duplication)
        new_workspace = context.window.workspace

        # Rename it
        new_workspace.name = WORKSPACE_NAME

        self.report({"INFO"}, f"Created workspace: {WORKSPACE_NAME}")
        return {"FINISHED"}
