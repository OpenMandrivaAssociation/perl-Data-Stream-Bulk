%define upstream_name    Data-Stream-Bulk
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	L<Path::Class::Dir> traversal
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-Stream-Bulk-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This module tries to find middle ground between one at a time and all at
once processing of data sets.

The purpose of this module is to avoid the overhead of implementing an
iterative api when this isn't necessary, without breaking forward
compatibility in case that becomes necessary later on.

The API optimizes for when a data set typically fits in memory and is
returned as an array, but the consumer cannot assume that the data set is
bounded.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 653563
- rebuild for updated spec-helper

* Sat Aug 28 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 573791
- update to 0.08

* Fri Jul 30 2010 Shlomi Fish <shlomif@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 563322
- import perl-Data-Stream-Bulk


* Fri Feb 05 2010 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist

