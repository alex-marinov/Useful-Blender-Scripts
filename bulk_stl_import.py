import bpy
import os

# Root folder path
root_folder = 'root-folder-path'

def create_collections(root, parent_collection):
    for item in os.listdir(root):
        item_path = os.path.join(root, item)
        if os.path.isdir(item_path):
            # Create a collection for the current folder
            collection = bpy.data.collections.new(item)
            parent_collection.children.link(collection)
            # Recursively create collections for subfolders
            create_collections(item_path, collection)
            # Import STL files within the current collection
            import_stl_files(item_path, collection)

def import_stl_files(root, parent_collection):
    for file in os.listdir(root):
        file_path = os.path.join(root, file)
        if file.endswith(".stl"):
            # Import the STL file
            # Support both Blender 5+ (wm.stl_import) and older versions (import_mesh.stl)
            if hasattr(bpy.ops.wm, 'stl_import'):
                # Blender 5+ uses the new API
                bpy.ops.wm.stl_import(filepath=file_path)
            else:
                # Older Blender versions use the legacy API
                bpy.ops.import_mesh.stl(filepath=file_path)
            # Move the imported object to the parent collection
            obj = bpy.context.selected_objects[0]
            parent_collection.objects.link(obj)

# Create a main collection for the root folder
main_collection = bpy.data.collections.new(os.path.basename(root_folder))
bpy.context.scene.collection.children.link(main_collection)

# Recursively create collections and import STL files
create_collections(root_folder, main_collection)