Summary:	Ogg Bitstream Library
Summary(pl):	Biblioteka obs³ugi strumieni bitowych Ogg
Summary(pt_BR):	Biblioteca libogg
Name:		libogg
Version:	1.1
Release:	2
Epoch:		2
License:	BSD
Group:		Libraries
Source0:	http://www.vorbis.com/files/1.0.1/unix/%{name}-%{version}.tar.gz
# Source0-md5:	461d7097bf47864b872085a94ff94e10
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-am18.patch
URL:		http://www.vorbis.com/
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

%description -l pt_BR
Ogg e' uma familia de diversos projetos de multimídia e processamento
de sinais. libogg é a biblioteca do formato de codec bitstream para o
codec Vorbis, formando o encoder/decoder de áudio Ogg Vorbis.

%package devel
Summary:	Ogg Bitstream Library Development
Summary(pl):	Pliki nag³ówkowe i dokumentacja developerska
Summary(pt_BR):	Bibliotecas para desenvolvimento com o Ogg Vorbis
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Obsoletes:	libogg0-devel

%description devel
The libogg-devel package contains the header files and documentation
needed to develop applications with libogg.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja potrzebna do rozwijania aplikacji
u¿ywaj±cych biblioteki libogg.

%description devel -l pt_BR
Bibliotecas e arquivos de inclusão para desenvolvimento com o Ogg
Vorbis.

%package static
Summary:	Ogg Bitstream Static Library
Summary(pl):	Biblioteka statyczna Ogg
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com o Ogg Vorbis
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
The libogg-static package contains the static libraries of libogg.

%description static -l pl
Statyczna biblioteka libogg.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com o Ogg Vorbis.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
