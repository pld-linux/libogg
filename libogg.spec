Summary:	Ogg Bitstream Library
Name:		libogg
Version:	1.0.0_cvs2000.10.29
Release:	1
License:	LGPL
Vendor:		Xiphophorus <team@xiph.org>
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://www.xiph.org/ogg/vorbis/download/vorbis_nightly_cvs.tgz
Patch0:		%{name}-make.patch
Patch1:		libogg-ac_fixes.patch
URL:		http://www.xiph.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libogg is a library for manipulating ogg bitstreams. It handles both
making ogg bitstreams and getting packets from ogg bitstreams.

%package devel
Summary:	Ogg Bitstream Library Development
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The libogg-devel package contains the header files and documentation
needed to develop applications with libogg.

%package static
Summary:	Ogg Bitstream Library Development
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
The libogg-static package contains the static libraries of libogg.

%prep
%setup -q -n ogg
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf AUTHORS CHANGES README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/lib*.la

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*.{html,png}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/ogg-config
%{_includedir}/ogg
%{_aclocaldir}/ogg.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
