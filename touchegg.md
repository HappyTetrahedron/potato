# Install and configure touchegg on potato

Touchegg is a software that enables gesture support for the touchscreen (things like pinching and dragging with one or more fingers). I had some trouble getting it to work, but this is (probably) more of a problem with arch and not so much with potato. Nevertheless, here's what I did:

Touchegg is available in the AUR. It does, however, not compile. To get it to do so, I had to install xorg-server-devel-dev from AUR. This took ages to compile on potato, so it might be a good idea to compile the package on a different machine and copy the package over.

After xorg-server-devel-dev is installed, you can install touchegg (I recommend using an AUR helper as touchegg depends on several other AUR packages which again depend on AUR packages...). It should compile successfully.

A sample configuration file is provided. Documentation can be found [here](https://github.com/JoseExposito/touchegg/wiki/All-gestures-supported-by-Touch%C3%A9gg).

# Review

* Tapping and dragging is recognized pretty reliably (I tested up to 3 fingers, will test more when I get the chance).
* Pinching seems to work. It currently seems to only detect outward pinching, but that might be a configuration issue.
* Rotating is recognized semi-reliably. Touchegg sometimes confuses it with pinching.
* Double tapping is recognized, but touchegg also registers two single taps along with it, so it's kinda unusable. You can use either double- or single taps with a specific amount of fingers, otherwise you get a mess.
* Tap and hold is not recognized at all. Instead, a tap and a drag are registered.
