Summary:	Hierarchical pool based memory system
Name:		talloc
Version:	2.0.7
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	http://samba.org/ftp/talloc/talloc-%{version}.tar.gz
# Source0-md5:	dbfb3146f4cc47054e13b8a2988299f9
URL:		http://talloc.samba.org/
BuildRequires:	autoconf
BuildRequires:	docbook-style-xsl
BuildRequires:	libxslt-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The talloc library implements a hierarchical allocator with
destructors.

%package devel
Summary:	Development files for the talloc library
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development files needed to create programs that link against the
talloc library.

%prep
%setup -q

%build
export CC="%{__cc}"
export CXX="%{__cxx}"
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcxxflags}"
export LDFLAGS="%{rpmldflags}"
./buildtools/bin/waf configure	\
	--disable-python	\
        --libdir=%{_libdir}     \
        --mandir=%{_mandir}     \
        --prefix=%{_prefix}     \
        --nocache

./buildtools/bin/waf -v build

%install
rm -rf $RPM_BUILD_ROOT

./buildtools/bin/waf -v install \
	--destdir=$RPM_BUILD_ROOT

chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so*

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libtalloc.so.?
%attr(755,root,root) %{_libdir}/libtalloc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtalloc.so
%{_includedir}/talloc.h
%{_pkgconfigdir}/talloc.pc
%{_mandir}/man3/talloc.3*

