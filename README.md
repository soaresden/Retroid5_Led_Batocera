# 🎮 Retroid Pocket 5 LED Controller

## 📸 Preview
![LED Retroid Controller](screenshot.png)

A comprehensive pygame-based LED controller for the Retroid Pocket 5 handheld console, featuring dual-mode operation for individual LED control and battery-based LED effects.

## Features

### 🎮 Dual-Mode Operation

#### **JSON Mode** - Individual LED Control
- Control 8 individual LEDs (L1-L4, R1-R4) independently
- Parent-child hierarchy: BOTH → LEFT/RIGHT → Individual LEDs
- Real-time intensity adjustment (0-255 levels)
- 16-color palette with visual preview
- Disabled LED state management
- Joystick color visualization showing combined LED output

#### **BATTERY Mode** - Battery-Level-Based LED Effects
- Define LED effects at specific battery percentage thresholds
- Supports hex colors, PULSE, RAINBOW, and OFF effects
- Real-time brightness control (0-255)
- Live LED preview with color/brightness adjustment
- Visual battery slider with color gradients
- Simulation mode to preview effects at different battery levels
- Zone-based effect removal (remove effect from current battery range)

### 🎨 Visual Feedback

- **Color Bar**: 16 colors for easy selection
- **Battery Slider**: Color-coded visualization showing active effects at each battery level
- **Joystick Circles**: Real-time LED color preview (JSON mode and battery mode)
- **Live LED Apply**: See changes on device LEDs as you adjust settings
- **UI Overlays**: Visual indicators for simulation mode

### ⚡ Control Features

- **Hardware LED Integration**: Changes apply live to device LEDs
- **Real-Time Save**: All changes saved immediately to config files
- **Long-Press Acceleration**: Quick adjustments with held button presses
- **Wrap-Around Navigation**: Seamless color/effect cycling

## Installation

### Prerequisites
- Batocera OS on Retroid Pocket 5
- Python 3
- Pygame 2.5+

### Setup

1. **Copy the script** to your Retroid Pocket 5:
```bash
/userdata/roms/pygame/ledretroid/led_retroid.pygame
```

2. **Create the config directory**:
```bash
mkdir -p /userdata/system/configs
```

3. **Optional: Create initial battery config** (`/userdata/system/configs/leds.conf`):
```
20=FF0000
30=FF7F00
50=PULSE
85=00FF00
```

The service will auto-register on first launch.

## Controls

### Mode Switching
- **SELECT**: Switch between JSON and BATTERY modes

### JSON Mode (Individual LED Control)

| Button | Action |
|--------|--------|
| **Dpad** | Navigate LED grid |
| **L/R** | Change LED color (wrap-around) |
| **A** | Increase brightness (hold for acceleration) |
| **Y** | Decrease brightness (hold for acceleration) |
| **B** | Toggle LED disabled state |
| **START** | Exit (no reboot) |
| **SELECT** | Switch to BATTERY mode |

### BATTERY Mode (Battery-Level Effects)

#### Edit Mode
| Button | Action |
|--------|--------|
| **Dpad L/R** | Move battery slider (0-100%) |
| **Dpad Up/Down** | Adjust brightness (0-255) |
| **X** | Loop through effects (Color/PULSE/RAINBOW/OFF) |
| **L/R** | Change color (when Color effect selected) |
| **A** | Add/update effect at current battery level |
| **B** | Remove effect from current battery zone |
| **Y** | Enter simulation mode |
| **START** | Exit (shows reboot dialog) |
| **SELECT** | Switch to JSON mode |

#### Simulation Mode
| Button | Action |
|--------|--------|
| **Dpad L/R** | Simulate battery level change |
| **Dpad Up/Down** | Adjust brightness preview |
| **Y** | Exit simulation, return to edit |

## Configuration Files

### JSON Mode: `colorsave.json`
Location: `/userdata/roms/pygame/ledretroid/colorsave.json`

```json
{
  "Left Joystick": {
    "L1_Right": {
      "enabled": true,
      "color": "#FF0000",
      "brightness": 100
    },
    ...
  },
  "Right Joystick": { ... },
  "Controls": {
    "LEFT": { "color": "#FF0000", "brightness": 100 },
    "RIGHT": { "color": "#00FF00", "brightness": 100 },
    "BOTH": { "color": "#0000FF", "brightness": 100 }
  }
}
```

### BATTERY Mode: `leds.conf`
Location: `/userdata/system/configs/leds.conf`

Format: `battery_percentage=effect`
- No spaces around `=`
- Battery percentages: 0-100
- Effects: hex color (6 digits, e.g., `FF0000`), `PULSE`, `RAINBOW`, `OFF`

```
10=FF0000
20=FF7F00
30=FFFF00
50=00FF00
85=0000FF
```

