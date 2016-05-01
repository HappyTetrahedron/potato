# How to get the touchscreen working on a potato

There are two relevant github repositories: 
* <https://github.com/onitake/gslx680-acpi>
* <https://github.com/onitake/gsl-firmware>

The first contains a driver for the Silead GSLx68 touchscreen series.  The
second contains firmware for various specific devices, including potatos.  The
firmware is required in order for the driver to work.

## Install the firmware 

Clone the firmware git repository. It contains two directories, tools and
firmware.  In the tools directory, the fwtool can be found, which can convert
the included firmware for potato to a format the driver understands. The
firmware for potato resides in

    firmware/trekstor/surftab7old/SurfTab_wintron_7-0_Windows_Driver-Package/TP/

Navigate to tools/, then run as root:

    ./fwtool -c ../firmware/trekstor/surftab7old/SurfTab_wintron_7-0_Windows_Driver-Package/TP/GSL_TS_CFG.h -2 -m 1680 -w 1024 -h 600 -t 10 -f track /lib/firmware/silead_ts.fw

This is the command stated in TobleMiner's tutorial, except with the corrected
file path. It converts the firmware and places it in the correct directory. It also enables in-driver finger tracking which is required for multitouch.

If you plan to use your potato in portrait mode, you will have to change "-f track" to "-f track,swap" to swap the x and y axis. When you rotate the screen, the touchscreen won't be automatically rotated with it. With this driver, you can have either portrait or landscape.

It might be possible to swap the axes dynamically with some higher level driver, I haven't looked into that yet.

## Install the driver 

Switch to the other git repository. Make sure you have the kernel headers
installed (package linux-headers). Run "make".

Once make completes, the file gslx680_ts_acpi.ko will be created. To test
whether everything works, run as root:

    insmod gslx680_ts_acpi.ko

This loads the driver kernel module.

Then, (re)start X and verify the touchscreen works.

### Automatically load the driver on boot

*Disclaimer: I'm writing this up from memory and I'm completely unsure whether this is correct*

To automatically load the kernel module on boot, copy the .ko file to /lib/modules/extramodules<kernelversion>/
Then, go to /lib/modprobe.d and create a new text file named
"gslx680_ts_acpi.conf" containing the following line:

insmod /lib/modules/extramodules<kernelversion>/gslx680_ts_acpi.ko

## Calibrate 

The touchscreen still needs some calibration once it works. To do that, install
xinput_calibrator from the AUR. Run xinput_calibrator from a terminal and
follow the instructions. Once completed, the calibrator will output some
configuration options in the terminal. These can be copied over to a new file
/etc/X11/xorg.conf.d/99-calibration.conf in order to make the calibration
permanent.

Congratulations, your potato now has a working touchscreen!

Now you can, for example, use touchegg to configure multitouch gestures or install onboard as a keyboard replacement.
