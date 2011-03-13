Summary:	Additional user level InfiniBand management utilities
Summary(pl.UTF-8):	Dodatkowe narzędzia zarządzające InfiniBand
Name:		ibutils
Version:	1.5.7
Release:	1
License:	BSD or GPL v2
Group:		Networking/Utilities
Source0:	http://www.openfabrics.org/downloads/ibutils/%{name}-%{version}.tar.gz
# Source0-md5:	82c7e95508f38caec4e8b8b5437598e0
Patch0:		%{name}-link.patch
URL:		http://www.openfabrics.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.3
BuildRequires:	libibmad-devel
BuildRequires:	libibumad-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 1:1.4.2
BuildRequires:	opensm-devel >= 1.7.0
BuildRequires:	tcl-devel >= 8.3
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional user level InfiniBand management utilities:
- ibdiag suite
- ibdm (Fabric utils)
- ibis (IB In-band Services)
- ibmgtsim

%description -l pl.UTF-8
Dodatkowe narzędzia zarządzające InfiniBand:
- pakiet ibdiag
- ibdm (narzędzia Fabric)
- ibis (IB In-band Services)
- ibmgtsim

%package libs
Summary:	InfiniBand utility libraries
Summary(pl.UTF-8):	Biblioteki narzędziowe InfiniBand
Group:		Libraries

%description libs
InfiniBand utility libraries.

%description libs -l pl.UTF-8
Biblioteki narzędziowe InfiniBand.

%package devel
Summary:	Header files for IB utility libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek narzędziowych IB
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libibmad-devel
Requires:	libibumad-devel
Requires:	libstdc++-devel
Requires:	opensm-devel >= 1.7.0
Requires:	tcl-devel >= 8.3

%description devel
Header files for IB utility libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek narzędziowych IB.

%package static
Summary:	Static IB utility libraries
Summary(pl.UTF-8):	Statyczne biblioteki narzędziowe IB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static IB utility libraries.

%description static -l pl.UTF-8
Statyczne biblioteki narzędziowe IB.

%prep
%setup -q
%patch0 -p1

for f in AUTHORS ChangeLog NEWS README THANKS ; do cp -l ibdm/${f} ${f}.ibdm ; done
for f in AUTHORS NEWS README ; do cp -l ibis/${f} ${f}.ibis ; done
for f in AUTHORS ChangeLog README ; do cp -l ibis/${f} ${f}.ibmgtsim ; done

%build
cd ibdm
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../ibmgtsim
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
cd ..
%configure \
	--enable-ibmgtsim
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/git_version.tcl

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS.* COPYING ChangeLog* NEWS.* README* THANKS.ibdm
%attr(755,root,root) %{_bindir}/IBMgtSim
%attr(755,root,root) %{_bindir}/RunSimTest
%attr(755,root,root) %{_bindir}/dump2psl.pl
%attr(755,root,root) %{_bindir}/dump2slvl.pl
%attr(755,root,root) %{_bindir}/ibdiagnet
%attr(755,root,root) %{_bindir}/ibdiagpath
%attr(755,root,root) %{_bindir}/ibdiagui
%attr(755,root,root) %{_bindir}/ibdmchk
%attr(755,root,root) %{_bindir}/ibdmsh
%attr(755,root,root) %{_bindir}/ibdmtr
%attr(755,root,root) %{_bindir}/ibis
%attr(755,root,root) %{_bindir}/ibmsquit
%attr(755,root,root) %{_bindir}/ibmssh
%attr(755,root,root) %{_bindir}/ibnlparse
%attr(755,root,root) %{_bindir}/ibtopodiff
%attr(755,root,root) %{_bindir}/mkSimNodeDir
%{_libdir}/ibdiagnet%{version}
%{_libdir}/ibdiagpath%{version}
%{_libdir}/ibdiagui%{version}
%dir %{_libdir}/ibdm%{version}
%attr(755,root,root) %{_libdir}/ibdm%{version}/libibdm.so.%{version}
%{_libdir}/ibdm%{version}/ibnl
%{_libdir}/ibdm%{version}/pkgIndex.tcl
%dir %{_libdir}/ibis%{version}
%attr(755,root,root) %{_libdir}/ibis%{version}/libibis.so.%{version}
%{_libdir}/ibis%{version}/pkgIndex.tcl
%{_datadir}/ibmgtsim
%{_mandir}/man1/IBMgtSim.1*
%{_mandir}/man1/RunSimTest.1*
%{_mandir}/man1/ibdiagnet.1*
%{_mandir}/man1/ibdiagpath.1*
%{_mandir}/man1/ibdiagui.1*
%{_mandir}/man1/ibdm-ibnl-file.1*
%{_mandir}/man1/ibdm-topo-file.1*
%{_mandir}/man1/ibdmchk.1*
%{_mandir}/man1/ibdmsh.1*
%{_mandir}/man1/ibdmtr.1*
%{_mandir}/man1/ibis.1*
%{_mandir}/man1/ibmsquit.1*
%{_mandir}/man1/ibmssh.1*
%{_mandir}/man1/ibtopodiff.1*
%{_mandir}/man1/mkSimNodeDir.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibdm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibdm.so.1
%attr(755,root,root) %{_libdir}/libibdmcom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibdmcom.so.1
%attr(755,root,root) %{_libdir}/libibmscli.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibmscli.so.1
%attr(755,root,root) %{_libdir}/libibsysapi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libibsysapi.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libibdm.so
%attr(755,root,root) %{_libdir}/libibdmcom.so
%attr(755,root,root) %{_libdir}/libibmscli.so
%attr(755,root,root) %{_libdir}/libibsysapi.so
%{_libdir}/libibdm.la
%{_libdir}/libibdmcom.la
%{_libdir}/libibmscli.la
%{_libdir}/libibsysapi.la
%{_includedir}/ibdm
%{_includedir}/ibmgtsim

%files static
%defattr(644,root,root,755)
%{_libdir}/libibdm.a
%{_libdir}/libibdmcom.a
%{_libdir}/libibmscli.a
%{_libdir}/libibsysapi.a
