# PyDrum
PyDrum transform your GuitarHero® Drum in a real electronic drum.

## Installation
To read the USB devices, copy the udev rule to the directory 
`/lib/udev/rules.d/`, and install the `pyusb` and mplayer requirement.

    $ cp conf/50-pydrum.rules /lib/udev/rules.d/
    $ sudo pip3 install pyusb
    $ sudo apt-get install mplayer


## Running
Plug the USB of GuitarHero® Drum and run the PyDrum script.

    $ python3 pydrum.py

## Demo
Click bellow and see this in action.

[Youtube Video](http://www.youtube.com/watch?v=Lw94ewgFMDo)
[![PyDrum Example](http://img.youtube.com/vi/Lw94ewgFMDo/0.jpg)](http://www.youtube.com/watch?v=Lw94ewgFMDo)

## TODO

- Improvement the Drum parts sounds.
