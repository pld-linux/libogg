Summary:	Ogg Bitstream Library
Summary(pl):	Biblioteka obs³ugi strumieni bitowych Ogg
Summary(pt_BR):	Biblioteca libogg
Name:		libogg
Version:	1.0
Release:	1
Epoch:		1
License:	LGPL
Vendor:		Xiphophorus <team@xiph.org>
Group:		Libraries
Source0:	http://www.xiph.org/ogg/vorbis/download/%{name}-%{version}.tar.gz
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

%description -l pt_BR
Ogg e' uma familia de diversos projetos de multimídia e processamento
de sinais. libogg é a biblioteca do formato de codec bitstream para o
codec Vorbis, formando o encoder/decoder de áudio Ogg Vorbis.

%package devel
Summary:	Ogg Bitstream Library Development
Summary(pl):	Pliki nag³ówkowe i dokumentacja developerska
Summary(pt_BR):	Bibliotecas para desenvolvimento com o Ogg Vorbis
Group:		Development/Libraries
Requires:	%{name} = %{version}
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
Requires:	%{name}-devel = %{version}

%description static
The libogg-static package contains the static libraries of libogg.

%description static -l pl
Statyczna biblioteka libogg.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com o Ogg Vorbis.

%prep
%setup -q
%patch0 -p1

%build
rm missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README doc/*.{html,png} doc/ogg/
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/ogg
%{_aclocaldir}/ogg.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
