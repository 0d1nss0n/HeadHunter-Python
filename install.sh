# Note: This installer only serves as an installer for HeadHunter on GNU/Linux.
#!/bin/bash
echo "Copying headhunter psudo binary"
cp bin/headhunter /usr/bin
chmod +x /usr/bin/headhunter
echo "Setting execute permissions"
mkdir /usr/share/HeadHunter
cp -r * /usr/share/HeadHunter
echo "Moving headhunter source tree to /usr/share/HeadHunter"
pip install -r requirements.txt
echo "Installing required dependencies"
