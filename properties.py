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

"""Blender properties and data for FluxFrame addon."""

from bpy.props import StringProperty
from bpy.types import PropertyGroup

from .config import INPUT_TEXT_MAX_LENGTH


class FluxFrameProperties(PropertyGroup):
    """Property group for FluxFrame addon settings."""

    input_text: StringProperty(
        name="Input Text",
        description="Enter text here",
        default="",
        maxlen=INPUT_TEXT_MAX_LENGTH,
    )
