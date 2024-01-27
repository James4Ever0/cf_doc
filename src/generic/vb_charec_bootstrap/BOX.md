here's the hardware version of lazero.

the input source for a standard PC is easy to establish.

It does not grarentee to have the same image or sound.

[PC] - [USB] - [file sharing/ HID/ camera/ more]
     - [HDMI] - [screen imaging/ sound]
     - [sound jack] - [sound io]
     - [network] - [ipc/ relay]

due to limitation of current phone, it is recommend to develop hardware hypervisor to take control of these devices, also applicable for arbitrary OS. anyway, developing a custom OS ordigging deeper into current OS is also great.

[Phone] - [Main Plug] - [usb/ video]
        - [audio jack] - [audio io]
	- [internal connection] - [video/ audio/ touch]
	- [card slot] - [wifi/ storage]

[custom device] - [standard port emulation]
                - [supervisor port]
