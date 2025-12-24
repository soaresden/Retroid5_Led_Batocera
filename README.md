# Retroid Pocket 5 LED Controller

Advanced LED configuration system for Retroid Pocket 5 handheld devices running Batocera. Display battery levels and achievements through customizable RGB LED effects.

## Features

- 🔋 **Battery-Aware LED Control** - Dynamic LED colors based on current battery percentage
- 🎨 **Multiple Effect Modes** - Color, PULSE, RAINBOW, and OFF modes
- 🔅 **Brightness Control** - Adjustable brightness from 0-100%
- 🎮 **Interactive UI** - Intuitive gamepad controls for configuration
- 💾 **Persistent Configuration** - Save and load LED settings from `/userdata/system/configs/leds.conf`
- ⚙️ **JSON Mode Support** - Alternative JSON-based configuration system
- 🔄 **Headless Service** - Background daemon for automatic LED management
- 🌈 **Achievement Integration** - Special LED effects when unlocking RetroAchievements

## Architecture

### Three-App System

1. **ledretroid_Battery.py** - Interactive Battery Mode UI
   - Full-featured configuration editor
   - Real-time LED preview
   - Gamepad-based controls
   - Visual battery level simulator

2. **ledretroid_JSON.py** - JSON Mode UI
   - Alternative configuration format
   - JSON file-based settings

3. **ledretroid_Battery_Apply.py** - Headless Service
   - Runs in background
   - Reads config and applies LED colors
   - No UI, pure daemon functionality

## Configuration File

Edit `/userdata/system/configs/leds.conf`:

```
5=PULSE
10=FF0000
15=FF4000
30=050300
50=000500
100=RAINBOW
```

### Format: `battery_level=value`

**battery_level**: 0-100 (percentage)

**value**: Either
- **Hex Color**: `RRGGBB` (e.g., `FF0000` for red)
- **Effect Mode**: `PULSE`, `RAINBOW`, `OFF`

### Behavior

- Colors/modes apply to all battery levels >= their threshold
- Zone 0% to first point inherits first point's mode + closest color
- When battery reaches 100% (charging), special effects trigger
- `PULSE`: Breathing effect with dimming
- `RAINBOW`: Cycling through color spectrum
- `OFF`: LEDs turn off

## Installation

1. Clone repository:
```bash
git clone https://github.com/yourusername/Retroid5_Led_Batocera
cd Retroid5_Led_Batocera
```

2. Copy files to Batocera:
```bash
# Battery Mode (Interactive)
cp ledretroid_Battery.py /userdata/roms/pygame/ledretroid/

# Service (Auto-start)
cp ledretroid_Battery_Apply.py /userdata/system/services/
```

3. Create config directory:
```bash
mkdir -p /userdata/system/configs
```

4. Create initial config:
```bash
cat > /userdata/system/configs/leds.conf << 'EOF'
0=PULSE
5=FF0000
10=CC3333
15=FF7F00
100=009900
EOF
```

## Usage

### Interactive Mode

Launch from Batocera menu:
```
Pygame > ledretroid_Battery
```

### Controls

| Button | Action |
|--------|--------|
| **D-Pad Left/Right** | Move battery slider (±5%) |
| **L/R Bumpers** | Cycle color selector (16 colors) |
| **Y** | Decrease brightness (hold: accelerate) |
| **A** | Increase brightness (hold: accelerate) |
| **B** | Add point at slider with selected color/mode |
| **X** | Remove closest point to slider |
| **SELECT** | Cycle effect mode (Color → PULSE → RAINBOW → OFF) |
| **START** | Exit menu dialog |

### UI Layout

**Top Section:**
- Battery level indicator (0-100%)
- Main LED effect preview bar (animated)
- Point markers with current mode effects

**Middle Section:**
- Brightness slider & percentage
- Preview color box
- Battery points list with hex values

**Bottom Section:**
- Color selector palette (16 predefined colors)
- Visual brightness range (25%-100% for visibility)

## Headless Service

Auto-apply LED colors in background without UI:

```bash
systemctl start led_retroid_5_battery
systemctl enable led_retroid_5_battery
```

