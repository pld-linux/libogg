Summary:	Ogg Bitstream Library
Name:		libogg
Version:	1.0.0_cvs2000.10.29
Release:	1
Group:		Libraries/Multimedia
Group(pl):	Biblioteki/Multimedia
Copyright:	LGPL
URL:		http://www.xiph.org/
Vendor:		Xiphophorus <team@xiph.org>
Source:		ftp://www.xiph.org/ogg/vorbis/download/vorbis_nightly_cvs.tgz
Patch0:		%{name}-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libogg is a library for manipulating ogg bitstreams.  It handles
both making ogg bitstreams and getting packets from ogg bitstreams.

%package devel
Summary: 	Ogg Bitstream Library Development
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The libogg-devel package contains the header files and documentation
needed to develop applications with libogg.

%package static
Summary: 	Ogg Bitstream Library Development
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}-%{release}

%description static
The libogg-static package contains the static libraries of libogg.

%prep
%setup -q -n ogg
%patch0 -p1

%build
if [ ! -f configure ]; then
  CFLAGS="$RPM_FLAGS" ./autogen.sh --prefix=%{_prefix}
else
  CFLAGS="$RPM_FLAGS" %configure --prefix=%{_prefix}
fi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(644,root,root,755)
%doc AUTHORS
%doc CHANGES
%doc COPYING
%doc README
%attr(755,root,root) %{_libdir}/libogg.so*
%attr(755,root,root) %{_libdir}/libogg.la

%files devel
%defattr(644,root,root,755)
%doc doc/index.html
%doc doc/framing.html
%doc doc/oggstream.html
%doc doc/white-ogg.png
%doc doc/white-xifish.png
%doc doc/stream.png
%{_includedir}/ogg/ogg.h
%{_includedir}/ogg/os_types.h
%{_includedir}/ogg/config_types.h
/usr/share/aclocal/ogg.m4
%attr(755,root,root) %{_bindir}/ogg-config

%files static
%attr(644,root,root) %{_libdir}/*.a

%clean 
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig
