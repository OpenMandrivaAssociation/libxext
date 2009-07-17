%define libxext %mklibname xext 6
Name: libxext
Summary: X11 miscellaneous extension library
Version: 1.0.99.3
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxdmcp-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 7.4-21
BuildRequires: x11-util-macros >= 1.0.1

%description
Misc X Extension Library

#-----------------------------------------------------------

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

#-----------------------------------------------------------

%package -n %{libxext}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxext} = %{version}
Requires: x11-proto-devel >= 7.4-21
Provides: libxext-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0
Conflicts: x11-proto-devel < 7.4-21

%description -n %{libxext}-devel
Development files for %{name}

%files -n %{libxext}-devel
%defattr(-,root,root)
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXext.so
%{_libdir}/libXext.la
%{_libdir}/pkgconfig/xext.pc
%{_mandir}/man3/*.3*

#-----------------------------------------------------------

%package -n %{libxext}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxext}-devel = %{version}
Provides: libxext-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxext}-static-devel
Static development files for %{name}

%files -n %{libxext}-static-devel
%defattr(-,root,root)
%{_libdir}/libXext.a

#-----------------------------------------------------------

%prep
%setup -q -n libXext-%{version}

%build
%configure2_5x

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libxext}
%defattr(-,root,root)
%{_libdir}/libXext.so.6
%{_libdir}/libXext.so.6.4.0


