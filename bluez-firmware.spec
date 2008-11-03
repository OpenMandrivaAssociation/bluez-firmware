%define	name	bluez-firmware
%define version 1.2
%define release %mkrel 4

Name: 		%{name}
Summary: 	Bluetooth firmware utilities
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://bluez.sourceforge.net/
License:	Freeware
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Provides:	bluez-bluefw
Obsoletes:	bluez-bluefw

%description
Bluetooth(TM) Firmware. Package contains firmware images for some
   Bluetooth(TM) adapters. Currently supported are: 

* Broadcom Corporation BCM2033
* AVM Computersysteme Vertriebs GmbH BLUEFRITZ! USB

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., USA.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog 
%{_libdir}/firmware/*

