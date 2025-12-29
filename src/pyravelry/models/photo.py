from typing import Optional

from pydantic import Field

from .base import BaseRavelryModel


class PhotoModel(BaseRavelryModel):
    """Represents a Ravelry Photo object.

    Covers 'Photo' and 'Photo (small)' variants.

    [Photo Ravelry API documentation](https://www.ravelry.com/api#Photo_result)
    """

    id: int
    sort_order: Optional[int] = None
    user_id: Optional[int] = Field(None, description="User ID of the photo's owner/uploader")

    # Captions
    caption: Optional[str] = Field(None, description="Photo caption")
    caption_html: Optional[str] = Field(None, description="Photo caption with image tags")
    copyright_holder: Optional[str] = None

    # Image URLs
    thumbnail_url: Optional[str] = Field(None, description="100px on longest side")
    square_url: Optional[str] = Field(None, description="75x75px square thumbnail")
    small_url: Optional[str] = Field(None, description="240px on longest side")
    small2_url: Optional[str] = Field(None, description="320px on longest side")
    medium_url: Optional[str] = Field(None, description="500px on longest side")
    medium2_url: Optional[str] = Field(None, description="640px on longest side")

    # Offsets
    x_offset: Optional[int] = Field(None, description="X offset for centered photo")
    y_offset: Optional[int] = Field(None, description="Y offset for centered photo")


class PhotoFullModel(PhotoModel):
    """Represents the 'Photo (full)' variant with additional fields.

    [Photo Ravelry API documentation](https://www.ravelry.com/api#Photo_result)
    """

    flickr_url: Optional[str] = None
    shelved_url: Optional[str] = Field(None, description="A book cover image, 150 pixels wide")
