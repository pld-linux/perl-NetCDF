%include	/usr/lib/rpm/macros.perl
Summary:	Perl interface for NetCDF
Summary(pl.UTF-8):	Perlowy interfejs do biblioteki NetCDF
Name:		perl-NetCDF
Version:	1.2.4
Release:	1
License:	BSD-like
Group:		Development/Languages/Perl
Source0:	ftp://ftp.unidata.ucar.edu/pub/netcdf-perl/netcdf-perl-%{version}.tar.gz
# Source0-md5:	36b517662bda6a12a76f817acb49a993
URL:		http://www.unidata.ucar.edu/software/netcdf-perl/
BuildRequires:	netcdf-devel >= 3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The netCDF Perl package is a Perl extension module for accessing
scientific datasets in netCDF format based on version 2 of the netCDF
package.

Note: this package is deprecated (no longer actively developed,
through supported). One may want to use PDL::NetCDF instead.

%description -l pl.UTF-8
Pakiet netCDF Perl to moduł rozszerzenia Perla pozwalający na dostęp
do naukowych zbiorów danych w formacie netCDF, oparty na wersji 2
pakietu netCDF.

Uwaga: ten pakiet jest przestarzały (nie jest już aktywnie rozwijany,
choć jest wspierany). Zamiast niego można użyć modułu PDL::NetCDF.

%prep
%setup -q -n netcdf-perl-%{version}

%build
cd src
export PERL_MANDIR=%{_mandir}
export CPP_NETCDF=" "
export LD_NETCDF=" "
%configure2_13
cd perl
# Don't use pipes here: they generally don't work. Apply a patch.
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	PERL_MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc src/{COPYRIGHT,HISTORY,README}
%{perl_vendorarch}/NetCDF.pm
%dir %{perl_vendorarch}/auto/NetCDF
%{perl_vendorarch}/auto/NetCDF/NetCDF.bs
%attr(755,root,root) %{perl_vendorarch}/auto/NetCDF/NetCDF.so
%{perl_vendorarch}/auto/NetCDF/autosplit.ix
%{_mandir}/man1/netCDFPerl.1*
