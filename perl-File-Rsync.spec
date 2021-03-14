#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	File
%define		pnam	Rsync
Summary:	File::Rsync - a wrapper module for rsync
Summary(pl.UTF-8):	File::Rsync - wrapper dla programu rsync
Name:		perl-File-Rsync
Version:	0.49
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3929283d5391b6599799072c34a9e93e
URL:		https://metacpan.org/release/File-Rsync
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-IPC-Run3
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Simple
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
%{_mandir}/man3/File::Rsync.3pm*
