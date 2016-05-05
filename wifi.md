# WiFi

We got WiFi to work using the patches found [here](https://github.com/hadess/rtl8723bs), though for some reason, the patches won't work with kernel 4.5 or higher.

For the time being, we're using Kernel 4.8.8 with a modified version of the patches. They can be found in wifi/, along with a PKGBUILD for Arch Linux. If you're not an Arch user, get the kernel sources for 4.8.8 from <kernel.org> and apply the patches manually.
