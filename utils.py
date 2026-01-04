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

"""Utility functions for GalaxyRend addon."""

import bpy

from .config import WORKSPACE_NAME


def get_galaxyrend_props(context):
    """Get the GalaxyRend properties from the scene.

    Args:
        context: Blender context object.

    Returns:
        GalaxyRendProperties instance or None if not available.
    """
    return getattr(context.scene, "galaxyrend_props", None)


def workspace_exists(name=WORKSPACE_NAME):
    """Check if a workspace with the given name exists.

    Args:
        name: Name of the workspace to check.

    Returns:
        True if workspace exists, False otherwise.
    """
    return name in bpy.data.workspaces


def get_workspace(name=WORKSPACE_NAME):
    """Get a workspace by name.

    Args:
        name: Name of the workspace.

    Returns:
        Workspace object or None if not found.
    """
    return bpy.data.workspaces.get(name)
