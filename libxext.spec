%define major 6
%define libxext %mklibname xext %{major}
%define develname %mklibname xext -d

Name:		libxext
Summary:	X11 miscellaneous extension library
Epoch:		1
Version:	1.3.1
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXext-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xau) >= 1.0.0
BuildRequires:	pkgconfig(xdmcp) >= 1.0.0
BuildRequires:	x11-proto-devel >= 7.5
BuildRequires:	x11-util-macros >= 1.0.1

%description
Misc X Extension Library

%package -n %{libxext}
Summary:	X11 miscellaneous extension library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{EVRD}

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
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxext} = %{EVRD}
Provides:	libxext-devel = %{EVRD}
Obsoletes:	%{_lib}xext6-devel < 1:1.3.1
Obsoletes:	%{_lib}xext6-static-devel < 1:1.3.1

Conflicts:	libxorg-x11-devel < 7.0
Conflicts:	x11-proto-devel < 7.5

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


%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1:1.3.1-1
+ Revision: 783942
- version update 1.3.1

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:1.3.0-3
+ Revision: 745593
- rebuild
- disabled static build
- removed .la files
- employed major macro
- cleaned up spec

* Tue May 24 2011 Götz Waschk <waschk@mandriva.org> 1:1.3.0-2
+ Revision: 678154
- fix devel provides

* Sun May 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:1.3.0-1
+ Revision: 677457
- update to new version 1.3.0

* Fri Feb 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:1.2.0-2
+ Revision: 638320
- dropped major from devel and static pkg names
- added proper provides and obsoletes

* Thu Oct 28 2010 Thierry Vignaud <tv@mandriva.org> 1:1.2.0-1mdv2011.0
+ Revision: 589801
- adjust file list
- drop patch 0 (merged upstream)
- new release

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 1:1.1.2-1mdv2011.0
+ Revision: 556452
- new release

* Mon Jan 04 2010 Funda Wang <fwang@mandriva.org> 1:1.1.1-2mdv2010.1
+ Revision: 486084
- drop files conflicts with liblbxutil

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:1.1.1-1mdv2010.1
+ Revision: 463682
- New version: 1.1.1

* Tue Jul 21 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1:1.0.5-1mdv2010.0
+ Revision: 398286
- Revert libxext 1.0.99.3 update: it is development stuff and breaks
  x11-server 1.6.2 build, shouldn't pushed without updating x11-server
  and possibly other x11 packages to latest devel releases.

* Fri Jul 17 2009 Colin Guthrie <cguthrie@mandriva.org> 1.0.99.3-1mdv2010.0
+ Revision: 396717
- New version: 1.0.99.3

* Sun Feb 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.5-2mdv2009.1
+ Revision: 336167
- fix build
- update to new version 1.0.5

* Thu Nov 06 2008 Olivier Blin <blino@mandriva.org> 1.0.4-3mdv2009.1
+ Revision: 300368
- rebuild for new xcb

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-2mdv2009.0
+ Revision: 223072
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Feb 29 2008 Colin Guthrie <cguthrie@mandriva.org> 1.0.4-1mdv2008.1
+ Revision: 176693
- New version: 1.0.4

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 151679
- Update BuildRequires and rebuild.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2008.1
+ Revision: 129237
- kill re-definition of %%buildroot on Pixel's request
- enhanced summary
- enhanced description
- fix man pages extension

