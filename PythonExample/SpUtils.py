import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np

def drawbbox(anns):
  if len(anns) == 0:
    return 0
  if 'segmentation' in anns[0] or 'keypoints' in anns[0]:
    datasetType = 'instances'
  elif 'caption' in anns[0]:
    datasetType = 'captions'
  else:
    raise Exception('datasetType not supported')  
  if datasetType == 'instances':
    ax = plt.gca()
    ax.set_autoscale_on(False)      
    polygons = []
    color = []
    for ann in anns:
      c = (np.random.random((1, 3))*0.6+0.4).tolist()[0]
      [bbox_x, bbox_y, bbox_w, bbox_h] = ann['bbox']
      poly = [[bbox_x, bbox_y], [bbox_x, bbox_y+bbox_h], [bbox_x+bbox_w, bbox_y+bbox_h], [bbox_x+bbox_w, bbox_y]]
      np_poly = np.array(poly).reshape((4,2))
      polygons.append(Polygon(np_poly))
      color.append(c)
    #p = PatchCollection(polygons, facecolor=color, linewidths=0, alpha=0.4)
    #ax.add_collection(p)
    p = PatchCollection(polygons, facecolor='none', edgecolors=color, linewidths=2)
    ax.add_collection(p)
