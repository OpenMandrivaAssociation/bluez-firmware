%define	name	bluez-firmware
%define version 1.2
%define release %mkrel 2

Name: 		%{name}
Summary: 	Bluetooth firmware utilities
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://bluez.sourceforge.net/
License:	GPL+
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	bluez-bluefw
Obsoletes:	bluez-bluefw

%description
Bluetooth(TM) Firmware. Package contains firmware images for some
   Bluetooth(TM) adapters. Currently supported are: * Broadcom
   Corporation BCM2033

* AVM Computersysteme Vertriebs GmbH BLUEFRITZ! USB

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., USA.

%prep
%setup -q
# use sanitized kernel headers whenever possible
#mkdir -p fake-linux/include
#cp -a /usr/src/linux/include/pcmcia/ fake-linux/include/

%build
%configure2_5x  --mandir=%{_mandir}
%make CFLAGS="$RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install
#%makeinstall fwdir=$RPM_BUILD_ROOT%{_datadir}/bluetooth/firmware usbdir=$RPM_BUILD_ROOT%{_sysconfdir}/udev/agents.d/usb
#perl -p -i -e 's|exec /sbin/bluefw|exec /usr/sbin/bluefw||g' $RPM_BUILD_ROOT%{_sysconfdir}/udev/agents.d/usb/bluefw 

# use udev rules instead of hotplug usermap
#mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d
#/usr/sbin/udev_import_usermap --no-modprobe usb $RPM_BUILD_ROOT%{_sysconfdir}/udev/agents.d/usb/bluefw.usermap > $RPM_BUILD_ROOT%{_sysconfdir}/udev/#rules.d/70-bluefw.rules
#rm -f $RPM_BUILD_ROOT%{_sysconfdir}/udev/agents.d/usb/bluefw.usermap

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog 
%{_libdir}/firmware/*

