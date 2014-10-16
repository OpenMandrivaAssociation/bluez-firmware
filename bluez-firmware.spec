Name:		bluez-firmware
Summary:	Bluetooth firmware utilities
Version:	1.2
Release:	10
Source:		http://bluez.sf.net/download/%{name}-%{version}.tar.gz
URL:		http://bluez.sourceforge.net/
License:	Freeware
Group:		Communications
%rename		bluez-bluefw
BuildArch:	noarch

%description
Bluetooth(TM) Firmware. Package contains firmware images for some
   Bluetooth(TM) adapters. Currently supported are: 

* Broadcom Corporation BCM2033
* AVM Computersysteme Vertriebs GmbH BLUEFRITZ! USB

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., USA.

%prep
%setup -q

%build
%configure --libdir=/lib
%make
										
%install
%makeinstall_std


%files
%doc AUTHORS ChangeLog 
/lib/firmware/*
