Summary:	Ogg Bitstream Library
Summary(pl):	Biblioteka obs�ugi strumieni bitowych Ogg
Summary(pt_BR):	Biblioteca libogg
Name:		libogg
Version:	1.1.3
Release:	2
Epoch:		2
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.gz
# Source0-md5:	eaf7dc6ebbff30975de7527a80831585
Patch0:		%{name}-ac_fixes.patch
URL:		http://www.xiph.org/ogg/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Obsoletes:	libogg0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libogg is a library for manipulating Ogg bitstreams. It handles both
making Ogg bitstreams and getting packets from Ogg bitstreams.

%description -l pl
Libogg jest bibliotek� do manipulacji strumieniami bitowymi Ogg.
Obs�uguje ona zar�wno tworzenie strumieni jak i uzyskiwanie pakiet�w
ze strumieni.

%description -l pt_BR
Ogg e' uma familia de diversos projetos de multim�dia e processamento
de sinais. libogg � a biblioteca do formato de codec bitstream para o
codec Vorbis, formando o encoder/decoder de �udio Ogg Vorbis.

%package devel
Summary:	Ogg Bitstream Library Development
Summary(pl):	Pliki nag��wkowe i dokumentacja developerska
Summary(pt_BR):	Bibliotecas para desenvolvimento com o Ogg Vorbis
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libogg0-devel

%description devel
The libogg-devel package contains the header files and documentation
needed to develop applications with libogg.

%description devel -l pl
Pliki nag��wkowe i dokumentacja potrzebna do rozwijania aplikacji
u�ywaj�cych biblioteki libogg.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento com o Ogg
Vorbis.

%package static
Summary:	Ogg Bitstream Static Library
Summary(pl):	Biblioteka statyczna Ogg
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com o Ogg Vorbis
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
The libogg-static package contains the static libraries of libogg.

%description static -l pl
Statyczna biblioteka libogg.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com o Ogg Vorbis.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

mv -f $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} devel-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES COPYING README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc devel-docs/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/ogg
%{_aclocaldir}/ogg.m4
%{_pkgconfigdir}/ogg.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
