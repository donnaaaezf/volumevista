# VolumeVista

VolumeVista is a Python-based application that provides volume and sound management tools, enhancing audio control capabilities on Windows systems.

## Features

- **Mute/Unmute**: Quickly toggle mute status on your system.
- **Volume Up/Down**: Adjust the system volume with ease.

## Requirements

- Windows operating system
- Python 3.x
- `nircmd.exe` utility from NirSoft (download it from [NirSoft](https://www.nirsoft.net/utils/nircmd.html))

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/VolumeVista.git
   ```

2. **Navigate into the directory:**

   ```bash
   cd VolumeVista
   ```

3. **Ensure `nircmd.exe` is in the same directory as `volume_vista.py`.**

## Usage

Run the script using Python:

```bash
python volume_vista.py
```

Once running, use the following hotkeys:

- **Mute/Unmute**: Your system's mute hotkey
- **Volume Down**: Your system's volume down hotkey
- **Volume Up**: Your system's volume up hotkey

## Notes

- The application depends on `nircmd.exe` for volume controls. Make sure it's downloaded and placed correctly.
- The hotkeys are registered using the `user32.dll` library.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Thanks to NirSoft for providing `nircmd.exe` utility.
```

Note: The program uses `nircmd.exe`, a command-line utility from NirSoft, to manage volume controls. Please ensure to download it and place it in the same directory as the script for it to work correctly.