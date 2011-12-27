%define major 6
%define libxext %mklibname xext %{major}
%define develname %mklibname xext -d

Name: libxext
Summary: X11 miscellaneous extension library
Epoch: 1
Version: 1.3.0
Release: 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxdmcp-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 7.5
BuildRequires: x11-util-macros >= 1.0.1

%description
Misc X Extension Library

%package -n %{libxext}
Summary: X11 miscellaneous extension library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxext}
LibXext provides an X Window System client interface to several extensions to
the X protocol. 
The supported protocol extensions are: 
- DOUBLE-BUFFER (DBE), the Double Buffer extension;
- DPMS, the VESA Display Power Management System extension;
- Extended-Visual-Information (EVI), an extension for gathering extra
  information about the X server's visuals;
- LBX, the Low Bandwidth X extension;
- MIT-SHM, the MIT X client/server shared memory extension;
- MIT-SUNDRY-NONSTANDARD, a miscellaneous extension by MIT;
- Multi-Buffering, the multi-buffering and stereo display extension;
- SECURITY, the X security extension;
- SHAPE, the non-rectangular shaped window extension;
- SYNC, the X synchronization extension;
- TOG-CUP, the Open Group's Colormap Utilization extension;
- XC-APPGROUP, the X Consortium's Application Group extension;
- XC-MISC, the X Consortium's resource ID querying extension;
- XTEST, the X test extension (this is one of two client-side implementations;
  the other is in the libXtst library, provided by the libxtst6 package);

LibXext also provides a small set of utility functions to aid authors of client
APIs for X protocol extensions.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxext} = %{epoch}:%{version}-%{release}
Provides: libxext-devel = %{epoch}:%{version}-%{release}
Obsoletes: %{_lib}xext6-devel
Obsoletes: %{_lib}xext6-static-devel

Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.5

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXext-%{version}

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%_datadir/doc/libXext

%files -n %{libxext}
%{_libdir}/libXext.so.%{major}*

%files -n %{develname}
%doc specs/*.xml
%{_libdir}/libXext.so
%{_libdir}/pkgconfig/xext.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/*.3*

