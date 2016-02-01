# PyQtBoilerPlate
testing out PyQT trying to figure it out


Tyring to get a feel for how to use PyQt 5
in order to do this you need the pyuic5 tool installed:
    sudo apt-get install pyqt5-dev-tools
    
To get the QT designer:
    sudo apt-get install qttools5-dev-tools
    
You can run the designer by:
    /usr/lib/x86_64-linux-gnu/qt5/bin/designer
    
You can design the UI anyway you want in the designer, then you will have the <name>.ui file
next run pyuic5 tool:
    pyuic5 <name>.ui > <name>.py
    
Then you can mess with your logic file after inporting the ui .py file. See code for example

