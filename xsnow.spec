Name:           xsnow
Version:        1.42 
Release:        22%{?dist}
Summary:        An X Window System based dose of Christmas cheer

Group:          Amusements/Graphics
License:        Distributable
URL:            http://dropmix.xs4all.nl/rick/Xsnow/
Source0:        http://dropmix.xs4all.nl/rick/Xsnow/%{name}-%{version}.tar.gz
# Fedora Core 3
Patch0:         %{name}-1.42-misc.patch
# Debian
Patch1:         %{name}-1.42-fixoptions.patch
Patch2:         %{name}-1.42-Imakefile.patch
Patch3:         %{name}-1.42-manpage.patch
Patch4:         %{name}-1.42-vroot.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXext-devel
BuildRequires:  xorg-x11-proto-devel

BuildRequires:  imake

%description
The Xsnow toy provides a continual gentle snowfall, trees, and Santa
Claus flying his sleigh around the screen.  Xsnow is only for the X
Window System, though; consoles just get coal.


%prep
%setup -q
# Redraw windows when exiting
%patch0 -p1
# Patch broken -nokeepsnowonwindows and -nokeepsnow options
%patch1 -p1
# Do not link lm
%patch2 -p1
# xsnow.man belongs to section 6
%patch3 -p1
# Use vroot.h from xscreensaver 4.23
%patch4 -p1


%build
xmkmf -a
make CDEBUGFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Install man page
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 644 xsnow.man $RPM_BUILD_ROOT%{_mandir}/man6/xsnow.6


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%doc README


%changelog
* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.42-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.42-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.42-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.42-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Mar 12 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.42-18
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Feb 09 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.42-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 12 2009 Andrea Musuruane <musuruan@gmail.com> 1.42-16
- first release for RPM Fusion
- updated package to Fedora guidelines
- used Debian patches

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Than Ngo <than@redhat.com> 1.42-14
- cleanup codes, #116665

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Nov 26 2003 Than Ngo <than@redhat.com> 1.42-12
- BuildRequires on XFree86-devel

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Nov  7 2002 Than Ngo <than@redhat.com> 1.42-9
- fix unpackaged files issue

* Mon Aug 26 2002 Than Ngo <than@redhat.com> 1.42-8
- get rid of desktop file (bug #69556)
 
* Wed Jul 24 2002 Than Ngo <than@redhat.com> 1.42-7
- desktop file issue (bug #69556)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Apr 24 2002 Than Ngo <than@redhat.com> 1.42-4
- add missing icon

* Mon Feb 25 2002 Than Ngo <than@redhat.com> 1.42-3
- rebuild in new enviroment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 21 2001 Than Ngo <than@redhat.com> 1.42-1
- update to 1.42
- add Url
- fix bug #53192, #53194, #52132

* Mon May 21 2001 Tim Powers <timp@redhat.com>
- built for the distro

* Tue Nov 7 2000 Than Ngo <than@redhat.com>
- clean up specfile

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Thu Jul 13 2000 Than Ngo <than@redhat.de>
- rebuilt

* Thu Jun 01 2000 Than Ngo <than@redhat.de>
- rebuild for 7.0
- gzip man page
- remove wmconfig/xsnow, add xsnow.desktop

* Tue Jul 27 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Mon Dec 20 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc

