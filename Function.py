"""
This script provides functions to perform geospatial operations such as reading raster files, extracting metadata, and reprojecting data.

Author: Xiong Wanqiu
Date: June 25, 2023

Usage:
    $ python script.py
"""

import gdal
from osgeo import osr

def read_raster_file(file_path):
    """
    Read a raster file and return the raster dataset object.

    Parameters:
        file_path (str): The path to the raster file.

    Returns:
        gdal.Dataset: The raster dataset object.
    """
    dataset = gdal.Open(file_path)
    return dataset

def get_raster_metadata(dataset):
    """
    Retrieve metadata information from a raster dataset.

    Parameters:
        dataset (gdal.Dataset): The raster dataset object.

    Returns:
        dict: A dictionary containing the metadata information.
    """
    metadata = {}
    metadata['Width'] = dataset.RasterXSize
    metadata['Height'] = dataset.RasterYSize
    metadata['Projection'] = dataset.GetProjection()
    metadata['GeoTransform'] = dataset.GetGeoTransform()
    return metadata

def reproject_raster(dataset, output_path, target_projection):
    """
    Reproject a raster dataset to a specified projection.

    Parameters:
        dataset (gdal.Dataset): The raster dataset object.
        output_path (str): The output path for the reprojected raster file.
        target_projection (osgeo.osr.SpatialReference): The target projection.

    Returns:
        str: The path to the reprojected raster file.
    """
    # Create the output dataset with the target projection
    driver = gdal.GetDriverByName('GTiff')
    output_dataset = driver.CreateCopy(output_path, dataset)
    output_dataset.SetProjection(target_projection.ExportToWkt())

    # Perform the reprojection
    gdal.ReprojectImage(dataset, output_dataset, dataset.GetProjection(), target_projection.ExportToWkt(), gdal.GRA_Bilinear)

    return output_path


