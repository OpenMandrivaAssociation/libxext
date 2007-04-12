%define libxext %mklibname xext 6
Name: libxext
Summary:  Misc X Extension Library
Version: 1.0.3
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxdmcp-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Misc X Extension Library

#-----------------------------------------------------------

%package -n %{libxext}
Summary:  Misc X Extension Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxext}
Misc X Extension Library

#-----------------------------------------------------------

%package -n %{libxext}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxext} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxext-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxext}-devel
Development files for %{name}

%files -n %{libxext}-devel
%defattr(-,root,root)
%{_libdir}/libXext.so
%{_libdir}/libXext.la
%{_libdir}/pkgconfig/xext.pc
%{_mandir}/man3/*.3*.bz2

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
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxext}
%defattr(-,root,root)
%{_libdir}/libXext.so.6
%{_libdir}/libXext.so.6.4.0


