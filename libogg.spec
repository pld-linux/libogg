Summary:	Ogg Bitstream Library
Summary(pl):	Biblioteka obs³ugi strumieni bitowych Ogg
Name:		libogg
Version:	1.0rc2
Release:	2
Epoch:		1
License:	LGPL
Vendor:		Xiphophorus <team@xiph.org>
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.vorbis.com/files/rc2/unix/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.xiph.org/ogg/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libogg0

%description
Libogg is a library for manipulating ogg bitstreams. It handles both
making ogg bitstreams and getting packets from ogg bitstreams.

%description -l pl
Libogg jest bibliotek± do manipulacji strumieniami bitowymi ogg.
Obs³uguje ona zarówno tworzenie strumieni jak i uzyskiwanie pakietów
ze strumieni.

%package devel
Summary:	Ogg Bitstream Library Development
Summary(pl):	Pliki nag³ówkowe i dokumentacja developerska
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	libogg0-devel

%description devel
The libogg-devel package contains the header files and documentation
needed to develop applications with libogg.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja potrzebna do rozwijania aplikacji
u¿ywaj±cych biblioteki libogg.

%package static
Summary:	Ogg Bitstream Static Library
Summary(pl):	Biblioteka statyczna Ogg
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
The libogg-static package contains the static libraries of libogg.

%description -l pl static
Statyczna biblioteka libogg.

%prep
%setup -q 
%patch0 -p1

%build
rm missing
libtoolize --copy --force
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

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/*.{html,png}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/ogg
%{_aclocaldir}/ogg.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
