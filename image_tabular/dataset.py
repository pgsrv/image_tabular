# AUTOGENERATED! DO NOT EDIT! File to edit: 01_dataset.ipynb (unless otherwise specified).

__all__ = ['ImageTabDataset', 'get_imagetabdatasets']

# Cell
from fastai.vision import *
from fastai.tabular import *

# Cell
class ImageTabDataset(Dataset):
    def __init__(self, images, tabs):
        """
        Hybrid dataset that integrates image and tabular data.

        :param images: a fastai LabelList that contains image data
        :param tabs: a fastai LabelList that contains tabular data
        """
        self.images, self.tabs = images, tabs

    def __len__(self):
        return len(self.images)

    def __getitem__(self, i):
        # return x as a tuple of image x and tabular x
        # image y and tabular y should be the same
        return (self.images[i][0], self.tabs[i][0]), self.images[i][1]

# Cell
def get_imagetabdatasets(image_data, tabular_data):
    """
    Helper function to construct train, valid, and optional test imagetabdatasets.

    :param image_data: a fastai Labellists that contains image train, valid, and optional test Labellists
    :param tabular_data: a fastai Labellists that contains tabular train, valid, and optional test Labellists
    """
    datasets = []
    for images, tabs in zip(image_data.lists, tabular_data.lists):
        datasets.append(ImageTabDataset(images, tabs))
    return datasets