# %%
import open3d.ml.torch as ml3d  # or open3d.ml.tf as ml3d
import open3d.visualization.rendering as rendering
import open3d.visualization.gui as gui
import open3d as o3d
o3d.visualization.webrtc_server.enable_webrtc()

def visualize(data):
    app = gui.Application.instance
    app.initialize()

    vis = o3d.visualization.O3DVisualizer("Open3D visualizer", 1024, 768)
    vis.show_settings = True
    vis.add_geometry("data", data)

    vis.reset_camera_to_default()

    app.add_window(vis)
    app.run()

# construct a dataset by specifying dataset_path
dataset = ml3d.datasets.SemanticKITTI(dataset_path='dataa/SemanticKITTI')

# get the 'all' split that combines training, validation and test set
val_split = dataset.get_split('val')

# print the attributes of the first datum
print(val_split.get_attr(0))

# print the shape of the first point cloud
print(val_split.get_data(0)['point'].shape)

print(type(val_split.get_data(0)['point']))

pcd = o3d.geometry.PointCloud() 
pcd.points = o3d.utility.Vector3dVector(val_split.get_data(0)['point'])

print(type(pcd.points))

# # show the first 100 frames using the visualizer
vis = ml3d.vis.Visualizer()
vis.visualize_dataset(dataset, 'all', indices=range(100))
# visualize(pcd)
# o3d.visualization.draw_plotly([pcd])
