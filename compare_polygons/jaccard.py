from shapely.geometry import box, Polygon
import numpy as np
import polis

def compare_polys(poly_a, poly_b):
    """Compares two polygons via the Jaccard distance metric.

    Input:
        poly_a: A Shapely polygon.
        poly_b: Another Shapely polygon.

    Returns:
        The Jaccard distance between these two polygons.
    """
    intersection = poly_a.intersection(poly_b).area
    union = poly_a.union(poly_b).area
    jaccard = 1 - intersection/union
    return jaccard

if __name__ == "__main__":
    ground_truth_boxes = [np.array([[ 62, 135],
            [120, 208],
            [144, 188],
            [ 86, 115]], dtype=np.int32),
    np.array([[ 65, 115],
            [120, 208],
            [144, 188],
            [ 86, 120]], dtype=np.int32),
    np.array([[ 60, 95],
            [111, 190],
            [143, 178],
            [ 86, 120]], dtype=np.int32),
    np.array([[ 50, 145],
            [124, 190],
            [143, 178],
            [ 90, 115]], dtype=np.int32)]

    polys_gt = [Polygon(c) for c in ground_truth_boxes]
    centroids_gt = [np.asarray(p.centroid) for p in polys_gt]
    areas_gt = [p.area for p in polys_gt]
    bounds_gt = [p.bounds for p in polys_gt]
    sizes_gt = [[p[2]-p[0], p[3]-p[1]] for p in bounds_gt]
    radii_gt = [np.sqrt( size[0]**2 + size[1]**2 ) for size in sizes_gt]

    # comare all polygons to the first polygoin
    poly = polys_gt[0]

    for itmp in range(len(polys_gt)):
        poly_tmp = polys_gt[itmp]
        compare_polys(poly, poly_tmp)
        print 'Polis: ', polis.compare_polys(poly, poly_tmp)
