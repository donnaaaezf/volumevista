import ctypes
from ctypes import wintypes
import sys
import os

class VolumeVista:
    def __init__(self):
        self._get_volume_control_interface()

    def _get_volume_control_interface(self):
        self._volume_control = ctypes.windll.user32
        self._volume_control.RegisterHotKey(None, 1, 0x0000, 0xAF)  # VK_VOLUME_MUTE
        self._volume_control.RegisterHotKey(None, 2, 0x0000, 0xAE)  # VK_VOLUME_DOWN
        self._volume_control.RegisterHotKey(None, 3, 0x0000, 0xAF)  # VK_VOLUME_UP

    def run(self):
        try:
            msg = wintypes.MSG()
            while ctypes.windll.user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == 0x0312:  # WM_HOTKEY
                    if msg.wParam == 1:
                        self._toggle_mute()
                    elif msg.wParam == 2:
                        self._adjust_volume(-5)
                    elif msg.wParam == 3:
                        self._adjust_volume(5)
                ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
                ctypes.windll.user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            self._cleanup()

    def _toggle_mute(self):
        os.system("nircmd.exe mutesysvolume 2")

    def _adjust_volume(self, change):
        os.system(f"nircmd.exe changesysvolume {change * 655}")

    def _cleanup(self):
        self._volume_control.UnregisterHotKey(None, 1)
        self._volume_control.UnregisterHotKey(None, 2)
        self._volume_control.UnregisterHotKey(None, 3)
        print("Cleaned up hotkeys.")

if __name__ == "__main__":
    if not os.path.exists("nircmd.exe"):
        print("Error: 'nircmd.exe' is required to run this program. Please download it from https://www.nirsoft.net/utils/nircmd.html")
        sys.exit(1)
        
    volume_vista = VolumeVista()
    volume_vista.run()