# Blender-STL-Bulk-Importer

## Description

This repository contains useful Blender Python scripts to enhance your workflow with collections and STL files.

## Scripts

### 1. Bulk STL Import (`bulk_stl_import.py`)

This Python script is used to create collections and import STL files in Blender using the bpy (Blender Python) library. It recursively traverses a specified root folder, creates collections for subfolders, and imports STL files into the corresponding collections.

#### Usage

1. Replace `'root-folder-path'` with the actual root folder path in the script.
2. Run the script in Blender's scripting interface or from the command line using Blender's `--python` option:
   ```bash
   blender --python bulk_stl_import.py
   ```

### 2. Collection Switcher for 3D Viewport (`collection_switcher_viewport.py`)

This addon allows you to switch between collections using number keys 1-9 while the cursor is in the 3D Viewport. By default, Blender only supports collection switching with number keys in the Outliner editor - this script extends that functionality to the 3D Viewport.

#### Features

- Bind keys 1-9 (both regular and numpad) to switch collections in the 3D Viewport
- Pressing 1 shows Collection 1 and hides others
- Pressing 2 shows Collection 2 and hides others, and so on
- Works seamlessly alongside the native Outliner collection switching
- Compatible with Blender 5+

#### Installation

1. Open Blender
2. Go to Edit → Preferences → Add-ons
3. Click "Install..." and select `collection_switcher_viewport.py`
4. Enable the addon by checking the box next to "Collection Switcher for 3D View"

#### Usage

Once the addon is installed and enabled:
1. Make sure you have collections in your scene (Collection 1, Collection 2, etc.)
2. Position your cursor in the 3D Viewport
3. Press number keys 1-9 to switch between collections
4. The selected collection will be shown while others are hidden

Alternatively, you can run the script directly in Blender's scripting interface:
```bash
blender --python collection_switcher_viewport.py
```

## Notes

Feel free to customize these scripts as needed for your project.
If you have any further questions or need additional assistance, please feel free to ask!
