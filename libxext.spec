%define major 6
%define libxext %mklibname xext %{major}
%define devname %mklibname xext -d

# Workaround for 32-bit gcc LTO
# No damage done because we manually enable
# LTO for the 64-bit build
%global _disable_lto 1

%global optflags %{optflags} -O3

# libxext is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif
%if %{with compat32}
%define lib32xext libxext%{major}
%define dev32name libxext-devel
%endif

Summary:	X11 miscellaneous extension library
Name:		libxext
Epoch:		1
Version:	1.3.4
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xau) >= 1.0.0
BuildRequires:	pkgconfig(xdmcp) >= 1.0.0
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
%if %{with compat32}
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
%endif

%description
Misc X Extension Library.

%package -n %{libxext}
Summary:	X11 miscellaneous extension library
Group:		Development/X11

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

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxext} = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32xext}
Summary:	X11 miscellaneous extension library (32-bit)
Group:		Development/X11

%description -n %{lib32xext}
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

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32xext} = %{EVRD}
Requires:	%{devname} = %{EVRD}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXext-%{version} -p1
export CONFIGURE_TOP="`pwd`"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

mkdir build
cd build
CFLAGS="%{optflags} -flto" LDFLAGS="%{optflags} -flto" %configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build
rm -rf %{buildroot}%{_datadir}/doc/libXext

%files -n %{libxext}
%{_libdir}/libXext.so.%{major}*

%files -n %{devname}
%doc specs/*.xml
%{_libdir}/libXext.so
%{_libdir}/pkgconfig/xext.pc
%{_includedir}/X11/extensions/*.h
%{_mandir}/man3/*.3*

%if %{with compat32}
%files -n %{lib32xext}
%{_prefix}/lib/libXext.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXext.so
%{_prefix}/lib/pkgconfig/*.pc
%endif