Logs to: `/userdata/system/logs/ledretroid5.log`

## API / Manual Control

Control LEDs from command line:

```bash
# Set solid color (RGB values 0-255)
/usr/bin/batocera-led-handheld set_color_dec 255 0 0

# Trigger rainbow effect
/usr/bin/batocera-led-handheld rainbow

# Pulse effect
/usr/bin/batocera-led-handheld pulse

# Turn off
/usr/bin/batocera-led-handheld off

# Get current color
/usr/bin/batocera-led-handheld get_color

# Set brightness (0-100)
/usr/bin/batocera-led-handheld set_brightness 50
```

## RetroAchievement Integration

Trigger LED effects when unlocking achievements:

```bash
mkdir -p /userdata/system/configs/emulationstation/scripts/achievements/
echo "#!/bin/bash" > /userdata/system/configs/emulationstation/scripts/achievements/leds.sh
echo "/usr/bin/batocera-led-handheld rainbow" >> /userdata/system/configs/emulationstation/scripts/achievements/leds.sh
chmod +x /userdata/system/configs/emulationstation/scripts/achievements/leds.sh
```

## Color Reference

### Predefined Colors (16)

| Index | Name | Hex |
|-------|------|-----|
| 0 | Red | FF0000 |
| 1 | Red-Orange | FF4000 |
| 2 | Orange | FF7F00 |
| 3 | Orange-Yellow | FFBF00 |
| 4 | Yellow | FFFF00 |
| 5 | Yellow-Green | BFFF00 |
| 6 | Lime | 7FFF00 |
| 7 | Green | 00FF00 |
| 8 | Green-Cyan | 00FF7F |
| 9 | Cyan-Green | 00FFBF |
| 10 | Cyan | 00FFFF |
| 11 | Blue | 0000FF |
| 12 | Blue-Purple | 7F00FF |
| 13 | Purple | BF00FF |
| 14 | Magenta | FF00BF |
| 15 | Magenta-Red | FF0040 |

### Battery Color Examples

```
# Low battery = Red warning
5=FF0000

# Medium battery = Orange
30=FF7F00

# High battery = Green
70=00FF00

# Charging = Rainbow cycling
100=RAINBOW
```

## Brightness & Display

- **Actual Brightness**: 0-255 (0% = off, 100% = full)
- **Visual Display**: 25%-100% minimum (for UI visibility)
  - 0% actual → shows as 25% in UI
  - 100% actual → shows as 100% in UI
- **LED Hardware**: Always uses real brightness value

## File Structure

```
Retroid5_Led_Batocera/
├── ledretroid_Battery.py          # Interactive UI
├── ledretroid_JSON.py             # JSON config mode
├── ledretroid_Battery_Apply.py    # Headless service
├── batoled.py                     # LED hardware interface
└── README.md
```

## Requirements

- Batocera Linux on Retroid Pocket 5
- Python 3.7+
- Pygame
- `/sys/class/leds/` hardware access

## Troubleshooting

### LEDs not responding
1. Check `/sys/class/leds/` exists:
   ```bash
   ls /sys/class/leds/
   ```
2. Verify permissions (should be writable as root)
3. Check logs:
   ```bash
   tail -f /userdata/system/logs/ledretroid5.log
   ```

### Config not loading
1. Verify file path: `/userdata/system/configs/leds.conf`
2. Check syntax (battery% = value, one per line)
3. Validate hex colors (6 characters, 0-F)

### UI freezing
1. Ensure joystick is detected
2. Check for Python errors in logs
3. Restart pygame service

### Brightness not changing
1. Verify brightness control is enabled in device tree
2. Check `/sys/class/leds/` file permissions
3. Test manual brightness:
   ```bash
   echo 128 > /sys/class/leds/r:r1/brightness
   ```

## Contributing

Contributions welcome! Please submit:
- Bug reports with logs
- Feature requests with examples
- Configuration examples for specific games/themes

## License

MIT License - See LICENSE file

## Credits

Written for Batocera - @lbrpdx
Enhanced LED configuration system for Retroid Pocket 5

---

**Last Updated**: 25 December 2025
**Tested On**: Batocera on Retroid Pocket 5