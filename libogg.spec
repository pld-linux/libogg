#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Ogg Bitstream Library
Summary(pl.UTF-8):	Biblioteka obsługi strumieni bitowych Ogg
Summary(pt_BR.UTF-8):	Biblioteca libogg
Name:		libogg
Version:	1.3.3
Release:	1
Epoch:		2
License:	BSD
Group:		Libraries
Source0:	https://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.xz
# Source0-md5:	87ed742047f065046eb6c36745d871b8
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.xiph.org/ogg/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.6
BuildRequires:	libtool
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	libogg0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libogg is a library for manipulating Ogg bitstreams. It handles both
making Ogg bitstreams and getting packets from Ogg bitstreams.

%description -l pl.UTF-8
Libogg jest biblioteką do manipulacji strumieniami bitowymi Ogg.
Obsługuje ona zarówno tworzenie strumieni jak i uzyskiwanie pakietów
ze strumieni.

%description -l pt_BR.UTF-8
Ogg e' uma familia de diversos projetos de multimídia e processamento
de sinais. libogg é a biblioteca do formato de codec bitstream para o
codec Vorbis, formando o encoder/decoder de áudio Ogg Vorbis.

%package devel
Summary:	Ogg Bitstream Library Development
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja developerska
Summary(pt_BR.UTF-8):	Bibliotecas para desenvolvimento com o Ogg Vorbis
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libogg0-devel

%description devel
The libogg-devel package contains the header files and documentation
needed to develop applications with libogg.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja potrzebna do rozwijania aplikacji
używających biblioteki libogg.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento com o Ogg
Vorbis.

%package static
Summary:	Ogg Bitstream Static Library
Summary(pl.UTF-8):	Biblioteka statyczna Ogg
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com o Ogg Vorbis
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
The libogg-static package contains the static libraries of libogg.

%description static -l pl.UTF-8
Statyczna biblioteka libogg.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com o Ogg Vorbis.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

mv -f $RPM_BUILD_ROOT%{_docdir}/%{name} devel-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING README.md
%attr(755,root,root) %{_libdir}/libogg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libogg.so.0

%files devel
%defattr(644,root,root,755)
%doc devel-docs/*
%attr(755,root,root) %{_libdir}/libogg.so
%{_libdir}/libogg.la
%{_includedir}/ogg
%{_aclocaldir}/ogg.m4
%{_pkgconfigdir}/ogg.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libogg.a
%endif
