#!/usr/bin/env python3
"""
LED Retroid 5 - Headless JSON LED Applicator
Applies LEDs from JSON config WITHOUT GUI
Used by service to maintain LED state
"""
import json
import sys
import os

def apply_json_leds():
    """Apply LEDs from JSON config - pure headless, no pygame"""
    try:
        json_file = '/userdata/roms/pygame/ledretroid/colorsave.json'
        
        if not os.path.exists(json_file):
            print(f"Error: {json_file} not found", file=sys.stderr)
            return 1
        
        with open(json_file, 'r') as f:
            config = json.load(f)
        
        # Just load and verify - actual LED application is handled by daemon
        # when block file is present
        print(f"✓ JSON loaded: {len([k for k,v in config.items() if isinstance(v, dict)])} LEDs")
        return 0
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(apply_json_leds())