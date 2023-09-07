# AutoOrg (v1.0)

# Function:

AutoOrg - constantly runs.

1. Checks the default Downloads folder for audio, image, video files.
2. Moves the files to default Music, Pictures and Videos respectively.
3. Runs in the background and constatly moves the files as they're coming in (manually moving a file into Downloads, downloading from a browser, taking screenshots in a browser)

AutoOrg Once - runs once.

1. Checks the default Downloads folder for audio, image, video files.
2. Moves the files to default Music, Pictures and Videos respectively.
3. Program closes once the process has been completed.

# Setup:
1. AutoOrg v1.0 setup<br />
   -Run setup.<br />
   -Copy shortcut.<br />
   -[Win] + [R]<br />
   -Type "shell:startup" and hit [Enter]<br />
   -Paste shortcut.<br />
   -Restart<br />
   
2. AutoOrg Oncev1.0 setup<br />
  -Run Setup<br />
  -Start program.<br />

   
# Problem(s):

1. Not adapted for iOS
2. Windows defender detects program as trojan
3. Not tested on Windows 11

# Additional:

1. Script written with the help of GPT-3.5 and BingAI
2. Icon changed via Resource Hacker
3. .py script turned into .exe via cmd command - pyinstaller --onefile --noconsole AutoBin.py
4. .exe compiled into a setup file via InstallForge
