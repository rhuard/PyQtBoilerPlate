# PyQtBoilerPlate
testing out PyQT trying to figure it out


Tyring to get a feel for how to use PyQt 5

As a heads up, especally with the naming of menu items in the menu bar, I did not use good naming conventions. One day I will probably change that.
For now it may be a little confusing and for that I applogize, but this was a really hacked together project to get some boiler plate running. The boiler
plate being the code in the Run.py. the UI.py was just something to test on.

in order to do this you need the pyuic5 tool installed:
    ```
    sudo apt-get install pyqt5-dev-tools
    ```
    
To get the QT designer:
    ```
    sudo apt-get install qttools5-dev-tools
    ```
    
You can run the designer by:
    ```
    /usr/lib/x86_64-linux-gnu/qt5/bin/designer
    ```
If you are on a 32 bit system it should be:
    ```
    /usr/lib/i386-linux-gnu/qt5/bin/designer
    ```
    
    
You can design the UI anyway you want in the designer, then you will have the <name>.ui file
next run pyuic5 tool:
    ```
    pyuic5 <name>.ui > <name>.py
    ```
    
Then you can mess with your logic file after inporting the ui .py file. See code for example


Also note: the main reason to use this boilerplate is because when you run pyuic5 the UI.py file will not be runable.
Either you need to modify the file or do something like what I did in the run.py file. I chose not to modify the file
because the UI.py is autogenerated and anytime you change the .ui file and run pyuic it will overwrite your changes and I am
lazy. With the method I used you can autogenerate and change the .ui file as much as you want and you will not need to change
run file to make it work.



This is for Qt 5 using Qt 5 designer and Python 3


In the future there will be one python 2 and Qt 4
