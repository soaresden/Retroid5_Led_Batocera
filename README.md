# LED Retroid 5 Controller 🎮💡

Simple and elegant LED control system for Retroid Pocket handheld devices.

---

## 📖 English

### What is it? 🤔

LED Retroid 5 Controller lets you customize the LED lights on your Retroid Pocket device in two different ways:

- **JSON Mode** 🎨 - Control individual LED colors for each button
- **Battery Mode** 🔋 - Show battery level through LED colors automatically



### How does it work? ⚙️

**JSON Mode:**
- You run the app and customize each LED's color and brightness
- Your settings are saved in a JSON file
- When you reboot, the colors stay exactly as you left them ✅

**Battery Mode:**
- The app reads your battery percentage
- It automatically changes LED colors based on battery level
- Low battery = red, Full battery = green, etc.

### What you get 📦

```
3 files to copy:
├── ledretroid_JSON.pygame          (Individual LED control app)
├── ledretroid_Battery.pygame       (Battery-based LED app)  
└── ledretroid_JSON_Apply.py        (Auto-apply on boot)
```

### Installation 🚀

**Super easy:**

1. Copy these 3 files into: `roms/pygame/ledretroid/`
2. Done! ✨

That's it. No configuration needed.

### How to use 🎮

**Starting JSON Mode (customize LEDs):**
```
Launch ledretroid_JSON.pygame
↓
Customize your LED colors and brightness
↓
Press START to exit
↓
Colors are saved and persist on reboot ✓
```

**Starting Battery Mode (auto colors):**
```
Launch ledretroid_Battery.pygame
↓
App automatically shows battery level with colors
↓
Colors change as battery drains
```

### Features ✨

- 🎨 **16 colors** to choose from
- 🔆 **Brightness control** for each LED
- 💾 **Auto-save** - settings persist after reboot
- ⚡ **Simple UI** - easy joystick navigation
- 🔄 **Mode switching** - switch between JSON and Battery anytime
- 📊 **Live preview** - see colors change in real-time

### Controls 🕹️

**In JSON Mode:**
- `D-Pad` - Navigate LED selection
- `L/R buttons` - Change color
- `A button` - Increase brightness
- `Y button` - Decrease brightness
- `B button` - Toggle LED on/off
- `START` - Exit and save

**In Battery Mode:**
- Just enjoy the automatic colors!
- `START` to exit

### What happens when you exit? 🔌

**JSON Mode:**
- Your custom colors are saved
- They come back on next reboot ✓

