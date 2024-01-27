THE HYPERVISOR

there's a critical bug inside virtualbox disallowing us to take screenshot:

https://www.virtualbox.org/ticket/19740

while py2 version of virtualbox-python is broken and not usable, we must recompile the box right up from the source. consider uploading it to elsewhere.

just assume that all staffs in oracle are dead now.

either switch to another language or just rebuild the thing.

offtopic: is it nice to test custom(handcrafted) OS from VM?

root@kali ~/A/V/s/l/x/p/src# cat VariantUtils.cpp  | grep -n PyUnicode_FromStringAndSize
136:                    ret = PyUnicode_FromStringAndSize(NULL, s.Length());
631:            return PyUnicode_FromStringAndSize( (char *)array_ptr, sequence_size );
1906:           ret = PyUnicode_FromStringAndSize( ((char *)ns_v.ptr), 1 );
2023:                   ret = PyUnicode_FromStringAndSize( *((char **)ns_v.ptr), string_size );
2282:           ret = PyUnicode_FromStringAndSize(&temp, 1);
2385:                   ret = PyUnicode_FromStringAndSize(t, string_size);

understand the system deeper, create some shared nodes between dos and the main OS, via network stack or filesystem or something reasonable. otherwise we can only manually type into the console, which could be slow sometimes.

apt-get install acpica-tools chrpath doxygen g++-multilib libasound2-dev libcap-dev \
        libcurl4-openssl-dev libdevmapper-dev libidl-dev libopus-dev libpam0g-dev \
        libpulse-dev libqt5opengl5-dev libqt5x11extras5-dev libsdl1.2-dev libsdl-ttf2.0-dev \
        libssl-dev libvpx-dev libxcursor-dev libxinerama-dev libxml2-dev libxml2-utils \
        libxmu-dev libxrandr-dev make nasm python3-dev python-dev qttools5-dev-tools \
        texlive texlive-fonts-extra texlive-latex-extra unzip xsltproc \
        \
        default-jdk libstdc++5 libxslt1-dev linux-kernel-headers makeself \
        mesa-common-dev subversion yasm zlib1g-dev

the linux-kernel-headers is missing from package list.

http://cncc.bingj.com/cache.aspx?q=compile+virtualbox+from+source&d=4933624692742038&mkt=en-US&setlang=en-US&w=CNTaoDdCJ9TDjc4K0sV3K4XyB9Py0mTC

apt-get install ia32-libs libc6-dev-i386 lib32gcc1 lib32stdc++6

dpkg: error processing package tex-common (--configure):
 installed tex-common package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 tex-common

the problem inside that piece of code is in fact with the sdk(vboxapi), not with virtualbox main infrastructure. so in order to get things working, you need to find how to manually replace and reinstall vboxapi after virtualbox installation.

consider qemu for better console support and less computational cost.
