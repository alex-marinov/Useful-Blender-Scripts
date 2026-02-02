import bpy

bl_info = {
    "name": "Collection Switcher for 3D View",
    "author": "Alex Marinov (alex@konsept.design)",
    "version": (0, 0, 1),
    "blender": (5, 0, 1),
    "description": "Switch between collections using number keys 1-9 in 3D Viewport",
    "category": "3D View",
}

# Mapping from index to key type names
NUMBER_KEYS = {
    1: 'ONE',
    2: 'TWO',
    3: 'THREE',
    4: 'FOUR',
    5: 'FIVE',
    6: 'SIX',
    7: 'SEVEN',
    8: 'EIGHT',
    9: 'NINE',
}

NUMPAD_KEYS = {
    1: 'NUMPAD_1',
    2: 'NUMPAD_2',
    3: 'NUMPAD_3',
    4: 'NUMPAD_4',
    5: 'NUMPAD_5',
    6: 'NUMPAD_6',
    7: 'NUMPAD_7',
    8: 'NUMPAD_8',
    9: 'NUMPAD_9',
}

addon_keymaps = []


def register():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')

        # Map keys 1-9 to hide_collection operator
        for i in range(1, 10):
            # Regular number keys
            kmi = km.keymap_items.new(
                'object.hide_collection',
                type=NUMBER_KEYS[i],
                value='PRESS',
                ctrl=False,
                shift=False,
                alt=False
            )
            kmi.properties.collection_index = i
            kmi.properties.extend = False
            addon_keymaps.append((km, kmi))

            # Numpad keys
            kmi2 = km.keymap_items.new(
                'object.hide_collection',
                type=NUMPAD_KEYS[i],
                value='PRESS',
                ctrl=False,
                shift=False,
                alt=False
            )
            kmi2.properties.collection_index = i
            kmi2.properties.extend = False
            addon_keymaps.append((km, kmi2))


def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


if __name__ == "__main__":
    register()
    print("Collection Switcher registered! Press 1-9 in 3D Viewport to switch collections.")
