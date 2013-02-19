Summary:	A client library and example client for the Tivo vstream server
Summary(pl.UTF-8):	Biblioteka kliencka i przykładowy klient serwera vstream Tivo
Name:		vstream-client
Version:	1.2.1.1
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/vstream-client/downloads/list
Source0:	http://vstream-client.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	4f2fc3e5835592f5d8c230aaacd6a7b6
Patch0:		%{name}-shared.patch
URL:		http://code.google.com/p/vstream-client/
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# needs external vstream_error() function
%define		skip_post_check_so	libvstream-client.*

%description
This is a fork off of the vstream library from the tivo-mplayer
project. It has been stripped down to just the client code, and
includes an example client application.

%description -l pl.UTF-8
Ta biblioteka to odgałęzienie biblioteki vstream z projektu
tivo-mplayer. Została okrojona do wyłącznie klienckiego kodu,
ponadto zawiera przykładową aplikację kliencką.

%package devel
Summary:	Header files for vstream-client library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki vstream-client
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for vstream-client library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki vstream-client.

%package static
Summary:	Static vstream-client library
Summary(pl.UTF-8):	Statyczna biblioteka vstream-client
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static vstream-client library.

%description static -l pl.UTF-8
Statyczna biblioteka vstream-client.

%prep
%setup -q
%patch0 -p1

%build
# NOTE: not autoconf configure
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--incdir=%{_includedir}

%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	INCDIR=$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vstream-client
%attr(755,root,root) %{_libdir}/libvstream-client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvstream-client.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvstream-client.so
%{_libdir}/libvstream-client.la
%{_includedir}/vstream-client.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libvstream-client.a
