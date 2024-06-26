import os
import yaml

folder_path = "./Testpurpose"
sidebar_path = "./_data/sidebars/mydoc_sidebar.yml"

def update_sidebar(folder_path, sidebar_path):
    # Get a list of files in the folder
    files = os.listdir(folder_path)
    print("Files in folder:", files)

    # Update the sidebar configuration
    with open(sidebar_path, 'r') as f:
        sidebar = yaml.safe_load(f)
    print("Original sidebar content:", sidebar)

    # Append new items to the sidebar
    for file in files:
        # Create a dictionary for the new item
        new_item = {"title": file, "url": f"/pages/Testpurpose/{file}", "output": "web, pdf"}

        # Append the new item to the appropriate section
        sidebar['entries'][-1]['folders'][-1]['folderitems'].append(new_item)

    # Save the updated sidebar
    with open(sidebar_path, 'w') as f:
        yaml.dump(sidebar, f, default_flow_style=False)
    print("Updated sidebar content:", sidebar)
    print("Sidebar updated and saved successfully.")

update_sidebar(folder_path, sidebar_path)
