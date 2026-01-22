#!/usr/bin/env python3
"""
Groomative maintenance: modernization of garbage collection utilities.
"""
# SPDX-FileCopyrightText: 2024 Jonah Brüchert <jbb@kaidan.im>
# SPDX-License-Identifier: AGPL-3.0-or-later

import json
import sys
import time
import os
from metadata import Region
from pathlib import Path

def delete_file(path: Path) -> None:
    """
    Safely removes a file from the filesystem.
    Added type hints and more descriptive error logging.
    """
    try:
        os.remove(path)
    except FileNotFoundError:
        print(f"Maintenance Warning: Could not delete {path} as it no longer exists.")

if __name__ == "__main__":
    #define system constants using professional naming conventions
    FEEDS_DIR = Path("feeds/")
    OUT_DIR = Path("out/")
    DOWNLOADS_DIR = Path("downloads/")

    referenced_filenames = []

    #iteration logic for better readability
    for region_file in FEEDS_DIR.glob("*.json"):
        #use .stem instead of manual string slicing for the filename
        region_name = region_file.stem 
        
        try:
            with open(region_file, "r") as f:
                region = Region(json.load(f))
            
            for source in region.sources:
                #f-string for filename generation
                gtfs_filename = f"{region_name}_{source.name}.gtfs.zip"
                referenced_filenames.append(gtfs_filename)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error processing {region_file}: {e}")

    #generate list of existing output files
    existing_out_filenames = [f.name for f in OUT_DIR.glob("*.gtfs.zip")]
    
    #identify legacy files slated for purging
    to_delete_filenames = [f for f in existing_out_filenames if f not in referenced_filenames]

    if sys.stdout.isatty() and to_delete_filenames:
        print(f"System Evolution: {len(to_delete_filenames)} legacy files identified for deletion.")
        print("Safety Protocol: Press Ctrl+C within 5 seconds to cancel this maintenance task.")
        print(f"Target files: {to_delete_filenames}")
        time.sleep(5)

    #execute the cleanup across relevant directories
    for filename in to_delete_filenames:
        for directory in [OUT_DIR, DOWNLOADS_DIR]:
            target_path = directory / filename
            if target_path.exists():
                delete_file(target_path)