Summary:	Ogg Bitstream Library
Summary(pl):	Biblioteka obs≥ugi strumieni bitowych Ogg
Summary(pt_BR):	Biblioteca libogg
Name:		libogg
Version:	1.0rc3
Release:	2
Epoch:		1
License:	LGPL
Vendor:		Xiphophorus <team@xiph.org>
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
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
Obs≥uguje ona zarÛwno tworzenie strumieni jak i uzyskiwanie pakietÛw
ze strumieni.

%description -l pt_BR
Ogg e' uma familia de diversos projetos de multimÌdia e processamento
de sinais. libogg È a biblioteca do formato de codec bitstream para o
codec Vorbis, formando o encoder/decoder de ·udio Ogg Vorbis.

%package devel
Summary:	Ogg Bitstream Library Development
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja developerska
Summary(pt_BR):	Bibliotecas para desenvolvimento com o Ogg Vorbis
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Obsoletes:	libogg0-devel

%description devel
The libogg-devel package contains the header files and documentation
needed to develop applications with libogg.

%description -l pl devel
Pliki nag≥Ûwkowe i dokumentacja potrzebna do rozwijania aplikacji
uøywaj±cych biblioteki libogg.

%description -l pt_BR devel
Bibliotecas e arquivos de inclus„o para desenvolvimento com o Ogg
Vorbis.

%package static
Summary:	Ogg Bitstream Static Library
Summary(pl):	Biblioteka statyczna Ogg
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com o Ogg Vorbis
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
The libogg-static package contains the static libraries of libogg.

%description -l pl static
Statyczna biblioteka libogg.

%description -l pt_BR static
Bibliotecas est·ticas para desenvolvimento com o Ogg Vorbis.

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
