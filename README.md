# 🎮 Retroid 5 LED Controller

## ✨ Overview
A pygame-based LED controller for Retroid Pocket 5 that lets you customize button LEDs with custom colors and brightness. The app automatically installs a Batocera service to persist your settings across reboots.

## 🚀 Features
- 🎨 16 vibrant colors to choose from
- 💾 Auto-save configuration to JSON
- 🔧 Parent-child LED hierarchy (control groups or individual buttons)
- 🎯 Real-time LED updates
- 🤖 Automatic Batocera service installation
- 📊 Clean configuration file format

## 📋 Installation

1. Copy both files to your Retroid:
```bash
mkdir -p /userdata/roms/pygame/ledretroid/
cp led_controller.py /userdata/roms/pygame/ledretroid/
```

2. Launch from Batocera: **Games → Pygame → led_controller**
   - First launch auto-installs the service ✅

## 🎮 Controls
- **D-Pad** = Navigate
- **A** = Change brightness
- **B** = Enable/Disable LED
- **L/R** = Change color
- **START** = Save & Exit

## 📁 Configuration
Config is stored at: `/userdata/roms/pygame/ledretroid/colorsave.json`
```json
{
  "Left Joystick": {
    "L1_Right": {"enabled": true, "color": "#FF0000", "brightness": 255},
    ...
  },
  "Controls": {
    "LEFT": {"color": "#0000FF", "brightness": 100},
    ...
  }
}
```

## 🔧 How it Works
- Reads/writes LED config from JSON
- Controls LEDs via sysfs (`/sys/class/leds/`)
- Service disables Batocera LED daemon to avoid conflicts
- Parent controls (LEFT/RIGHT/BOTH) override child LEDs

## ⚙️ Technical Details
- Written in Python 3 + Pygame
- No external dependencies beyond Pygame
- Auto-disables `batocera-led-handheld` daemon
- Service auto-starts on boot

---
Made with ❤️ for Retroid Pocket 5 enthusiasts
```

Et pour le message Discord/community :
```
🎮 **Small Contribution for Retroid 5 LED Management!** 🎮

Hey everyone! 👋 I just created a Pygame LED controller for the Retroid Pocket 5. 

✨ What it does:
🎨 Customize button LED colors from 16 different hues
💾 Auto-saves settings to JSON (survives reboots!)
🎯 Control individual LEDs or groups
🤖 Automatically installs a Batocera service

🚀 Features:
✅ Real-time LED updates
✅ Clean JSON config format
✅ Parent-child LED hierarchy
✅ Dead simple to use

📝 Usage:
- Just copy 2 files + launch the pygame
- First run auto-installs the service
- Use D-Pad to navigate, buttons to change colors/brightness

🙏 Built with AI assistance but thoroughly tested on my own device. Works great! Probably room for improvement, but very functional as-is.

Anyone interested? Happy to take feedback! 🤗

#RetroidPocket5 #LEDCustomization #Pygame