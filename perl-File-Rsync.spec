#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Rsync
Summary:	File::Rsync - a wrapper module for rsync
Summary(pl.UTF-8):	File::Rsync - wrapper dla programu rsync
Name:		perl-File-Rsync
Version:	0.43
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fe745f0460454250bc4ed557de8f11ac
Patch0:		%{name}-misc.patch
URL:		http://search.cpan.org/dist/File-Rsync/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	rsync
%endif
Requires:	rsync
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Rsync is a Perl wrapper for the rsync program.

%description -l pl.UTF-8
File::Rsync jest wrapperem w Perlu dla programu rsync.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%{perl_vendorlib}/File/Rsync.pm
%dir %{perl_vendorlib}/File/Rsync
%{perl_vendorlib}/File/Rsync/Config.pm
%{_mandir}/man3/File::Rsync.*
%{_mandir}/man3/File::Config.*