**Battery Mode:**
- Battery config is saved
- LEDs will show battery level next time
- Custom.sh is removed (won't interfere with JSON)

### Troubleshooting 🔧

**LEDs not showing my colors?**
- Make sure you saved before exiting (Press START)
- Colors will appear on next reboot

**Can't switch between modes?**
- Exit the current mode completely (Press START)
- Then launch the other mode
- It will handle the switch automatically

**Colors look dim?**
- Increase brightness with A button
- Brightness is saved too!

---

## 📖 Français

### C'est quoi? 🤔

LED Retroid 5 Controller vous permet de personnaliser les LEDs de votre Retroid Pocket de deux façons différentes:

- **Mode JSON** 🎨 - Contrôlez chaque couleur de LED individuellement
- **Mode Batterie** 🔋 - Affichage automatique du niveau de batterie par les LEDs

### Comment ça marche? ⚙️

**Mode JSON:**
- Vous lancez l'app et personnalisez la couleur et luminosité de chaque LED
- Vos paramètres sont sauvegardés dans un fichier JSON
- Au redémarrage, les couleurs restent exactement comme vous les avez laissées ✅

**Mode Batterie:**
- L'app lit le pourcentage de batterie
- Elle change automatiquement les couleurs des LEDs selon le niveau
- Batterie faible = rouge, Batterie pleine = vert, etc.

### Ce que vous obtenez 📦

```
3 fichiers à copier:
├── ledretroid_JSON.pygame          (Contrôle individuel des LEDs)
├── ledretroid_Battery.pygame       (LEDs basées sur la batterie)  
└── ledretroid_JSON_Apply.py        (Auto-apply au démarrage)
```

### Installation 🚀

**Super simple:**

1. Copiez ces 3 fichiers dans: `roms/pygame/ledretroid/`
2. C'est tout! ✨

Zéro configuration nécessaire.

### Comment utiliser 🎮

**Démarrer le Mode JSON (personnaliser les LEDs):**
```
Lancez ledretroid_JSON.pygame
↓
Personnalisez vos couleurs et luminosité
↓
Appuyez sur START pour quitter
↓
Les couleurs sont sauvegardées et persistent au redémarrage ✓
```

**Démarrer le Mode Batterie (couleurs auto):**
```
Lancez ledretroid_Battery.pygame
↓
L'app affiche automatiquement le niveau de batterie avec les couleurs
↓
Les couleurs changent à mesure que la batterie se décharge
```

### Fonctionnalités ✨

- 🎨 **16 couleurs** à choisir
- 🔆 **Contrôle de luminosité** pour chaque LED
- 💾 **Auto-save** - paramètres persistent après redémarrage
- ⚡ **Interface simple** - navigation facile au joystick
- 🔄 **Changement de mode** - basculez entre JSON et Batterie facilement
- 📊 **Aperçu en direct** - voyez les couleurs changer en temps réel

### Contrôles 🕹️

**En Mode JSON:**
- `D-Pad` - Sélectionner une LED
- `Boutons L/R` - Changer de couleur
- `Bouton A` - Augmenter la luminosité
- `Bouton Y` - Diminuer la luminosité
- `Bouton B` - Activer/Désactiver la LED
- `START` - Quitter et sauvegarder

**En Mode Batterie:**
- Profitez simplement des couleurs automatiques!
- `START` pour quitter

### Que se passe-t-il quand vous quittez? 🔌

**Mode JSON:**
- Vos couleurs personnalisées sont sauvegardées
- Elles réapparaissent au redémarrage ✓

**Mode Batterie:**
- La config batterie est sauvegardée
- Les LEDs afficheront le niveau de batterie la prochaine fois
- custom.sh est supprimé (n'interfère pas avec JSON)

### Dépannage 🔧

**Les LEDs ne montrent pas mes couleurs?**
- Assurez-vous d'avoir sauvegardé avant de quitter (Appuyez sur START)
- Les couleurs apparaîtront au prochain redémarrage

**Je ne peux pas basculer entre les modes?**
- Quittez complètement le mode actuel (Appuyez sur START)
- Puis lancez l'autre mode
- Il gérera automatiquement le changement

**Les couleurs semblent ternes?**
- Augmentez la luminosité avec le bouton A
- La luminosité est aussi sauvegardée!

---

## 📁 File Structure / Structure des fichiers

```
roms/
└── pygame/
    └── ledretroid/
        ├── ledretroid_JSON.pygame
        ├── ledretroid_Battery.pygame
        └── ledretroid_JSON_Apply.py
```

---

## 🔄 Mode Switching / Changement de mode

- **JSON → Battery:** Exit JSON (START), launch Battery
- **Battery → JSON:** Exit Battery (START), launch JSON
- **Automatic:** Custom.sh is created/deleted automatically

---

## 💡 Tips & Tricks

- Change LED colors in real-time to test!
- Use brightness to make colors pop
- Toggle LEDs on/off if you don't need all of them
- Battery mode is totally automatic - no tweaking needed

---

## 🎨 Colors Available / Couleurs disponibles

Red • Orange • Yellow • Green • Cyan • Blue • Purple • Magenta ... and 8 more variations!

---

**Enjoy your custom LED setup!** 🎉

Made for Retroid Pocket with ❤️