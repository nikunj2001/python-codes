from cx_Freeze import *
includefiles=['bg.ico']
excludes=[]
packages=[]
base = None
if sys.platform=='win32':
    base="Win32GUI"

short_table=[
    ("DesktopShortcut" , 
    'DesktopFolder','Simple Music Player',
    'TARGETDIR',
    "[TARGETDIR]\musicplayer.exe",
    None,
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR"
    )
]
msi_data={"Shortcut": shortcut_table}
setup(
    version=".1",
    name="MUSIC PLAYER",
    executable=[
        Executable(
            script="musicplayer.py",
            base=base,
            icon='bg.ico'
        )
    ]
)