**Color Interpolation**: If your battery is at 75%, it uses the highest effect ≤ 75% (in this example, 50=00FF00)

## LED Hardware Layout

### Physical Layout (Diamond Pattern)
```
        L1
    L3      L2
        
    R3      R2
        R1
        R4
```

### Hardware Paths
- Left Joystick: `/sys/class/leds/l:r{1-4}/brightness` (Red, Green, Blue for L1-L4)
- Right Joystick: `/sys/class/leds/r:r{1-4}/brightness` (Red, Green, Blue for R1-R4)

### Hierarchy
- **BOTH** (index 10): Controls all 8 LEDs
- **LEFT** (index 8): Controls L1-L4
- **RIGHT** (index 9): Controls R1-R4
- **Individual LEDs** (indices 0-7): L1, L2, L3, L4, R1, R2, R3, R4

## Color Palette

16 predefined colors for easy selection:

| # | Name | RGB | Hex |
|---|------|-----|-----|
| 0 | Red | 255, 0, 0 | `FF0000` |
| 1 | RedOrange | 255, 64, 0 | `FF4000` |
| 2 | Orange | 255, 127, 0 | `FF7F00` |
| 3 | OrangeYellow | 255, 191, 0 | `FFBF00` |
| 4 | Yellow | 255, 255, 0 | `FFFF00` |
| 5 | YellowGreen | 191, 255, 0 | `BFFF00` |
| 6 | Lime | 127, 255, 0 | `7FFF00` |
| 7 | Green | 0, 255, 0 | `00FF00` |
| 8 | GreenCyan | 0, 255, 127 | `00FF7F` |
| 9 | CyanGreen | 0, 255, 191 | `00FFBF` |
| 10 | Cyan | 0, 127, 255 | `007FFF` |
| 11 | Blue | 0, 0, 255 | `0000FF` |
| 12 | BluePurple | 127, 0, 255 | `7F00FF` |
| 13 | Purple | 191, 0, 255 | `BF00FF` |
| 14 | Magenta | 255, 0, 191 | `FF00BF` |
| 15 | MagentaRed | 255, 0, 64 | `FF0040` |

## Brightness Levels

35 intensity levels available for smooth transitions:
```
0, 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 255
```

## Service Management

The controller auto-installs a Batocera service at:
```
/userdata/system/services/retroid5_led
```

Service commands:
```bash
batocera-services enable retroid5_led
batocera-services start retroid5_led
batocera-services stop retroid5_led
batocera-services status retroid5_led
```

## Logging

Application logs are written to:
```
/tmp/led_controller.log
```

Check logs to debug issues:
```bash
tail -f /tmp/led_controller.log
```

## Tips & Tricks

### JSON Mode Tips
- **Parent Control**: Adjust BOTH, LEFT, or RIGHT to change multiple LEDs at once
- **Color Preview**: The joystick circles show the combined color output in real-time
- **Disabled LEDs**: Red X marks disabled LEDs (saved state persists)

### Battery Mode Tips
- **Create Gradients**: Set different colors at multiple battery levels for smooth gradients
- **Simulation Mode**: Preview how effects look at different battery percentages without affecting the device
- **Brightness Adjustment**: Use Up/Down while on battery slider to dim/brighten effects
- **Zone Remove**: You don't need to position exactly on a point to remove it; B button removes the effect in your current zone

### Workflow
1. Start in **JSON Mode** to test individual LED placement
2. Switch to **BATTERY Mode** to create progressive effects
3. Use **Simulation Mode** to preview battery transitions
4. **Save and exit**
5. **Reboot** when prompted (required for battery mode to take effect)

## Troubleshooting

### LEDs Not Responding
- Check `/tmp/led_controller.log` for errors
- Verify `/sys/class/leds/` paths exist
- Ensure Batocera service is running: `batocera-services status retroid5_led`

### Battery Mode Not Working After Exit
- **Reboot is required!** When exiting battery mode, accept the reboot dialog
- Without reboot, changes won't apply to the system

### Changes Not Saving
- Check file permissions on `/userdata/` directories
- Ensure disk space is available
- Check logs for write errors

### Colors Look Wrong
- LED brightness caps at 255 RGB (0-255 per channel)
- Brightness adjustment in battery mode affects RGB output
- Verify color values in config files are valid hex (6 digits)

## Development

### Project Structure
```
led_retroid.pygame          # Main application script
colorsave.json              # JSON mode config (auto-created)
/userdata/system/configs/
  └─ leds.conf              # Battery mode config (auto-created)
```

### Contributing
Feel free to fork and submit pull requests for:
- UI improvements
- New effects
- Hardware optimizations
- Bug fixes

## License

MIT License - See LICENSE file for details

## Credits

Built for the Retroid Pocket 5 community to enhance LED customization and control.

---

**Happy LED customizing! 🎨✨**

For issues, feature requests, or questions, please open an issue on GitHub.
